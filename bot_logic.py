import time
from input_handler import hold_key, mouse_click, mouse_move_and_click # Tuş işlemleri için import

def bot_action():
    hold_key(0x11, 3.52)
    hold_key(0x1E, 0.97)
    hold_key(0x11, 3.43)
    hold_key(0x1E, 0.95)
    hold_key(0x11, 3.53)
    hold_key(0x1E, 0.91)
    hold_key(0x11, 2.11)
    hold_key(0x20, 0.77)
    hold_key(0x20, 0.18)
    hold_key(0x31, 0.12)
    hold_key(0x11, 0.68)
    hold_key(0x01, 0.12)
    time.sleep(1)
    mouse_move_and_click(999, 574)
    time.sleep(1)
    mouse_move_and_click(917, 574)
    time.sleep(3)
    mouse_move_and_click(1786, 524)
    time.sleep(10)
    mouse_move_and_click(1759, 744)
    time.sleep(10)
    mouse_move_and_click(987, 588)
    
   
    


    try:
       
        
        while True:  # Sonsuz döngü
           
            print("bot...")
                

    except KeyboardInterrupt:
            # Kullanıcı Ctrl+C tuşuna bastığında döngü durur
            print("Bot manuel olarak durduruldu.")