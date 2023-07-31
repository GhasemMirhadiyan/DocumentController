from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

import PyPDF2
from io import BytesIO
from PIL import Image
import sys
import pyocr
import pyocr.builders
import codecs
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


def ReadFile(t):
    text = t
    pdfRead = PyPDF2.PdfFileReader(text)
    for i in range(pdfRead.getNumPages()):
        page = pdfRead.getPage(i)
        pageContent = page.extract_text()
        plaintext = text + str(pageContent)
        print("\n\n\nText:", plaintext)
        return plaintext


def ocrGithub(file):
    print("\nFilename:", file)
    pages = None
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = BytesIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(file, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    print(text)

    # write to .txt
    text_file = open("output.txt", "w")
    text = re.sub("\s\s+", " ", text.decode('utf8'))
    text_file.write("%s" % text)
    text_file.close()


def newgithub():
    tool = pyocr.get_available_tools()[0]
    builder = pyocr.builders.TextBuilder()

    txt = tool.image_to_string(
        Image.open(r'E:\Project\s\Scan - SP13-P0-EL-DW-7233-Rev. 04.pdf'),
        lang="eng",
        builder=builder
    )
    # txt is a Python string

    with codecs.open("toto.txt", 'w', encoding='utf-8') as file_descriptor:
        builder.write_file(file_descriptor, txt)
    # toto.txt is a simple text file, encoded in utf-8


def ocr(PDFFile):
    if platform.system() == "Windows":
        # Windows needs a PyTesseract Download
        # https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine

        pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")

        # Windows also needs poppler_exe
        path_to_poppler_exe = Path(r"C:\Path\poppler-23.07.0\Library\bin")

        # Put our output files in a sane place...
        out_directory = Path(r"E:\Project\output").expanduser()
    else:
        out_directory = Path(r"E:\Project\output").expanduser()

    # Path of the Input pdf
    PDF_file = PDFFile
    # PDF_file = Path(r"E:\Project\test\Scan - SP13-P0-EL-DW-7233-Rev. 04.pdf")

    # Store all the pages of the PDF in a variable
    image_file_list = []
    outlogdirectory = r'E:\Project\Result'

    text_file = outlogdirectory / Path(f'{PDF_file}.txt')

    with TemporaryDirectory() as tempdir:
        # Create a temporary directory to hold our temporary images.

        """
        Part #1 : Converting PDF to images
        """

        if platform.system() == "Windows":
            pdf_pages = convert_from_path(PDF_file, 600, poppler_path=path_to_poppler_exe)
        else:
            pdf_pages = convert_from_path(PDF_file, 600)
        # Read in the PDF file at 500 DPI

        # Iterate through all the pages stored above
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            # enumerate() "counts" the pages for us.

            # Create a file name to store the image
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"

            # Declaring filename for each page of PDF as JPG
            # For each page, filename will be:
            # PDF page 1 -> page_001.jpg
            # PDF page 2 -> page_002.jpg
            # PDF page 3 -> page_003.jpg
            # ....
            # PDF page n -> page_00n.jpg

            # Save the image of the page in system
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        """
        Part #2 - Recognizing text from the images using OCR
        """

        with open(text_file, "a") as output_file:
            # Open the file in append mode so that
            # All contents of all images are added to the same file

            # Iterate from 1 to total number of pages
            for image_file in image_file_list:
                # Set filename to recognize text from
                # Again, these files will be:
                # page_1.jpg
                # page_2.jpg
                # ....
                # page_n.jpg

                # Recognize the text as string in image using pytesserct
                text = str(((pytesseract.image_to_string(Image.open(image_file)))))

                # The recognized text is stored in variable text
                # Any string processing may be applied on text
                # Here, basic formatting has been done:
                # In many PDFs, at line ending, if a word can't
                # be written fully, a 'hyphen' is added.
                # The rest of the word is written in the next line
                # Eg: This is a sample text this word here GeeksF-
                # orGeeks is half on first line, remaining on next.
                # To remove this, we replace every '-\n' to ''.
                text = text.replace("-\n", "")
                return text

                # Finally, write the processed text to the file.
                output_file.write(text)

            # At the end of the with . output_file block
            # the file is closed after writing all the text.
        # At the end of the with .. tempdir block, the
        # TemporaryDirectory() we're using gets removed!
    # End of function!
