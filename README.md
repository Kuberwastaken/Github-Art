![Github-Art Banner](https://github.com/user-attachments/assets/e4783d50-b9c4-4431-8d71-e6f8caf9a399)

# Github-Art

Create Pixel Art in your GitHub Commit History using a simple Python Script.

## Overview

### Why Does this Project Exist
Short answer, because it's a fun idea. In a world where your technological capability as a developer is measured by how green your contribution chart is, adding a custom flair to it just seems like a fun idea.

I saw the contribution chart as a 52 x 7 canvas to show art on, this unlocks unlimited possibilities

### How Does It Work

This project allows you to generate pixel art in your GitHub commit history. By converting an image into a pattern of commits, you can create a visual representation directly on your GitHub profile.

## Usage

1. **Fork this Repository**: 

     Fork this repository to your GitHub account. 

2. **Clone the Repository**: 

     Clone the forked repository to your local machine: 
     ```
     bash git clone https://github.com/yourusername/Github-Art.git
     ```

3. **Create Your Pixel Art**:

    Your image should be in black and white, with whites representing commits and sized to 7x52 pixels to fit the commit history display on GitHub.

    You can use any tool to create your pixel art. I used [Pixilart](https://www.pixilart.com/) for this purpose.

    Place your image in the same directory as generate_commits.py and ensure the filename matches the one used in the script.

2. **Run the Script**:
   - Install the required Python package (Pillow):
     ```bash
     pip install pillow
     ```
   - Execute the script to generate commits:
     ```bash
     python generate_commits.py
     ```

3. **Push Your Commits**:
   - Once the script has created the commits, push them to your repository:
     ```bash
     git push origin main
     ```

Your GitHub profile will now display your pixel art in the commit history!

## Requirements

- Python 3.x
- Pillow library

## Disclaimer
This script is intended for educational and experimental purposes only. Misuse of this script to violate GitHub’s Terms of Service, such as artificially inflating commit activity or creating spam, is not recommended or endorsed. Please use this tool responsibly and ethically, respecting GitHub’s guidelines and the integrity of the platform.

## License

This project is licensed under the Apache-2.0 license License. See the [LICENSE](LICENSE) file for details.
