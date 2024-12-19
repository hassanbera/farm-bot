import time
from input_handler import hold_key, mouse_click, mouse_move_and_click # Tuş işlemleri için import
from utils import press_space_while_moving, ice_air, ice_rain, icy_aura, press_space_while_moving_2, handle_captcha


def bot_action():
    
    
    


    try:
        
       
        
        while True:  # Sonsuz döngü
        
            
          
        # Farming logic
            print("Farming...")

            # Check for CAPTCHA and handle it
            handle_captcha(bbox=(800, 600, 1200, 800), click_coords=(960, 640))

            # Resume farming
            print("Resuming farming...")
             
            

    except KeyboardInterrupt:
            # Kullanıcı Ctrl+C tuşuna bastığında d3öngü durur
            print("Bot manuel olarak durduruldu.")