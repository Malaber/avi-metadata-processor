import argparse
import os
import re
from datetime import datetime

import mutagen

def process_metadata(root_dir, dry_run=False):
    # Walk through all the files in the root directory and its subdirectories
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            # Check if the file is an AVI file
            if not filename.endswith(".avi"):
                continue

            # Extract the date and time information from the filename
            match = re.search(r"(\d{2})-(\d{2})-(\d{2})_(\d{2})-(\d{2}).\d{2}", filename)
            if match is None:
                continue

            # Parse the date and time using the datetime module
            year, month, day, hour, minute = map(int, match.groups())
            record_date = datetime(year + 2000, month, day, hour, minute)

            # Extract the title from the filename
            title = filename.split(".")[1]

            # Set the date/time and title to the metadata
            filepath = os.path.join(root, filename)
            audio = mutagen.AVI(filepath)
            audio["date"] = record_date.strftime("%Y-%m-%d %H:%M:%S")
            audio["title"] = title

            # Save the changes to the file
            if dry_run:
                print(f"Would have set date/time to {record_date} and title to {title} for {filepath}")
            else:
                audio.save()
                print(f"Set date/time to {record_date} and title to {title} for {filepath}")

def main():
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("root_dir", help="the root directory to search for AVI files")
    parser.add_argument("--dry-run", action="store_true", help="perform a dry run, printing the changes that would be made but not actually modifying the files")
    args = parser.parse_args()

    # Process the metadata of the AVI files
    process_metadata(args.root_dir, args.dry_run)

if __name__ == "__main__":
    main()
