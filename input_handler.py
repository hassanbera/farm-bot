import ctypes
import time

# Windows API yapılandırmaları
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Tuş basma ve bırakma fonksiyonları
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# Mouse sol tıklama fonksiyonları
def mouse_left_click():
    extra = ctypes.c_ulong(0)
    mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))  # Sol tuş basma
    x = Input(ctypes.c_ulong(0), Input_I(mi=mi))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))  # Sol tuş bırakma
    x = Input(ctypes.c_ulong(0), Input_I(mi=mi))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def hold_key(hexKeyCode, duration):
    """
    Belirtilen tuşa belirtilen süre boyunca basılı tutar.
    Args:
        hexKeyCode: Tuşun hexadecimal kodu.
        duration: Tuşun basılı kalacağı süre (saniye cinsinden).
    """
    press_key(hexKeyCode)
    time.sleep(duration)
    release_key(hexKeyCode)

def mouse_click(duration):
    """
    Belirtilen süre boyunca fare sol tıklamasını basılı tutar.
    Args:
        duration (float): Sol tıklamanın basılı kalacağı süre (saniye cinsinden).
    """
    extra = ctypes.c_ulong(0)
    # Sol tıklamayı başlat
    mi = MouseInput(0, 0, 0, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), Input_I(mi=mi))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    # Belirtilen süre kadar bekle
    time.sleep(duration)
    # Sol tıklamayı bırak
    mi = MouseInput(0, 0, 0, 0x0004, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(0), Input_I(mi=mi))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def mouse_move_and_click(x, y, duration=0.5):
    """
    Fareyi belirtilen (x, y) koordinatlarına hareket ettirir ve sol tıklama yapar.
    """
    ctypes.windll.user32.SetProcessDPIAware()  # DPI ölçeklendirmesi düzeltmesi
    screen_width = ctypes.windll.user32.GetSystemMetrics(0)
    screen_height = ctypes.windll.user32.GetSystemMetrics(1)

    if 0 <= x < screen_width and 0 <= y < screen_height:
        ctypes.windll.user32.SetCursorPos(x, y)
        print(f"Mouse {x}, {y} koordinatına taşındı.")
        mouse_left_click()
        print(f"Mouse tıklaması ({x}, {y}) koordinatında gerçekleştirildi.")
    else:
        print(f"Hata: Koordinatlar ekran sınırları dışında ({x}, {y}).")