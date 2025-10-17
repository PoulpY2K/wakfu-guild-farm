import sys
from enum import Enum

import pyautogui


class Click(Enum):
    RIGHT_CLICK = 1
    LEFT_CLICK = 2


def focus_wakfu():
    if sys.platform == "win32":
        windows = pyautogui.getWindowsWithTitle("WAKFU")
        windows = list(filter(lambda x: x.title == "WAKFU", windows))
        windows[0].activate()
    else:
        import subprocess

        # find the app or window back and activate it
        apple = """
        set the_title to "%s"
        tell application "System Events"
            repeat with p in every process whose background only is false
                repeat with w in every window of p
                    if (name of w) is the_title then
                        tell p
                            set frontmost to true
                            perform action "AXRaise" of w
                        end tell
                    end if
                end repeat
            end repeat
        end tell
    """ % ("WAKFU",)
        (subprocess.Popen(
            "osascript",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf8",
            text=True,
        ).communicate(apple)[0])

    pyautogui.sleep(0.1)


def interact_button(type_click: Click, x, y, sleep=0.0):
    if type_click == Click.RIGHT_CLICK:
        # Click on the button
        pyautogui.rightClick(x, y)
    else:
        pyautogui.leftClick(x, y)
    # Wait for action
    pyautogui.sleep(sleep)


def get_inside_room(rx, ry, lx, ly):
    # Right click hole
    interact_button(Click.RIGHT_CLICK, rx, ry, sleep=0.2)
    # Enter hole
    interact_button(Click.LEFT_CLICK, lx, ly, sleep=2.0)


def press_key(key, sleep=0.0):
    # Press the key
    pyautogui.press(key)
    # Wait for action
    pyautogui.sleep(sleep)


def finish_battle(x, y):
    # Close battle report
    pyautogui.press("esc")
    # Back out of the room
    pyautogui.click(x, y)
    # Sleep for a bit
    pyautogui.sleep(3)
