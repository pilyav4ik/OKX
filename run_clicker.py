import pyautogui
import time

def mouse_clicker(clicks=0, interval=0):
    """
    Simulates mouse clicks.

    :param clicks: Number of clicks to perform.
    :param interval: Time in seconds between each click.
    """
    for i in range(clicks):
        pyautogui.click()
        print(f"Click {i+1}/{clicks} performed")
        time.sleep(interval)

#CHANGE HERE
mouse_clicker(clicks=8, interval=10)
