import time
from input_handler import hold_key, mouse_click # Tuş işlemleri için import

def bot_action():
  
    last_press_time=time.time()

    try:

        
        while True:  # Sonsuz döngü
            print("Saldırı basladi...")
            hold_key(0x02,0.3)
            print("1")
            hold_key(0x05,0.1)
            print("moving")

            hold_key(0x2D,0.1)
            hold_key(0x2C,0.1)
            print("loot")
            time.sleep(0.2)
            hold_key(0x03,0.3)
            hold_key(0x02,0.3)
            hold_key(0x2D,0.1)
            hold_key(0x2C,0.1)
            print("loot")
            time.sleep(0.2)
            hold_key(0x04,0.3)
            hold_key(0x02,0.3)
            time.sleep(0.2)
            hold_key(0x2D,0.1)
            hold_key(0x2C,0.1)
            print("loot")
            hold_key(0xCB,0.5)
            time.sleep(0.3)
           
            print("Saldırı yaapılıyor...")
            
            
              
          
           
           
            

            current_time=time.time()
            if current_time-last_press_time >= 50:
                hold_key(0x3C,1)
                print("pot bastı")
                hold_key(0x3D,1)
                print("pot bastı")
                last_press_time=current_time 
            
                

                

    except KeyboardInterrupt:
            # Kullanıcı Ctrl+C tuşuna bastığında döngü durur
            print("Bot manuel olarak durduruldu.")
