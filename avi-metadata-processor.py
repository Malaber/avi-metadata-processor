import os
import mutagen
from mutagen.avi import AVIMetaData
from datetime import datetime
import argparse

# Set up command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true", help="Perform a dry run, printing the changes that would have been made but not actually writing them to the files")
parser.add_argument("--root-dir", required=True, help="The root directory to walk and process AVI files")
args = parser.parse_args()

# Set the date/time format to use when parsing the filenames
date_time_format = "%y-%m-%d_%H-%M.%S"

# Walk the directories and process the AVI files
for root, dirs, files in os.walk(args.root_dir):
    for filename in files:
        # Check if the file is an AVI file
        if filename.endswith(".avi"):
            # Open the AVI file and read its metadata
            avi_file = mutagen.open(os.path.join(root, filename))
            metadata = avi_file.tags

            # Split the filename into parts
            parts = filename.split(".")
            if len(parts) < 2:
                print(f"Failed to parse title and date/time from filename {filename}")
                continue

            # Set the title to the first part of the filename
            metadata["TITLE"] = parts[0]

            # Parse the date/time from the second part of the filename
            try:
                date_time = datetime.strptime(parts[1], date_time_format)
            except ValueError:
                print(f"Failed to parse date/time from filename {filename}")
                continue

            # Convert the datetime object to a string in the desired format
            date_time_str = datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S")

            # Set the date/time to the metadata
            metadata["DATE"] = date_time_str

            # Print the changes that would have been made or indicate that the changes will be written to the files
            if args.dry_run:
                print(f"Would have set title to '{metadata['TITLE']}' and date/time to '{metadata['DATE']}' for file {os.path.join(root, filename)}")
            else:
                print(f"Setting title to '{metadata['TITLE']}' and date/time to '{metadata['DATE']}' for file {os.path.join(root, filename)}")

            # Save the changes to the file (if not performing a dry run)
            if not args.dry_run:
                avi_file.save()
