import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from colorama import Fore, init
import os

init(autoreset=True)

TOGGLE_LEFT = KeyCode(char='t')
TOGGLE_RIGHT = KeyCode(char='y')
TOGGLE_BOTH = KeyCode(char='u')
TOGGLE_BOTH_INTERVAL = KeyCode(char='i')

clicking_left = False
clicking_right = False
clicking_both = False
clicking_both_interval = False
mouse = Controller()

print(f"{Fore.YELLOW}=====================")
print(f"{Fore.YELLOW}AUTO CLICKER")
print(f"{Fore.YELLOW}Created by : Kerogs")
print(f"{Fore.YELLOW}Version : 0.2.0")
print(f"{Fore.YELLOW}Github : https://github.com/Kerogs/AutoClick")
print(f"{Fore.YELLOW}=====================")
print("")
print(f"{Fore.GREEN}Press {Fore.YELLOW}'t' {Fore.GREEN}to toggle left click")
print(f"{Fore.GREEN}Press {Fore.YELLOW}'y' {Fore.GREEN}to toggle right click")
print(f"{Fore.GREEN}Press {Fore.YELLOW}'u' {Fore.GREEN}to toggle both clicks")
print(f"{Fore.GREEN}Press {Fore.YELLOW}'i' {Fore.GREEN}to toggle both clicks with interval")
print(f"{Fore.GREEN}Click per second set to {Fore.YELLOW}100c/s (Delay : 0.01s)")
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
            time.sleep(0.05)  # Petit intervalle entre les clics
            mouse.click(Button.right, 1)
        time.sleep(0.01)  # Ajuster le délai selon besoin

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
