from PIL import Image
import pytesseract

# Path to the Tesseract-OCR executable
# Only needed for Windows. For Raspberry Pi, it is usually not required to specify this.
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def read_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = 'body_test.jpg'  # Replace with the path to your image
    extracted_text = read_text_from_image(image_path)
    print("Extracted Text:\n", extracted_text)