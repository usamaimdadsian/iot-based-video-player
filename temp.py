from pynput import keyboard
from threading import Thread
import time

pressed_key = True
def on_press(key):
    global pressed_key
    if key == keyboard.Key.esc:
        print('break')
        # Stop listener
        pressed_key = False
        return False

def listen_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
th1 = Thread(target=listen_keyboard)
th1.start()
while pressed_key:
    print('h')
    time.sleep(1)
th1.join()    