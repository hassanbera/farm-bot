import pyautogui
import time

def show_mouse_position():
    print("Mouse pozisyonunu görmek için hareket ettirin. Çıkış için Ctrl+C basın.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Mouse pozisyonu: X={x}, Y={y}", end="\r")  # Pozisyonu satır içinde günceller
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nÇıkış yapıldı.")
        

show_mouse_position()
