import threading
import time
from input_handling.input_handler import hold_key

def press_space_while_moving():
    """
    Moves while pressing the Space key intermittently.
    """
    def press_space():
        for i in range(5):
            hold_key(0x39, 0.1)  # Space key
            print(f"Space pressed ({i + 1}/5)")
            time.sleep(1)

    space_thread = threading.Thread(target=press_space)
    space_thread.start()

    hold_key(0x11, 13)  # W key for movement
    print("Movement completed.")
    space_thread.join()
    print("Space pressing completed.")

def press_space_while_moving_2():
    """
    Moves while pressing the Space key intermittently.
    """
    def press_space():
        for i in range(5):
            hold_key(0x39, 0.1)  # Space key
            print(f"Space pressed ({i + 1}/5)")
            time.sleep(1)

    space_thread = threading.Thread(target=press_space)
    space_thread.start()

    hold_key(0x11, 10)  # W key for movement
    print("Movement completed.")
    space_thread.join()
    print("Space pressing completed.")
