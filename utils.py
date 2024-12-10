
import time

from input_handler import hold_key, mouse_move_and_click  # Zaman gecikmeleri eklemek için kullanılan modül

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