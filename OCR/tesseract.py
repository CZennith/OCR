import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/potat/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

def getText(filename):
    text = pytesseract.image_to_string(filename)
    return text


