from pynput import keyboard, mouse
import time

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

            key_name = key.char if hasattr(key, 'char') else str(key)

            # Sadece ilk basıldığında kaydedelim
            if key_name not in self.press_times:
                self.press_times[key_name] = time.time()  # İlk basılma zamanını kaydet
        except Exception as e:
            print(f"Tuş kaydedilemedi: {e}")

    def on_key_release(self, key):
        """
        Klavye tuşu bırakıldığında çağrılır.
        """
        try:
            if key == keyboard.Key.enter:
                return

            key_name = key.char if hasattr(key, 'char') else str(key)

            # Basılı tutma süresini hesapla
            press_time = self.press_times.pop(key_name, None)
            if press_time is not None:
                duration = time.time() - press_time  # Tuş basılı kalma süresi
                self.records.append((f"hold_key({key_name}, {duration:.2f})"))
                print(f"Tuş: {key_name}, Süre: {duration:.2f} saniye")
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
