import time
from input_handler import hold_key, mouse_click, mouse_move_and_click # Tuş işlemleri için import
from utils import press_space_while_moving, ice_air, ice_rain, icy_aura, press_space_while_moving_2

def bot_action():
    
    
    


    try:
        
       
        
        while True:  # Sonsuz döngü
        
            
          
        # Kamera Sabitleme Stage 1
            hold_key(0x0F, 0.14)
            time.sleep(1)
            hold_key(0x21, 0.13)
            time.sleep(1)
            hold_key(0x01, 0.14)
            time.sleep(1)
            hold_key(0x0F, 0.16)
            time.sleep(1)
            hold_key(0x21, 0.17)
            time.sleep(1)
            hold_key(0x01, 0.12)
            # Kamera Sabitleme Stage 1
            
            # İlk Dönüş için hareket
            hold_key(0x31, 0.1)
            hold_key(0x06, 0.1)
            hold_key(0x11, 15)
            hold_key(0x06, 0.15)
            hold_key(0x20, 0.75)
            # İlk Dönüş için hareket
            
            
            
            #Kristale gidiş
            press_space_while_moving_2()
            hold_key(0x20, 0.4)
            press_space_while_moving()
            #Kristale gidiş
            
            #Farma başlangıç
            hold_key(0x11, 7)
            hold_key(0x1E, 1)
            hold_key(0x11, 3.20)
            hold_key(0x1E, 0.5)
            hold_key(0x11, 3.30)
            hold_key(0x31, 0.15)
            #Farma başlangıç
            
            #Savaş Başlangıcı
            hold_key(0x07,0.2)
            hold_key(0x05,0.2)
            icy_aura()
            icy_aura()
            hold_key(0x05,2)
            ice_rain()
            hold_key(0x3B,0.2)
            ice_rain()
            ice_rain()
            
            ice_air()
            ice_air()
            hold_key(0x3B,0.2)
            ice_air()
            hold_key(0x3B,0.2)
            
            time.sleep(5)
            
            icy_aura()
            ice_rain()
            icy_aura()
            ice_rain()
            icy_aura()
            hold_key(0x3B,0.2)
            ice_rain()
            hold_key(0x3B,0.2)
            ice_rain()
            time.sleep(2)
            hold_key(0x3B,0.2)
            icy_aura()
            ice_rain()
            ice_rain()
            hold_key(0x3B,0.2)
            ice_rain()
            hold_key(0x3B,0.2)
            icy_aura()
            ice_air()
            ice_rain()
            hold_key(0x3B,0.2)
            icy_aura()
            ice_air()
            hold_key(0x3D,0.2)
            time.sleep(1)
            hold_key(0x58,0.2)
            hold_key(0x01,0.2)
            
            
            time.sleep(7)
            #Savaş btişi3
            
            #Karakter Seçimine Dönüş
            hold_key(0x01, 0.13)
            time.sleep(0.5)
            mouse_move_and_click(952, 582)
            time.sleep(2)
            mouse_move_and_click(874, 582)
            time.sleep(10)
            mouse_move_and_click(1690, 432)
            time.sleep(2)
            mouse_move_and_click(1754, 750)
            #Devamke213
            time.sleep(3)
             
            

    except KeyboardInterrupt:
            # Kullanıcı Ctrl+C tuşuna bastığında d3öngü durur
            print("Bot manuel olarak durduruldu.")