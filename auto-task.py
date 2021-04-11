import pyautogui
import pynput
import time
import PIL
import os
from PIL import ImageGrab, Image
from pynput import keyboard

# Colors & Images & Misc

Red_wire = 255, 0, 0
Yellow_wire = 255, 235, 4
Blue_wire = 38, 38, 255
Pink_wire = 255, 0, 255

Door_id = 71, 147, 52

# Electrical_color_1 = 14, 93, 255
# Electrical_color_2 = 13, 93, 255

Ring_color_1 = 255, 227, 0
Ring_color_2 = 83, 98, 255
Ring_color_3 = 111, 249, 255

Download_color = 241, 212, 161

Plunger_color = 170, 86, 88

# Checks


# def is_electrical():
#     screenshot = ImageGrab.grab(bbox=(805, 535, 806, 810))
#     check_r, check_g, check_b = screenshot.getpixel((0, 0))
#     print(check_g, check_b)
#     if check_g == 93 and check_b == 255:
#         return True
#     else:
#         return False


def is_airship_plunger():
    screenshot = ImageGrab.grab(bbox=(815, 700, 816, 701))
    if_plunger = screenshot.getpixel((0, 0))
    if if_plunger == Plunger_color:
        return True
    else:
        return False


def is_airship_door():
    screenshot = ImageGrab.grab(bbox=(1590, 975, 1591, 976))
    if_door = screenshot.getpixel((0, 0))
    if if_door == Door_id:
        return True
    else:
        return False


def is_download():

    screenshot = ImageGrab.grab(bbox=(1265, 470, 1266, 471))
    if_download = screenshot.getpixel((0, 0))
    if if_download == Download_color:
        return True
    else:
        return False


def is_wire():
    screenshot = ImageGrab.grab(bbox=(555, 270, 556, 271))
    if_wire = screenshot.getpixel((0, 0))
    if if_wire == Red_wire or if_wire == Yellow_wire or if_wire == Blue_wire or if_wire == Pink_wire:
        return True
    else:
        return False

# Functions


# def electrical():
#     while True:
#         screenshot = ImageGrab.grab(bbox=(1160, 235, 1161, 530))
#         ring_1 = screenshot.getpixel((0, 0))
#         ring_2 = screenshot.getpixel((0, 265))
#         # ring_3 = screenshot.getpixel((0, 520))

#         if ring_1 == Ring_color_1:
#             time.sleep(0.005)
#             pyautogui.moveTo(1230, 315)
#             pyautogui.click()
#             pyautogui.moveTo(1225, 585)

#         if ring_2 == Ring_color_2:
#             pyautogui.click()
#             break
#         # if ring_3 == Ring_color_3:
#         #     pyautogui.moveTo(1230, 845)
#         #     pyautogui.click()


def plunger():
    pyautogui.moveTo(830, 380)
    pyautogui.mouseDown()
    for i in range(15):
        pyautogui.moveTo(825, 525)
        pyautogui.moveTo(830, 380)
    pyautogui.mouseUp


def wires():
    wire_pos_L, wire_pos_R = [(555, 270), (555, 460), (555, 645), (555, 830)], [
        (1340, 270), (1340, 460), (1340, 645), (1340, 830)]

    screenshot = ImageGrab.grab(bbox=(555, 270, 560, 871))
    screenshot.show
    wire_1, wire_2, wire_3, wire_4 = screenshot.getpixel((0, 1)), screenshot.getpixel(
        (0, 170)), screenshot.getpixel((0, 350)), screenshot.getpixel((0, 525))

    screenshot = ImageGrab.grab(bbox=(1340, 270, 1341, 871))
    wire_5, wire_6, wire_7, wire_8 = screenshot.getpixel((0, 1)), screenshot.getpixel(
        (0, 170)), screenshot.getpixel((0, 350)), screenshot.getpixel((0, 525))

    wireL, wireR = [wire_1, wire_2, wire_3, wire_4], [
        wire_5, wire_6, wire_7, wire_8]

    L, R = 0, 0
    for s in range(4):
        for i in range(4):
            if wireL[L] == wireR[R]:
                xpos, ypos = wire_pos_L[L]
                xloc, yloc = wire_pos_R[R]
                pyautogui.moveTo(xpos, ypos)
                pyautogui.mouseDown()
                pyautogui.moveTo(xloc, yloc)
                pyautogui.mouseUp()
                break
            else:
                R += 1
        R = 0
        L += 1


def downloads():
    pyautogui.moveTo(955, 665)
    pyautogui.click()


def airship_door():
    pyautogui.click(1020, 870)
    time.sleep(0.2)
    pyautogui.moveTo(685, 175)
    pyautogui.mouseDown()
    pyautogui.moveTo(685, 855, 1.2)
    pyautogui.mouseUp()


# Hotkey


def on_activate():
    time.sleep(0.8)
    if is_wire() is True:
        wires()
        return print("wires")
    elif is_download() is True:
        downloads()
        return print("download")
    elif is_airship_door() is True:
        airship_door()
        return print("a-ship_door")
    elif is_airship_plunger() is True:
        plunger()
        return print("toilet-time")
    # elif is_electrical() is True:
    #     electrical()
    #     return print("electrical")


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(keyboard.HotKey.parse('<space>'), on_activate)

with keyboard.Listener(on_press=for_canonical(hotkey.press),
                       on_release=for_canonical(hotkey.release)) as l:
    l.join()
