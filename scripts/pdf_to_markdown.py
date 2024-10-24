r"""
# PDF To Markdown

## Setup

```bash
python -m pip install pymupdf markdownify pdf2image
```

## Usage

```bash
python pdf_to_markdown.py example.pdf output.md $(mktemp -d) --max-workers $(proc) --mode serial
```
"""

import fitz  # PyMuPDF
from markdownify import markdownify as md
import os
import argparse
import asyncio
from concurrent.futures import ProcessPoolExecutor


def extract_text_from_page(args):
    """Extracts text from a single page in the PDF document."""
    pdf_path, page_num = args
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num)
        text = page.get_text("text")
        doc.close()
        return text
    except Exception as e:
        print(f"Error extracting text from page {page_num + 1}: {e}")
        return ""  # Return empty string on error


def extract_images_from_page(args):
    """Extracts images from a single page and saves them."""
    pdf_path, page_num, output_folder = args
    saved_images = []
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(
                output_folder, f"page_{page_num+1}_img_{img_index}.{image_ext}"
            )

            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            saved_images.append(image_path)
        doc.close()
        return saved_images
    except Exception as e:
        print(f"Error extracting images from page {page_num + 1}: {e}")
        return []  # Return empty list on error


async def extract_text_serial(pdf_path):
    """Extracts text from all PDF pages serially."""
    text_pages = []
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            try:
                page = doc.load_page(page_num)
                text = page.get_text("text")
                text_pages.append(text)
            except Exception as e:
                print(f"Error extracting text from page {page_num + 1}: {e}")
                text_pages.append("")  # Append empty string on error
        doc.close()
    except Exception as e:
        print(f"Error opening PDF file '{pdf_path}': {e}")
        return ""  # Return empty string on error
    return "\n".join(text_pages)


async def extract_text_parallel(pdf_path, executor, max_workers):
    """Extracts text from all PDF pages using ProcessPoolExecutor."""
    try:
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        doc.close()
    except Exception as e:
        print(f"Error opening PDF file '{pdf_path}': {e}")
        return

    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(max_workers)
    tasks = []

    async def semaphore_task(args):
        async with semaphore:
            return await loop.run_in_executor(executor, extract_text_from_page, args)

    for page_num in range(num_pages):
        task = semaphore_task((pdf_path, page_num))
        tasks.append(task)
        # Process tasks in batches to limit memory usage
        if len(tasks) >= max_workers:
            text_pages = await asyncio.gather(*tasks)
            for text in text_pages:
                yield text
            tasks = []

    # Process any remaining tasks
    if tasks:
        text_pages = await asyncio.gather(*tasks)
        for text in text_pages:
            yield text


async def convert_pdf_to_markdown(
    pdf_path, output_md_path, mode, executor=None, max_workers=1
):
    """Converts the extracted PDF text to Markdown."""
    try:
        if mode == "serial":
            text = await extract_text_serial(pdf_path)
            # Convert the text to markdown format using markdownify
            markdown_text = md(text)
        else:
            # Parallel mode
            markdown_text = ""
            async for text in extract_text_parallel(pdf_path, executor, max_workers):
                # Convert each page's text to markdown and append
                markdown_text += md(text)
    except Exception as e:
        print(f"Error converting PDF to Markdown: {e}")
        return False  # Indicate failure

    try:
        # Save the markdown text to the output file
        with open(output_md_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_text)
    except Exception as e:
        print(f"Error writing Markdown output file '{output_md_path}': {e}")
        return False  # Indicate failure

    return True  # Indicate success


def extract_images_serial(pdf_path, output_folder):
    """Extracts images from the PDF and saves them serially."""
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception as e:
            print(f"Error creating output folder '{output_folder}': {e}")
            return False  # Indicate failure

    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            image_paths = extract_images_from_page((pdf_path, page_num, output_folder))
        doc.close()
        print(f"Images saved to {output_folder}")
    except Exception as e:
        print(f"Error extracting images: {e}")
        return False  # Indicate failure

    return True  # Indicate success


async def extract_images_parallel(pdf_path, output_folder, executor, max_workers):
    """Extracts images from the PDF and saves them using ProcessPoolExecutor."""
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception as e:
            print(f"Error creating output folder '{output_folder}': {e}")
            return False  # Indicate failure

    try:
        doc = fitz.open(pdf_path)
        num_pages = len(doc)
        doc.close()
    except Exception as e:
        print(f"Error opening PDF file '{pdf_path}': {e}")
        return False  # Indicate failure

    loop = asyncio.get_event_loop()
    semaphore = asyncio.Semaphore(max_workers)
    tasks = []

    async def semaphore_task(args):
        async with semaphore:
            return await loop.run_in_executor(executor, extract_images_from_page, args)

    for page_num in range(num_pages):
        task = semaphore_task((pdf_path, page_num, output_folder))
        tasks.append(task)
        # Process tasks in batches to limit memory usage
        if len(tasks) >= max_workers:
            await asyncio.gather(*tasks)
            tasks = []

    # Process any remaining tasks
    if tasks:
        await asyncio.gather(*tasks)
    print(f"Images saved to {output_folder}")
    return True  # Indicate success


async def main(pdf_file, markdown_output, image_output_folder, mode, max_workers):
    # Validate input PDF file
    if not os.path.isfile(pdf_file):
        print(f"Error: PDF file '{pdf_file}' does not exist.")
        return

    # Ensure output directories exist
    output_folder = os.path.dirname(markdown_output)
    if output_folder and not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
        except Exception as e:
            print(f"Error creating output directory '{output_folder}': {e}")
            return

    if mode == "serial":
        # Serial processing
        success = await convert_pdf_to_markdown(pdf_file, markdown_output, mode)
        if not success:
            print("Failed to convert PDF to Markdown.")
            return
        success = extract_images_serial(pdf_file, image_output_folder)
        if not success:
            print("Failed to extract images from PDF.")
            return
    else:
        # Parallel processing
        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            success = await convert_pdf_to_markdown(
                pdf_file, markdown_output, mode, executor, max_workers
            )
            if not success:
                print("Failed to convert PDF to Markdown.")
                return
            success = await extract_images_parallel(
                pdf_file, image_output_folder, executor, max_workers
            )
            if not success:
                print("Failed to extract images from PDF.")
                return

    print(f"Markdown saved to {markdown_output}")


if __name__ == "__main__":
    # Setup argparse to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Convert a PDF to Markdown and extract images."
    )
    parser.add_argument(
        "pdf_file", type=str, help="The path to the PDF file to be converted."
    )
    parser.add_argument(
        "markdown_output",
        type=str,
        help="The path where the output Markdown file will be saved.",
    )
    parser.add_argument(
        "image_output_folder",
        type=str,
        help="The folder where extracted images will be saved.",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["serial", "parallel"],
        default="serial",
        help="Processing mode: 'serial' or 'parallel'.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=4,
        help="Maximum number of worker processes (used in parallel mode).",
    )

    args = parser.parse_args()

    try:
        # Run the main function asynchronously with parsed arguments
        asyncio.run(
            main(
                args.pdf_file,
                args.markdown_output,
                args.image_output_folder,
                args.mode,
                args.max_workers,
            )
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
