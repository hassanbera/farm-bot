from pynput import keyboard, mouse
import time

SCANCODES = {
    # Harfler
    'a': 0x1E, 'b': 0x30, 'c': 0x2E, 'd': 0x20, 'e': 0x12,
    'f': 0x21, 'g': 0x22, 'h': 0x23, 'i': 0x17, 'j': 0x24,
    'k': 0x25, 'l': 0x26, 'm': 0x32, 'n': 0x31, 'o': 0x18,
    'p': 0x19, 'q': 0x10, 'r': 0x13, 's': 0x1F, 't': 0x14,
    'u': 0x16, 'v': 0x2F, 'w': 0x11, 'x': 0x2D, 'y': 0x15,
    'z': 0x2C,

    # Rakamlar
    '1': 0x02, '2': 0x03, '3': 0x04, '4': 0x05, '5': 0x06,
    '6': 0x07, '7': 0x08, '8': 0x09, '9': 0x0A, '0': 0x0B,

    # Yön Tuşları
    'up': 0xC8, 'down': 0xD0, 'left': 0xCB, 'right': 0xCD,

    # Fonksiyon Tuşları
    'f1': 0x3B, 'f2': 0x3C, 'f3': 0x3D, 'f4': 0x3E, 'f5': 0x3F,
    'f6': 0x40, 'f7': 0x41, 'f8': 0x42, 'f9': 0x43, 'f10': 0x44,
    'f11': 0x57, 'f12': 0x58,

    # Kontrol Tuşları
    'enter': 0x1C, 'backspace': 0x0E, 'tab': 0x0F, 'capslock': 0x3A,
    'shift_left': 0x2A, 'shift_right': 0x36, 'ctrl_left': 0x1D,
    'ctrl_right': 0x9D, 'alt_left': 0x38, 'altgr': 0xB8, 'esc': 0x01,

    # Diğer Tuşlar
    'space': 0x39, 'delete': 0xD3, 'insert': 0xD2, 'home': 0xC7,
    'end': 0xCF, 'page_up': 0xC9, 'page_down': 0xD1
}

class KeyboardMouseRecorder:
    """
    Klavye ve fare girdilerini kaydeden sınıf.
    """
    def __init__(self):
        self.records = []  # Kaydedilen girdiler için liste
        self.press_times = {}  # Tuşların basılma zamanlarını tutar
        self.is_recording = True  # Kaydı kontrol etmek için bayrak

    def on_key_press(self, key):
        """
        Klavye tuşuna basıldığında çağrılır.
        """
        try:
            # Enter tuşu tetikleyici olarak kullanılır
            if key == keyboard.Key.enter:
                print("Enter tuşuna basıldı. Kayıt durduruluyor...")
                self.is_recording = False
                return False  # Listener'ı durdur

            # Özel tuşlar için kontrol
            key_name = None
            if hasattr(key, 'char') and key.char:
                key_name = key.char.lower()
            elif key in keyboard.Key.__members__.values():  # Özel tuşlar
                key_name = key.name.lower()

            # Sadece tanımlı tuşları kaydedelim
            if key_name in SCANCODES and key_name not in self.press_times:
                self.press_times[key_name] = time.time()  # İlk basılma zamanını kaydet
        except Exception as e:
            print(f"Tuş kaydedilemedi: {e}")

    def on_key_release(self, key):
        """
        Klavye tuşu bırakıldığında çağrılır.
        """
        try:
            key_name = None
            if hasattr(key, 'char') and key.char:
                key_name = key.char.lower()
            elif key in keyboard.Key.__members__.values():  # Özel tuşlar
                key_name = key.name.lower()

            # Basılı tutma süresini hesapla
            if key_name in SCANCODES:
                press_time = self.press_times.pop(key_name, None)
                if press_time is not None:
                    duration = time.time() - press_time  # Tuş basılı kalma süresi
                    scancode = SCANCODES[key_name]  # Scancode değerini al
                    self.records.append((f"hold_key(0x{scancode:02X}, {duration:.2f})"))
                    print(f"Tuş: {key_name}, Scancode: 0x{scancode:02X}, Süre: {duration:.2f} saniye")
        except Exception as e:
            print(f"Tuş bırakma kaydedilemedi: {e}")

    def on_mouse_click(self, x, y, button, pressed):
        """
        Fare tıklandığında çağrılır.
        """
        if pressed and self.is_recording:
            # Kaydı string formatında ekle
            self.records.append((f"mouse_move_and_click({x}, {y})"))
            print(f"Mouse tıklaması: ({x}, {y}) - Buton: {button.name}")

    def start_recording(self):
        """
        Kayıt işlemine başlar.
        """
        print("Kayıt başlıyor... 'Enter' tuşuna basarak kaydı durdurabilirsiniz.")
        with keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release) as key_listener, \
             mouse.Listener(on_click=self.on_mouse_click) as mouse_listener:
            key_listener.join()  # Klavye dinleyicisini başlat

    def save_records(self, file_name="recorded_inputs.txt"):
        """
        Kaydedilen girdileri bir dosyaya yazar.
        """
        try:
            with open(file_name, "w") as file:
                for record in self.records:
                    file.write(f"{record}\n")
            print(f"Kayıt tamamlandı ve '{file_name}' dosyasına kaydedildi.")
        except Exception as e:
            print(f"Kayıt dosyaya yazılamadı: {e}")
