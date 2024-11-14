# Etsy Alt Text Generator

## Description
This script generates SEO-friendly alt text for Etsy images using a pre-trained image captioning model. The generated alt text is optimized to be concise (within 250 characters) and descriptive to improve Etsy search visibility.

## Prerequisites
### Python Version
- **Python 3.11.x** is required for this project.
  - PyTorch currently supports up to Python 3.11 as of November 2024.
  - This script is **not compatible** with Python 3.12 or higher.

### Required Tools
- **Python 3.11**: [Download Python](https://www.python.org/downloads/release/python-3110/)
- **Git**: [Download Git](https://git-scm.com/)
- **Homebrew** (macOS users): [Install Homebrew](https://brew.sh/)

## Installation Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/rileylemm/etsy-alt-text-generator.git
   cd etsy-alt-text-generator
   ```

2. Create a virtual environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scriptsctivate   # On Windows
   ```

3. Install the required packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

1. Place your images in the `images/` folder (ensure they are in .jpg, .jpeg, or .png format).
2. Run the script:
   ```bash
   python generate_alt_text.py
   ```
3. Check the `output/` folder for generated alt text files saved as .txt.

## Notes
- The generated alt text is saved as a .txt file for each image in the output folder.
- The descriptions are optimized for Etsy and will not exceed 250 characters.
- The first run may take some time as the model files are downloaded.

## Troubleshooting
- **Python Version Issues**: Ensure you're using Python 3.11.x. The script is not compatible with Python 3.12 or higher.
- **Model Download**: The script may take a few minutes to download the necessary model files on first run.
- **Virtual Environment**: If you encounter issues, try recreating the virtual environment with the correct Python version.

## License
This project is open-source and free to use.

