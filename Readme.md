# AVI Metadata processor

I recently ripped an old camcorder (Sony DCR-TRV145E PAL) of my uncle.
I wanted the files to include the correct dates which the ripping software kindly wrote into the filenames, but not into the metadata.
Obviously only a mad person would write code himself in 2022, so I turned to ChatGPT.
This project has no file (other than this part of the readme) written by me. All code is only copied from ChatGPT.

Okay.. Lets see if ChatGPT can write a summary of what it does.

`Malaber left the game.`

# avi-metadata-processor

A tool for processing the metadata of AVI files, including setting the date and title from the filename.

## Features

- Set the date/time of an AVI file from the filename
- Set the title of an AVI file from the filename
- Option to enable a dry run mode, where the script will only print the actions it would have taken, without modifying any files

## Installation

Install the dependencies for the `avi-metadata-processor` project using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

Run the `avi-metadata-processor` script using Poetry:

```bash
poetry run python avi-metadata-processor.py --root-dir /path/to/avi/files --dry-run
```

The `--root-dir` argument specifies the root directory to search for AVI files, and the `--dry-run` flag enables the dry run mode.

## Credits

- This project was created using the [OpenAI GPT-3](https://openai.com/blog/openai-api-now-includes-gpt-3/) language model.
