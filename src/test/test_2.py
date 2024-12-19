from PIL import ImageGrab, ImageDraw
from functions.utils import detect_captcha,visualize_bbox  # Import your detection and visualization functions

# Define the bounding box area to test
bbox = (804,472,1113,604)  # Adjust coordinates based on your game screen

# Step 1: Visualize the bounding box
visualize_bbox(bbox)  # This will open an image showing the bbox area

# Step 2: Test CAPTCHA detection
is_detected = detect_captcha(bbox=bbox, pixel_check=(850, 650), target_color=(255, 255, 255))  # Adjust pixel_check and target_color if needed
if is_detected:
    print("CAPTCHA detected in the specified area!")
else:
    print("CAPTCHA not detected. Adjust the bbox or parameters.")
