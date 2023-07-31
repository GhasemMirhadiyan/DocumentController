from PIL import Image as img
import pytesseract as PT
import sys
from pdf2image import convert_from_path as CFP
import os


def ocrTest():
    # Importing the pdf file
    PDF_file_1 = "E:\Project\x\SP13-P0-IN-DW-3233-REV 2.pdf"
    pages_1 = CFP(PDF_file1, 9)

    # Now, we will create a counter for storing images of each page of PDF to image
    image_counter1 = 1

    # Iterating through all the pages of the pdf file stored above
    for page in pages_1:
        # We will Declare the  filename for each page of PDF file as JPG file
        # For each page, the filename will be:
        # PDF page no. 1: Page_no_1.jpg
        # PDF page no.2: Page_no_2.jpg
        # PDF page no. 3: Page_no_3.jpg
        # PDF page no. 4: Page_no_4.jpg
        # .... and so on..
        # PDF page n: page_n.jpg
        filename1 = "Page_no_" + str(image_counter) + " .jpg"

        # Now, we will save the image of the page in system
        page.save(filename1, 'JPEG')

        # Then, we will increase the counter for updating filenames
        image_counter1 = image_counter1 + 1

    '''  
    Part #2 - Recognize the text content from the image files by using OCR  
    '''
    # Variable for getting the count of the total number of pages
    filelimit1 = image_counter1 - 1

    # then, we will create a text file for writing the output
    out_file1 = "output_text.txt"

    # Now, we will open the output file in append mode so that all contents of the # images will be added in the same output file.
    f_1 = open(out_file1, "a")

    # Iterating from 1 to total number of pages
    for K in range(1, filelimit1 + 1):
        # Now, we will set filename for recognizing text from images
        # Again, these files will be:
        # Page_no_1.jpg
        # Page_no_2.jpg
        # Page_no_3.jpg
        # ....
        # page_no_n.jpg
        filename1 = "Page_no_" + str(K) + " .jpg"

        # Here, we will write a code for recognizing the text as a string variable in an image file by using the pytesserct module
        text1 = str(((PT.image_to_string(Image.open(filename1)))))

        # : The recognized text will be stored in variable text
        # : Any string variable processing may be applied to text content
        # : Here, basic formatting will be done:-

        text1 = text1.replace('-\n', '')

        # At last, we will write the processed text into the file.
        f_1.write(text1)

    # Closing the file after writing all the text content.
    f_1.close()