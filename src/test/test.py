from PIL import Image
import pytesseract

# Test with a sample image
text = pytesseract.image_to_string(Image.open("test.jpeg"))
print(text)
