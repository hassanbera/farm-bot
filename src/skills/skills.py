from input_handling.input_handler import hold_key, mouse_move_and_click
import time

def icy_aura():
    """
    Simulates pressing the key for the 'Icy Aura' skill.
    """
    hold_key(0x03, 1)  # Press key '2'

def ice_rain():
    """
    Simulates the 'Ice Rain' skill by pressing a key and targeting.
    """
    hold_key(0x04, 0.1)  # Press key '3'
    mouse_move_and_click(857, 773)
    time.sleep(1)  # Delay for skill effect

def ice_air():
    """
    Simulates pressing the key for the 'Ice Air' skill.
    """
    hold_key(0x02, 1)  # Press key '1'
