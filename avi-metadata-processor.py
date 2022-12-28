import os
import argparse
import pymediainfo

def set_metadata(file_path, date, title):
    # Open the AVI file using pymediainfo
    mi = pymediainfo.MediaInfo.parse(file_path)

    # Get the first track (there should only be one track in an AVI file)
    track = mi.tracks[0]

    # Set the title of the AVI file
    track.title = title

    # Set the date/time of the AVI file
    track.recorded_date = date

    # Save the modified metadata to the AVI file
    track.to_data()

def parse_filename(filename):
    # Split the filename into parts
    parts = filename.split('.')

    # The date/time is the first part of the filename
    date_time_str = parts[0]

    # The title is the second part of the filename
    title = parts[1]

    # Parse the date/time string
    date, time = date_time_str.split('_')
    year, month, day = date.split('-')
    hour, minute, second = time.split('-')

    # Format the date/time as an ISO 8601 string
    date_time = f"{year}-{month}-{day}T{hour}:{minute}:{second}Z"

    return date_time, title

def process_files(root_dir, dry_run):
    # Walk the directories and process the AVI files
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.avi'):
                file_path = os.path.join(root, file)

                # Parse the filename to get the date/time and title
                date, title = parse_filename(file)

                if dry_run:
                    # In dry run mode, print the actions that would be taken
                    print(f"Would have set the date/time of {file_path} to {date} and the title to {title}")
                else:
                    # Set the metadata of the AVI file
                    set_metadata(file_path, date, title)
                    print(f"Set the date/time of {file_path} to {date} and the title to {title}")

if __name__ == '__main__':
    # Parse the command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--root-dir', required=True, help='Root directory to search for AVI files')
    parser.add_argument('--dry-run', action='store_true', help='Enable dry run mode')
    args = parser.parse_args()

    # Process the AVI files
    process_files(args.root_dir, args.dry_run)
