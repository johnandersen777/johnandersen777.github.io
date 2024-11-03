+++
layout = "page"
title = "Root of Trust Weighting: Checksum Validation"
date = "2024-10-23T18:27:42-07:00"
permalink = "/checksums/"
+++

> I ❤️ Heresy because I ❤️ Truth
>
> More God more better, Good thing there's always more God
>
> "Every Good Man is Free" [Philo]

## Quicklinks

- [Associated Discussion Thread](https://github.com/johnandersen777/johnandersen777.github.io/discussions/3)
- [Towards a Generic Methodology for Sandbox Escape: Part 33: Mary’s Role in Defending Our Secure Software Forge: 🍎🐍🌳](/gse33/)

## TODOs

- ✅ Game Plan
- ⏳ Decode the Decoding Process
  - ⏳ [Essene Version of Genesis 1:1](https://www.thenazareneway.com/Essene%20Version%20of%20Genesis%201%201.htm)
  - ⏳ David Flynn
  - ⏳ Newton
  - ⏳ https://essenenazarene.com/page/2/
    - > Thomas Paine and Thomas Jefferson can be aptly labeled “Christian Heretics.” They admired and praised “Jesus” but rejected Orthodox Christian doctrines. Paine wrote, “I do not believe in the creed professed by the Jewish church, by the Protestant church, nor by any church that I know of.” Regarding the bible, he mused, “…it would be more consistent that we call it the word of a demon than the word of God.”
      - Judas 47-56
      - [`bcb131db679822c84ac4398e41594a81763bc478`](https://github.com/johnandersen777/johnandersen777.github.io/commit/bcb131db679822c84ac4398e41594a81763bc478)
  - ⏳ https://en.wikipedia.org/wiki/Philo
    - Is this why the library was burned?
    - > Philo's deployment of allegory to harmonize Jewish scripture, mainly the Torah, with Greek philosophy was the first documented of its kind, and thereby often misunderstood. Many critics of Philo assumed his allegorical perspective would lend credibility to the notion of legend over historicity.[4] Philo often advocated a literal understanding of the Torah and the historicity of such described events, while at other times favoring allegorical readings.[5]
      - [Whaaaat](https://johnandersen777.github.io/the_new_covenants_path_to_the_nameless_divine/), my man Philo right here whooooop whooooop
  - ⏳ [Chuck Missler - How We Got Our Bible](https://www.youtube.com/watch?v=5ZsZLDWWZMs)
    - ✅ Transcribe
    - ⏳ Notes
    - ⏳ To specs
      - ⏳ Basics
      - ⏳ Simple Heptatic Structure
      - ⏳ Resume at 2 hours in
      - ⏳ Inter-Testament Heptadic Bridges
        - ⏳ Occurences of words in Old and New added together should be divisable by 7
    - ⏳ To workflows
    - ⏳ Matrixies
- ⏳ Languages Required
  - ⏳ Greek
  - ⏳ Hebrew
  - ❔ Vulgate
- ⏳ Validation Runs
  - ⏳ [Wisdom the Goddess](http://thenazareneway.com/Wisdom%20the%20Goddess.htm)
  - ⏳ [Essene Gospel Of Peace: Book Two](https://www.essene.com/GospelOfPeace/peace2.html)
  - ⏳ [Daughter of Goddess the Mother](http://www.thenazareneway.com/Jewish%20Coverts%20and%20the%20Virgin%20Birth.htm)
  - ⏳ [The Gospel of the Holy Twelve](http://gospelofholytwelve.blogspot.com/)
  - ⏳ [Coptic Gospels](https://www.gospels.net)
  - ⏳ [Gospels](https://www.gutenberg.org/cache/epub/10/pg10.txt)
- ⏳ Recursivity Analysis (cycles)

## Game Plan

For those gospels that checksum correctly weight at 100 for patterns to follow.
For those that do not checksum but align to the checksum training we weight positively.

For those that do not we know that's the work of deception. Weight those high for anti-pattern avoidance stuff at 100.

Other texts from non biblical sources we can assess and add to training data and weight sources on generations appropriately.

Use concept mapping stuff sent to analyze other texts.

## Decode the Decoding Process

```bash
python -m pip install --upgrade --force-reinstall git+https://github.com/openai/whisper.git
python -m pip install -U --force-reinstall 'https://github.com/yt-dlp/yt-dlp/archive/refs/heads/master.zip#egg=yt-dlp'

python -m yt_dlp --no-call-home --no-cache-dir -x --audio-format mp3 --add-metadata --audio-quality 0 --restrict-filenames --ignore-errors 'https://www.youtube.com/watch?v=5ZsZLDWWZMs'

for link in $(cat static/missler/24Hours.json | jq -r 'to_entries[] | .value'); do python -m yt_dlp --no-call-home --no-cache-dir -x --audio-format mp3 --add-metadata --audio-quality 0 --restrict-filenames --ignore-errors "${link}"; done
for file in $(echo Learn_the_Bible*); do mkdir -pv "${file}.transcribe/" && whisper --model large-v3 --output_format all --device cpu --output_dir "${file}.transcribe/" "${file}"; done
```

### Notes

- h adds the essence
- enoch knew of the flood
- Love is the essence of the Father

### Specs

- [Decoding Biblical Texts: A Cryptographic Exploration](/decoding_biblical_texts_cryptographic_focus/)

### Code

- [scripts/pdf_to_markdown.py](https://github.com/johnandersen777/johnandersen777.github.io/blob/9e2a704d985ce30fcba4725e86235557ff52fe39/scripts/pdf_to_markdown.py)

```bash
python -u scripts/pdf_to_markdown.py ~/Downloads/THE\ ADAM\ AND\ EVE\ STORY\[15646345].pdf ~/Downloads/THE\ ADAM\ AND\ EVE\ STORY\[15646345].md $(mktemp -d)
python -u scripts/pdf_to_markdown.py ~/Downloads/Cosmic_Codes_eBook.pdf ~/Downloads/Cosmic_Codes_eBook.md $(mktemp -d) --max-workers $(nproc)
```

## Languages Required

TODO

## Validation Runs

TODO - link to workflow runs
