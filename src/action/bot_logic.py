import time
from input_handling.input_handler import hold_key, mouse_click, mouse_move_and_click # Tuş işlemleri için import
from captcha_detection.captcha_detector import handle_captcha
from captcha_detection.captcha_detector import image_show

def bot_action():
    
    
    try:
        
       
        
        while True:  # Sonsuz döngü
        
            
          
        # Farming logic
            print("Farming...")
            

            # Check for CAPTCHA and handle it
            handle_captcha(bbox=(804,472,1113,604), click_coords=(891, 584))
            
            

            # Resume farming
            print("Resuming farming...")
             
            

    except KeyboardInterrupt:
            # Kullanıcı Ctrl+C tuşuna bastığında d3öngü durur
            print("Bot manuel olarak durduruldu.")