import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from colorama import Fore, init
import configparser

init(autoreset=True)
config = configparser.ConfigParser()
config.read('config.ini')

# ? KEYS
TOGGLE_LEFT = KeyCode(char=config['KEYS']['TOGGLE_LEFT'])
TOGGLE_RIGHT = KeyCode(char=config['KEYS']['TOGGLE_RIGHT'])
TOGGLE_BOTH = KeyCode(char=config['KEYS']['TOGGLE_BOTH'])
TOGGLE_BOTH_INTERVAL = KeyCode(char=config['KEYS']['TOGGLE_BOTH_INTERVAL'])
# ? DELAY
CLICK_PER_SECOND = int(config['CLICK']['CLICK_PER_SECOND'])
CLICK_DELAY = 1 / CLICK_PER_SECOND
CLICK_BOTH_DELAY = float(config['CLICK']['CLICK_BOTH_DELAY'])


# TOGGLE_LEFT = KeyCode(char='t')
# TOGGLE_RIGHT = KeyCode(char='y')
# TOGGLE_BOTH = KeyCode(char='u')
# TOGGLE_BOTH_INTERVAL = KeyCode(char='i')

clicking_left = False
clicking_right = False
clicking_both = False
clicking_both_interval = False
mouse = Controller()

print(f"{Fore.YELLOW}=====================")
print(f"{Fore.YELLOW}AUTO CLICKER")
print(f"{Fore.YELLOW}Created by : Kerogs")
print(f"{Fore.YELLOW}Version : 1.0.0")
print(f"{Fore.YELLOW}Github : https://github.com/kerogs/autoclick")
print(f"{Fore.YELLOW}=====================")
print("")
print(f"{Fore.GREEN}Press {Fore.YELLOW}{TOGGLE_LEFT} {Fore.GREEN}to toggle left click")
print(f"{Fore.GREEN}Press {Fore.YELLOW}{TOGGLE_RIGHT} {Fore.GREEN}to toggle right click")
print(f"{Fore.GREEN}Press {Fore.YELLOW}{TOGGLE_BOTH} {Fore.GREEN}to toggle both clicks")
print(f"{Fore.GREEN}Press {Fore.YELLOW}{TOGGLE_BOTH_INTERVAL} {Fore.GREEN}to toggle both clicks with interval")
print(f"{Fore.GREEN}Click per second set to {Fore.YELLOW}{CLICK_PER_SECOND}c/s (Delay : {CLICK_DELAY}s)")
print(f"{Fore.BLUE} Press to start...")

def clear_last_line():
    print("\033[F\033[K", end='')

def clicker():
    while True:
        if clicking_left:
            mouse.click(Button.left, 1)
        if clicking_right:
            mouse.click(Button.right, 1)
        if clicking_both:
            mouse.click(Button.left, 1)
            mouse.click(Button.right, 1)
        if clicking_both_interval:
            mouse.click(Button.left, 1)
            time.sleep({CLICK_BOTH_DELAY})  # Petit intervalle entre les clics
            mouse.click(Button.right, 1)
        time.sleep(CLICK_DELAY)  # Ajuster le délai selon besoin

def toggle_event(key):
    global clicking_left, clicking_right, clicking_both, clicking_both_interval
    
    clear_last_line()
    
    if key == TOGGLE_LEFT:
        clicking_left = not clicking_left
        clicking_right = False
        clicking_both = False
        clicking_both_interval = False
        print(f"{Fore.BLUE}Left clicker {'activated' if clicking_left else 'deactivated'}")
    elif key == TOGGLE_RIGHT:
        clicking_left = False
        clicking_right = not clicking_right
        clicking_both = False
        clicking_both_interval = False
        print(f"{Fore.BLUE}Right clicker {'activated' if clicking_right else 'deactivated'}")
    elif key == TOGGLE_BOTH:
        clicking_left = False
        clicking_right = False
        clicking_both = not clicking_both
        clicking_both_interval = False
        print(f"{Fore.BLUE}Both clickers {'activated' if clicking_both else 'deactivated'}")
    elif key == TOGGLE_BOTH_INTERVAL:
        clicking_left = False
        clicking_right = False
        clicking_both = False
        clicking_both_interval = not clicking_both_interval
        print(f"{Fore.BLUE}Both clickers with interval {'activated' if clicking_both_interval else 'deactivated'}")
    else:
        print(f"{Fore.BLUE}Press to start...")
        clicking_left = False
        clicking_right = False
        clicking_both = False
        clicking_both_interval = False

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
