import os
import shutil
import time
import concurrent.futures
import imghdr
import logging
import datetime
from PIL import Image
from PIL.ExifTags import TAGS
from tqdm import tqdm
from tqdm.auto import tqdm

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Define constants
PHOTO_DIR = 'D:/Photos42024/' # Source folder of your images
PARENT_DIR = 'D:/Programming/Python/Project/Organized Photos/' # Destination folder
BATCH_SIZE = 10 # Number of photos to process per thread batch
DELAY = 1 # Not used currently, reserved for future throttling

# Define helper functions
def get_photo_files():
    """Get a list of photo files in the photo directory."""
    photo_files = []
    for root, _, files in os.walk(PHOTO_DIR):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                photo_files.append(os.path.join(root, file))
    return photo_files

def get_date_from_exif(photo_file):
    """Get the date from the EXIF data of a photo file."""
    try:
        image = Image.open(photo_file)
    except Exception as e:
        logging.error(f'Error opening {photo_file}: {e}')
        return None

    try:
        exif_data = image._getexif()
    except Exception as e:
        logging.error(f'Error getting EXIF data from {photo_file}: {e}')
        return None

    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == 'DateTimeOriginal':
            date_time = value.split()
            date = date_time[0]
            return datetime.datetime.strptime(date, '%Y:%m:%d')

    logging.warning(f'Capture date not found in {photo_file}')
    return None

def move_photo_to_parent_dir(photo_file, date):
    """Move a photo file to the parent directory based on its date."""
    new_dir = os.path.join(PARENT_DIR, date.strftime('%Y-%m-%d'))
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    shutil.move(photo_file, new_dir)

# Define main function
def main():
    # Get a list of photo files
    photo_files = get_photo_files()

    # Set up tqdm progress bar
    progress_bar = tqdm(total=len(photo_files), desc='Processing photos', position=0)

    # Process photos in batches
    for i in range(0, len(photo_files), BATCH_SIZE):
        batch_photo_files = photo_files[i:i+BATCH_SIZE]

        # Set up thread pool
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(get_date_from_exif, photo_file): photo_file for photo_file in batch_photo_files}

            # Get the date for each photo file in the batch
            for future in concurrent.futures.as_completed(futures):
                date = future.result()
                if date is not None:
                    move_photo_to_parent_dir(futures[future], date)

        # Update the progress bar
        progress_bar.update(len(batch_photo_files))

    # Close the progress bar
    progress_bar.close()

# Define custom tqdm progress bar
class CustomProgressBar(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Run the main function
if __name__ == '__main__':
    main()
    
