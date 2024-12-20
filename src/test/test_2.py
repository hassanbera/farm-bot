from PIL import ImageGrab, ImageDraw
from captcha_detection.captcha_detector import detect_captcha, visualize_bbox
 # Import your detection and visualization functions

# Define the bounding box area to test
bbox = (804,472,1113,604)  # Adjust coordinates based on your game screen

# Step 1: Visualize the bounding box
visualize_bbox(bbox)  # This will open an image showing the bbox area

# Step 2: Test CAPTCHA detection
is_detected = detect_captcha(bbox=bbox, pixel_check=(850, 500), target_color=(255, 255, 255))  # Adjust pixel_check and target_color if needed
if is_detected:
    print("CAPTCHA detected in the specified area!")
else:
    print("CAPTCHA not detected. Adjust the bbox or parameters.")


from PIL import ImageGrab

def get_pixel_color(bbox, pixel_check):
    """
    Capture the screen and get the color of a specific pixel.
    Args:
        bbox: The bounding box area to capture (x1, y1, x2, y2).
        pixel_check: The pixel inside the bbox to inspect (x, y).
    Returns:
        The RGB color of the pixel.
    """
    # Capture the screen area defined by bbox
    screenshot = ImageGrab.grab(bbox=bbox)

    # Adjust pixel_check to be relative to bbox
    relative_pixel = (pixel_check[0] - bbox[0], pixel_check[1] - bbox[1])

    # Get the color of the pixel
    pixel_color = screenshot.getpixel(relative_pixel)
    return pixel_color

# Example usage
bbox = (804, 472, 1113, 604)  # Define your CAPTCHA message box area
pixel_check = (850, 500)  # The pixel you want to check inside the bbox

color = get_pixel_color(bbox, pixel_check)
print(f"The color of the pixel at {pixel_check} is: {color}")
