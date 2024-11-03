```bash
cat 24Hours.json | jq -r 'to_entries[] | .value'
python -m pip install -U --force-reinstall 'https://github.com/yt-dlp/yt-dlp/archive/refs/heads/master.zip#egg=yt-dlp'
for link in $(cat 24Hours.json | jq -r 'to_entries[] | .value'); do python -m yt_dlp --no-call-home --no-cache-dir -x --audio-format mp3 --add-metadata --audio-quality 0 --restrict-filenames --ignore-errors "${link}"; done
for file in $(echo Learn_the_Bible*); do mkdir -pv "${file}.transcribe/" && whisper --model large-v3 --output_format all --device cpu --output_dir "${file}.transcribe/" "${file}"; done
```
