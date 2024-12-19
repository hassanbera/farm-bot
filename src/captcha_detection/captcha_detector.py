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


def solve_captcha(bbox=(804,472,1113,604)):
    """
    Solves the CAPTCHA by reading and solving the math problem.
    """
    screenshot = ImageGrab.grab(bbox=bbox)
    captcha_text = pytesseract.image_to_string(screenshot)

    # Extract math problem
    match = re.search(r"(\d+)\s+plus\s+(\d+)|(\d+)\s+multiple\s+(\d+)", captcha_text.lower())
    if match:
        if "plus" in captcha_text.lower():
            num1, num2 = map(int, match.groups()[:2])
            return num1 + num2
        elif "multiple" in captcha_text.lower():
            num1, num2 = map(int, match.groups()[2:])
            return num1 * num2
    print(f"CAPTCHA not recognized: {captcha_text.strip()}")
    return None

def handle_captcha(bbox=(804,472,1113,604), click_coords=(960, 640)):
    """
    Detects, solves, and handles the CAPTCHA popup.
    """
    if detect_captcha(bbox=bbox):
        print("CAPTCHA detected!")
        answer = solve_captcha(bbox=bbox)
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
    draw.rectangle(bbox, outline="red", width=3)
    screenshot.show()
    print(f"Visualized bbox: {bbox}")
    print(f"Captured region size: width={bbox[2]-bbox[0]}, height={bbox[3]-bbox[1]}")

