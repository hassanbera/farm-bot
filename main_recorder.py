from recorder import KeyboardMouseRecorder  # Recorder sınıfını içe aktar
from bot_logic import bot_action
import time

if __name__ == "__main__":
  # Recorder sınıfını başlat
    recorder = KeyboardMouseRecorder()

    print("Klavye ve fare girdilerini kaydetmek için hazır.")
    print("ESC tuşuna basarak kaydı durdurabilirsiniz.")
    time.sleep(3)
    # Kayıt işlemini başlat
    recorder.start_recording()

    # Kaydedilen girdileri bir dosyaya yaz
    file_name = "recorded_inputs.txt"
    recorder.save_records(file_name)

    print(f"Girdiler kaydedildi: {file_name}")
    



