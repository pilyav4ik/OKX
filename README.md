0. Install Python https://www.python.org/downloads/

1. Run command `pip install -r requirements.txt`
1. Create File  `clicker.py`
2. Add code 


```
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

```

4. Enter the number of clicks to be made and the interval between clicks 

    > mouse_clicker(clicks=8, interval=10)

5. Run program from command line `python run_clicker.py`

6. Place the cursor on one of the button

![preview!](/CURSOR.jpg "San Juan Mountains")
# OKX
