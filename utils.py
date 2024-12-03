
import time  # Zaman gecikmeleri eklemek için kullanılan modül

def wait(seconds):
    """
    Belirtilen süre boyunca bekler ve süreyi konsola yazdırır.
    Args:
        seconds: Beklenecek süre (saniye cinsinden).
    """
    print(f"{seconds} saniye bekleniyor...")
    time.sleep(seconds)  # Belirtilen süre boyunca bekle
