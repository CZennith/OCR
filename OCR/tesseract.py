import pytesseract
import shutil

tess_path = shutil.which("tesseract")
if tess_path:
    pytesseract.pytesseract.tesseract_cmd = tess_path
else: 
    raise Exception("Tesseract OCR not installed into path. Please install it and try again.")


def getText(filename):
    text = pytesseract.image_to_string(filename)
    return text


