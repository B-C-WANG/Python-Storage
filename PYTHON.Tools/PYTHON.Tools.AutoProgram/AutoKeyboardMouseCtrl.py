import time
import win32api
import win32con
from ctypes import *

VK_CODE = {
  'backspace': 0x08,
  'tab': 0x09,
  'clear': 0x0C,
  'enter': 0x0D,
  'shift': 0x10,
  'ctrl': 0x11,
  'alt': 0x12,
  'pause': 0x13,
  'caps': 0x14,
  'esc': 0x1B,
  'space': 0x20,
  'pageup': 0x21,
  'pagedown': 0x22,
  'end': 0x23,
  'home': 0x24,
  'left': 0x25,
  'up': 0x26,
  'right': 0x27,
  'down': 0x28,
  'select': 0x29,
  'print': 0x2A,
  'execute': 0x2B,
  'printscreen': 0x2C,
  'ins': 0x2D,
  'del': 0x2E,
  'help': 0x2F,
  '0': 0x30,
  '1': 0x31,
  '2': 0x32,
  '3': 0x33,
  '4': 0x34,
  '5': 0x35,
  '6': 0x36,
  '7': 0x37,
  '8': 0x38,
  '9': 0x39,
  'a': 0x41,
  'b': 0x42,
  'c': 0x43,
  'd': 0x44,
  'e': 0x45,
  'f': 0x46,
  'g': 0x47,
  'h': 0x48,
  'i': 0x49,
  'j': 0x4A,
  'k': 0x4B,
  'l': 0x4C,
  'm': 0x4D,
  'n': 0x4E,
  'o': 0x4F,
  'p': 0x50,
  'q': 0x51,
  'r': 0x52,
  's': 0x53,
  't': 0x54,
  'u': 0x55,
  'v': 0x56,
  'w': 0x57,
  'x': 0x58,
  'y': 0x59,
  'z': 0x5A,
  'num0': 0x60,
  'num1': 0x61,
  'num2': 0x62,
  'num3': 0x63,
  'num4': 0x64,
  'num5': 0x65,
  'num6': 0x66,
  'num7': 0x67,
  'num8': 0x68,
  'num9': 0x69,
  'multiply': 0x6A,
  'add': 0x6B,
  'separator': 0x6C,
  'subtract': 0x6D,
  'decimal': 0x6E,
  'divide': 0x6F,
  'F1': 0x70,
  'F2': 0x71,
  'F3': 0x72,
  'F4': 0x73,
  'F5': 0x74,
  'F6': 0x75,
  'F7': 0x76,
  'F8': 0x77,
  'F9': 0x78,
  'F10': 0x79,
  'F11': 0x7A,
  'F12': 0x7B,
  'F13': 0x7C,
  'F14': 0x7D,
  'F15': 0x7E,
  'F16': 0x7F,
  'F17': 0x80,
  'F18': 0x81,
  'F19': 0x82,
  'F20': 0x83,
  'F21': 0x84,
  'F22': 0x85,
  'F23': 0x86,
  'F24': 0x87,
  'numlock': 0x90,
  'scrolllock': 0x91,
  'leftshift': 0xA0,
  'rightshift ': 0xA1,
  'leftcontrol': 0xA2,
  'rightcontrol': 0xA3,
  'leftmenu': 0xA4,
  'rightmenu': 0xA5,
  'browser_back': 0xA6,
  'browser_forward': 0xA7,
  'browser_refresh': 0xA8,
  'browser_stop': 0xA9,
  'browser_search': 0xAA,
  'browser_favorites': 0xAB,
  'browser_start_and_home': 0xAC,
  'volume_mute': 0xAD,
  'volume_Down': 0xAE,
  'volume_up': 0xAF,
  'next_track': 0xB0,
  'previous_track': 0xB1,
  'stop_media': 0xB2,
  'play/pause_media': 0xB3,
  'start_mail': 0xB4,
  'select_media': 0xB5,
  'start_application_1': 0xB6,
  'start_application_2': 0xB7,
  'attn_key': 0xF6,
  'crsel_key': 0xF7,
  'exsel_key': 0xF8,
  'play_key': 0xFA,
  'zoom_key': 0xFB,
  'clear_key': 0xFE,
  '+': 0xBB,
  ',': 0xBC,
  '-': 0xBD,
  '.': 0xBE,
  '/': 0xBF,
  '`': 0xC0,
  ';': 0xBA,
  '[': 0xDB,
  '\\': 0xDC,
  ']': 0xDD,
  "'": 0xDE,
  }


class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def mouse_moveTo(x,y):
    windll.user32.SetCursorPos(x, y)


def mouse_getPosition(sleep_time=0):
    time.sleep(sleep_time)
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    print(int(po.x), int(po.y))
    return int(po.x), int(po.y)


def mouse_click(x=None, y=None, click_type="L", times=1):
    '''
    :param x: position x
    :param y: position x
    :param click_type: left or right click
    :param times: how much time click
    :return: None
    '''
    if not ((x is None) and (y is None)):
        mouse_moveTo(x, y)
        time.sleep(0.01)
    if click_type == "L":
        for i in range(times):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        return
    if click_type == "R":
        for i in range(times):
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def mouse_hold(x=None, y=None, click_type="L"):
    if not ((x is None) and (y is None)):
        mouse_moveTo(x, y)
        time.sleep(0.01)
    if click_type == "L":
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        return
    if click_type == "R":
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def mouse_release():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def key_stringInput(_str=''):
    for c in _str:
        win32api.keybd_event(VK_CODE[c], 0, 0, 0)
        win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)


def key_keyInput(c):
    win32api.keybd_event(VK_CODE[c], 0, 0, 0)
    win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)


def key_holdKey(c):
    win32api.keybd_event(VK_CODE[c], 0, 0, 0)


def key_releaseKey(c):
    win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)