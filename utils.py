
import pytesseract
from PIL import ImageGrab
import re
import time
from input_handler import hold_key, mouse_move_and_click
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def wait(seconds):
    """
    Belirtilen süre boyunca bekler ve süreyi konsola yazdırır.
    Args:
        seconds: Beklenecek süre (saniye cinsinden).
    """
    print(f"{seconds} saniye bekleniyor...")
    time.sleep(seconds)  # Belirtilen süre boyunca bekle

import threading

def press_space_while_moving():
    """
    Hareket (örneğin, W tuşuna basma) devam ederken Space tuşuna eş zamanlı olarak basar.
    """
    def press_space():
        """
        Space tuşuna 5 kez saniyede bir basar.
        """
        for i in range(5):
            hold_key(0x39, 0.1)  # Space tuşuna bas
            print(f"Space tuşuna basıldı ({i + 1}/5)")
            time.sleep(1)  # 1 saniye bekle
    
    # Space tuşuna basma işlemini ayrı bir thread ile çalıştır
    space_thread = threading.Thread(target=press_space)
    space_thread.start()

    # Ana hareket (örneğin, W tuşuna basma)
    hold_key(0x11, 13)  # W tuşuna 8 saniye boyunca basar
    print("Ana hareket (W tuşu) tamamlandı.")
    
    # Space tuşu basma işleminin bitmesini bekle
    space_thread.join()
    print("Space tuşu basma işlemi tamamlandı.")

def icy_aura():
     hold_key(0x03, 1) #2'ye basma
        
        
def ice_rain():
    hold_key(0x04, 0.1)
    mouse_move_and_click(857, 773)
    time.sleep(1) #Alan açma denemesi

def ice_air():
    hold_key(0x02, 1) # 1'e basma
    

def press_space_while_moving_2():
    """
    Hareket (örneğin, W tuşuna basma) devam ederken Space tuşuna eş zamanlı olarak basar.
    """
    def press_space():
        """
        Space tuşuna 5 kez saniyede bir basar.
        """
        for i in range(5):
            hold_key(0x39, 0.1)  # Space tuşuna bas
            print(f"Space tuşuna basıldı ({i + 1}/5)")
            time.sleep(1)  # 1 saniye bekle
    
    # Space tuşuna basma işlemini ayrı bir thread ile çalıştır
    space_thread = threading.Thread(target=press_space)
    space_thread.start()

    # Ana hareket (örneğin, W tuşuna basma)
    hold_key(0x11, 10)  # W tuşuna 8 saniye boyunca basar
    print("Ana hareket (W tuşu) tamamlandı.")
    
    # Space tuşu basma işleminin bitmesini bekle
    space_thread.join()
    print("Space tuşu basma işlemi tamamlandı.")
    

def detect_captcha(bbox=(800, 600, 1200, 800), pixel_check=(850, 650), target_color=(255, 255, 255)):
    """
    Detects if a CAPTCHA is visible by checking a pixel or region.
    Args:
        bbox: Tuple defining the screenshot region for CAPTCHA detection.
        pixel_check: Pixel coordinates to check for specific color.
        target_color: Expected RGB color indicating CAPTCHA.
    Returns:
        bool: True if CAPTCHA is detected; otherwise False.
    """
    screenshot = ImageGrab.grab(bbox=bbox)
    pixel_color = screenshot.getpixel(pixel_check)
    return pixel_color == target_color

def solve_captcha(bbox=(800, 600, 1200, 800)):
    """
    Solves the CAPTCHA by reading and solving the math problem.
    Args:
        bbox: Tuple defining the screenshot region to capture CAPTCHA.
    Returns:
        int or None: Solved CAPTCHA result if recognized, otherwise None.
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

def handle_captcha(bbox=(800, 600, 1200, 800), click_coords=(960, 640)):
    """
    Detects, solves, and handles the CAPTCHA popup.
    Args:
        bbox: Region to detect and solve CAPTCHA.
        click_coords: Coordinates of the "Yes" button.
    """
    if detect_captcha(bbox=bbox):
        print("CAPTCHA detected!")
        answer = solve_captcha(bbox=bbox)
        if answer is not None:
            # Type the answer
            for char in str(answer):
                hold_key(char, 0.1)  # Adjust if `char` isn't directly mappable
            time.sleep(0.5)
            # Click "Yes" button
            mouse_move_and_click(*click_coords)
            print("CAPTCHA solved and handled successfully.")
        else:
            print("Failed to solve CAPTCHA.")
