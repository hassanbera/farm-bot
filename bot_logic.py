import time
from input_handler import hold_key, mouse_click # Tuş işlemleri için import

def bot_action():
    """
    Botun ana döngüsü.
    - Belirli tuşlara sırasıyla basar ve bırakır.
    - Kullanıcı Ctrl+C ile döngüyü durdurabilir.
    """
print("Bot çalışıyor...")
hold_key(0x04,1)
print("3 tuşuna basıldı...")
hold_key(0x11,12)
print("W tuşuna 12 saniye boyunca basılıyor...")
hold_key(0x1E,0.35)
print("A tuşuna 0.35 saniye boyunca basılıyor...")
hold_key(0x11,7)  
print("W tuşuna 7 saniye boyunca basılıyor...")
hold_key(0x20,0.35)
print("D tuşuna 0.35 saniye boyunca basılıyor...")
hold_key(0x11,6)
print("W tuşuna 6 saniye boyunca basılıyor...")
hold_key(0x04,1)
print("3 tuşuna basıldı...")
hold_key(0x20,0.4)
print("D tuşuna 0.4 saniye boyunca basılıyor...")


  

try:
        while True:  # Sonsuz döngü
            print("Döngü başladı...")
            hold_key(0x11,10)  
            print("W tuşuna 10 saniye boyunca basılıyor...")
            hold_key(0x31,1)
            print("N tuşuna basıldı...")
            hold_key(0x03,1)
            print("2 tuşuna basıldı...")
            mouse_click(1)
            print("Mouse'a basıldı...")
            time.sleep(3)
            hold_key(0x11,10)  
            print("W tuşuna 10 saniye boyunca basılıyor...")
            hold_key(0x31,1)
            print("N tuşuna basıldı...")
            
            
            
        
           

except KeyboardInterrupt:
        # Kullanıcı Ctrl+C tuşuna bastığında döngü durur
        print("Bot manuel olarak durduruldu.")
