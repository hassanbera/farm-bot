import pyautogui
import ctypes,time

# DPI farkını düzelt
ctypes.windll.user32.SetProcessDPIAware()

# Mouse tıklama fonksiyonu
def click_at(x, y):
    if pyautogui.onScreen(x, y):
        pyautogui.click(x, y)
        print(f"Tıklama yapıldı: ({x}, {y})")
    else:
        print(f"Koordinat ekran dışında: ({x}, {y})")

# Kullanım
time.sleep(5)
click_at(700, 500)  # Örnek koordinatlar
