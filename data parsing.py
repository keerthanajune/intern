from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
img = Image.open("receipt.png")
text = pytesseract.image_to_string(img)
print(text)
