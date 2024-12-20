from PIL import ImageGrab, ImageDraw
import pytesseract
import re
import time
from input_handling.input_handler import hold_key, mouse_move_and_click

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_captcha(bbox=(804, 472, 1113, 604), pixel_check=(850, 500), target_color=(255, 255, 255)):
    """
    Detects if a CAPTCHA is visible by checking a pixel or region.
    """
    # Capture the region of interest
    screenshot = ImageGrab.grab(bbox=bbox)

    # Ensure pixel_check is within the bbox bounds
    if not (bbox[0] <= pixel_check[0] < bbox[2] and bbox[1] <= pixel_check[1] < bbox[3]):
        raise ValueError(f"pixel_check {pixel_check} is out of bounds for bbox {bbox}")

    # Adjust pixel_check to be relative to the bbox
    adjusted_pixel = (pixel_check[0] - bbox[0], pixel_check[1] - bbox[1])

    # Get the color of the pixel
    pixel_color = screenshot.getpixel(adjusted_pixel)
    return pixel_color == target_color



def solve_captcha(captcha_text):
    """
    Solves a math CAPTCHA by detecting and calculating the operation.
    Supports: plus, multiple, minus, divide.
    Args:
        captcha_text (str): The text extracted from the CAPTCHA.
    Returns:
        float or None: The result of the calculation, or None if not recognized.
    """
    
    # Extract math problem using regex
    match = re.search(
        r"(\d+)\s+plus\s+(\d+)|(\d+)\s+multiple\s+(\d+)|(\d+)\s+minus\s+(\d+)|(\d+)\s+divide\s+(\d+)",
        captcha_text.lower()
    )

    if match:
        if "plus" in captcha_text.lower():
            # Extract numbers for addition
            num1, num2 = map(int, match.groups()[:2])
            return num1 + num2
        elif "multiple" in captcha_text.lower():
            # Extract numbers for multiplication
            num1, num2 = map(int, match.groups()[2:4])
            return num1 * num2
        elif "minus" in captcha_text.lower():
            # Extract numbers for subtraction
            num1, num2 = map(int, match.groups()[4:6])
            return num1 - num2
        elif "divide" in captcha_text.lower():
            # Extract numbers for division
            num1, num2 = map(int, match.groups()[6:8])
            if num2 != 0:  # Check for division by zero
                return num1 / num2
            else:
                print("Error: Division by zero!")
                return None

    # If no match found, log and return None
    print(f"CAPTCHA not recognized: {captcha_text.strip()}")
    return None


def handle_captcha(bbox=(804,472,1113,604), click_coords=(960, 640)):
    """
    Detects, solves, and handles the CAPTCHA popup.
    """
    if detect_captcha(bbox=bbox):
        print("CAPTCHA detected!")
        captcha_text = pytesseract.image_to_string(ImageGrab.grab(bbox=bbox))
        answer = solve_captcha(captcha_text)
        if answer is not None:
            for char in str(answer):
                hold_key(char, 0.1)  # Adjust if `char` isn't directly mappable
            time.sleep(0.5)
            mouse_move_and_click(*click_coords)
            print("CAPTCHA solved and handled successfully.")
        else:
            print("Failed to solve CAPTCHA.")

def visualize_bbox(bbox):
    """
    Visualize the bounding box area to confirm its position.
    """
    screenshot = ImageGrab.grab()
    draw = ImageDraw.Draw(screenshot)
    draw.rectangle(bbox, outline="blue", width=3)
    screenshot.show()
    print(f"Visualized bbox: {bbox}")
    print(f"Captured region size: width={bbox[2]-bbox[0]}, height={bbox[3]-bbox[1]}")

