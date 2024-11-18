import ctypes
import time

# Windows API yapılandırmaları
PUL = ctypes.POINTER(ctypes.c_ulong)

# Klavye girdisi
class KeyBdInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),      # Sanal tuş kodu
        ("wScan", ctypes.c_ushort),    # Donanım tarama kodu
        ("dwFlags", ctypes.c_ulong),   # Ek bayraklar (basma veya bırakma işlemleri)
        ("time", ctypes.c_ulong),      # İşlem zamanı (genelde 0)
        ("dwExtraInfo", PUL)           # Ek bilgi pointer'ı
    ]

# Birleşik giriş türü (Union)
class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBdInput)  # Klavye girdisi
    ]

# Giriş yapısı (Structure)
class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),  # Girdi türü (klavye veya fare)
        ("ii", Input_I)            # Girdi birleşimi (Union)
    ]

def press_key(hexKeyCode):
    """
    Belirtilen tuşa basma işlemini gerçekleştirir.
    Args:
        hexKeyCode: Tuşun hexadecimal kodu (örneğin, 'W' için 0x11).
    """
    extra = ctypes.c_ulong(0)  # Ek bilgi
    ii_ = Input_I()  # Girdi birleşim türü
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))  # Tuş basma yapılandırması
    x = Input(ctypes.c_ulong(1), ii_)  # Klavye girdisi olarak tanımlanır
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))  # Tuş basma işlemini gönderir

def release_key(hexKeyCode):
    """
    Belirtilen tuşun bırakılması işlemini gerçekleştirir.
    Args:
        hexKeyCode: Tuşun hexadecimal kodu.
    """
    extra = ctypes.c_ulong(0)  # Ek bilgi
    ii_ = Input_I()  # Girdi birleşim türü
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))  # Tuş bırakma yapılandırması
    x = Input(ctypes.c_ulong(1), ii_)  # Klavye girdisi olarak tanımlanır
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))  # Tuş bırakma işlemini gönderir

def hold_key(hexKeyCode, duration):
    """
    Belirtilen tuşa belirtilen süre boyunca basılı tutar.
    Args:
        hexKeyCode: Tuşun hexadecimal kodu.
        duration: Tuşun basılı kalacağı süre (saniye cinsinden).
    """
    press_key(hexKeyCode)  # Tuşa basma işlemini gerçekleştir
    time.sleep(duration)  # Belirtilen süre boyunca bekle
    release_key(hexKeyCode)  # Tuşu bırakma işlemini gerçekleştir
