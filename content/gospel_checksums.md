+++
layout = "page"
title = "Gospel Checksums"
date = "2024-10-23T18:27:42-07:00"
permalink = "/checksums/"
+++

## Quicklinks

- [Associated GitHub Issue](https://github.com/johnandersen777/johnandersen777.github.io/issues/1)

## TODOs

- [x] Game Plan
- [ ] Decode the Decoding Process
  - [ ] [Chuck Missler - How We Got Our Bible](https://www.youtube.com/watch?v=5ZsZLDWWZMs)
    - [x] Transcribe - Love is the essence of the Father
    - [ ] Notes
    - [ ] To specs
      - [ ] Basics
      - [ ] Simple Heptatic Structure
      - [ ] Resume at 2 hours in
      - [ ] Inter-Testament Heptadic Bridges
        - [ ] Occurences of words in Old and New added together should be divisable by 7
    - [ ] To workflows
    - [ ] Matrixies
- [ ] Languages Required
  - [ ] Vulgate
  - [ ] Greek
  - [ ] Hebrew
- [ ] Texts
  - [ ] [Wisdom the Goddess](http://thenazareneway.com/Wisdom%20the%20Goddess.htm)
  - [ ] [Essene Gospel Of Peace: Book Two](https://www.essene.com/GospelOfPeace/peace2.html)
  - [ ] [The Gospel of the Holy Twelve](http://gospelofholytwelve.blogspot.com/)
  - [ ] [Coptic Gospels](https://www.gospels.net)
  - [ ] [Gospels](https://www.gutenberg.org/cache/epub/10/pg10.txt)

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
```

### Notes

h adds the essence. enoch knew of the flood

### Specs

- [Decoding Biblical Texts: A Cryptographic Exploration](/decoding_biblical_texts_cryptographic_focus/)

## Languages Required

## Texts
