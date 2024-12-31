from PIL import Image
import os
import subprocess
from datetime import datetime, timedelta

# Path to your 7x52 image
image_path = "pixel_art.png"  # Ensure the name matches exactly

# Define the filename to modify with each commit
FILENAME = "art.txt"

# Starting date for the commit pattern (January 1, 2023)
start_date = datetime(2023, 1, 1)

# Create the file if it doesn’t exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("GitHub Art\n")

# Load the image and convert to a commit pattern
img = Image.open(image_path).convert("L")  # Convert to grayscale
img = img.resize((52, 7))  # Resize to ensure it's 7x52

# Create a pattern array where each pixel represents a commit day
pattern = []
for y in range(7):
    row = []
    for x in range(52):
        pixel = img.getpixel((x, y))
        # If pixel is dark (black), we make a commit (threshold at 128)
        if isinstance(pixel, int):  # Check if pixel is already in grayscale
            row.append(1 if pixel < 128 else 0)
        else:
            # If it's an RGB tuple, we take the first value (grayscale conversion)
            row.append(1 if pixel[0] < 128 else 0)
        print(f"Pixel at ({x}, {y}): {pixel}")  # Print pixel values for debugging
    pattern.append(row)

# Function to make a commit
def make_commit(date):
    with open(FILENAME, "a") as f:
        f.write(f"Commit on {date}\n")
    commit_date = date.strftime("%Y-%m-%dT%H:%M:%S")
    subprocess.run(["git", "add", FILENAME])
    subprocess.run(["git", "commit", "--date", commit_date, "-m", f"Commit on {date}"])

# Generate commits based on the pattern
current_date = start_date
for row in pattern:
    for cell in row:
        if cell == 1:  # "1" means a commit should be made
            make_commit(current_date)
        # Move to the next day
        current_date += timedelta(days=1)
    # Skip to the start of the next week (7 days)
    current_date += timedelta(days=7 - len(row))
