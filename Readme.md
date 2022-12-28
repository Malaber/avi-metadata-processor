# AVI Metadata processor

I recently ripped an old camcorder (Sony DCR-TRV145E PAL) of my uncle.
I wanted the files to include the correct dates which the ripping software kindly wrote into the filenames, but not into the metadata.
Obviously only a mad person would write code himself in 2022, so I turned to ChatGPT.
This project has no file (other than this part of the readme) written by me. All code is only copied from ChatGPT.

Okay.. Lets see if ChatGPT can write a summary of what it does.

`Malaber left the game.`

# avi-metadata-processor

A command line utility for editing the metadata of AVI files.

## Features

- Walk directories and process all AVI files found
- Set the title field in the metadata to the first part of the filename
- Parse the date/time from the second part of the filename and set it in the metadata
- Perform a dry run to preview the changes that would have been made, without actually writing to the files

## Usage

```usage: avi-metadata.py [-h] [--dry-run] --root-dir ROOT_DIR

A command line utility for editing the metadata of AVI files.

optional arguments:
-h, --help            show this help message and exit
--dry-run             Perform a dry run, printing the changes that would have been made but not actually writing them to
```

## Installation

This project requires Python 3.7 or higher. To install the dependencies using Poetry, run the following command:

```poetry install```

## Examples

Process all AVI files in the current directory and write the changes to the files:

```python avi-metadata.py --root-dir .```

Perform a dry run to preview the changes that would have been made, without actually writing to the files:

```python avi-metadata.py --dry-run --root-dir .```

## Credits

This project was developed by [Assistant](https://openai.com/blog/introducing-assistant/), a large language model developed by OpenAI.

I hope this helps! Let me know if you have any further questions.
