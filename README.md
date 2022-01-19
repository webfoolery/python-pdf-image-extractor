# PDF Image Extractor

It's a short Python script to parse PDF files & export the images found inside in their original formats.

## Setup

1. Clone the repo
2. Create the virtual environment - `python3 -m venv env`
2. Start the virtual environment, ie: `. env/Scripts/activate` (or whatever your system needs to do so)
3. `pip install -r ./requirements.txt`
4. End the virtual environment, ie: `deactivate`

## Usage
1. Place a PDF file in the same directory as the script
2. 
    * Linux: Run`_pdf-image.py`
    *  Windows: As above or run `_get-pdf-image.bat`
3. Check in the same directory to find the image/s. Files are names based upon the original file with page number, image number & file type appended