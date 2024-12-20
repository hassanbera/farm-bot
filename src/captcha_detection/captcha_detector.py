from PIL import ImageGrab, ImageDraw, ImageOps, ImageEnhance
import pytesseract
import re
import time
from input_handling.input_handler import hold_key, mouse_move_and_click

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image, method="threshold"):
    grayscale_image = ImageOps.grayscale(image)
    if method == "threshold":
        return grayscale_image.point(lambda x: 0 if x < 128 else 255, '1')  # Binarization
    elif method == "contrast":
        enhancer = ImageEnhance.Contrast(grayscale_image)
        return enhancer.enhance(3.0)  # Increase contrast


def image_show(image):
        threshold_image = preprocess_image(image, method="threshold")
        contrast_image = preprocess_image(image, method="contrast")
        threshold_image.save("threshold_output.png")
        contrast_image.save("contrast_output.png")

def detect_captcha(bbox=(804, 472, 1113, 604), pixel_check=(908, 586), target_color=(41, 24, 16)):
    """
    Detects if a CAPTCHA is visible by checking a specific pixel for the target color.
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
            num1, num2 = map(int, match.groups()[:2])
            print(num1+num2)
            return num1 + num2
        elif "multiple" in captcha_text.lower():
            num1, num2 = map(int, match.groups()[2:4])
            print(num1*num2)
            return num1 * num2
        elif "minus" in captcha_text.lower():
            num1, num2 = map(int, match.groups()[4:6])
            print(num1-num2)
            return num1 - num2
        elif "divide" in captcha_text.lower():
            num1, num2 = map(int, match.groups()[6:8])
            if num2 != 0:  # Check for division by zero
                print(num1/num2)
                return num1 / num2
            else:
                print("Error: Division by zero!")
                return None

    print(f"CAPTCHA not recognized: {captcha_text.strip()}")
    return None


def handle_captcha(bbox=(804, 472, 1113, 604), click_coords=(891, 584)):
    """
    Detects, solves, and handles the CAPTCHA popup.
    """
    if detect_captcha(bbox=bbox):
        print("CAPTCHA detected!")
        screenshot = ImageGrab.grab(bbox=bbox)
        processed_image = preprocess_image(screenshot)
        captcha_text = pytesseract.image_to_string(processed_image, config="--psm 6")  
        print(f"Extracted CAPTCHA text: '{captcha_text.strip()}' (length: {len(captcha_text.strip())})")

        if captcha_text.strip():  # Check if text is non-empty
            answer = solve_captcha(captcha_text)
            if answer is not None:
                print(f"Answer to be typed: '{answer}'")
                # Use the SCANCODES dictionary to get the hex keycodes
                SCANCODES = {
                    '0': 0x0B, '1': 0x02, '2': 0x03, '3': 0x04, '4': 0x05,
                    '5': 0x06, '6': 0x07, '7': 0x08, '8': 0x09, '9': 0x0A,
                }

                # Convert the answer to scancodes
                try:
                    hex_keycodes = [SCANCODES[char] for char in str(answer)]
                    print(f"Generated hex keycodes: {hex_keycodes}")

                    for keycode in hex_keycodes:
                        print(f"Sending keycode: {keycode}")
                        hold_key(keycode, 0.1)  # Simulate key press
                    time.sleep(0.5)
                    mouse_move_and_click(*click_coords)
                    print("CAPTCHA solved and handled successfully.")
                except KeyError as e:
                    print(f"Error: Unrecognized character '{e}' in the answer.")
            else:
                print("Failed to solve CAPTCHA.")
        else:
            print("Extracted CAPTCHA text is empty. Failed to solve CAPTCHA.")




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
