#-*- coding: UTF-8 -*-
from PIL import Image,ImageDraw,ImageGrab
from ctypes import *
import sys
import os
import time
import win32gui
import win32api
import win32con
import time
class POINT(Structure):
  _fields_ = [("x", c_ulong),("y", c_ulong)]
def mouse_move(x,y):
  windll.user32.SetCursorPos(x, y)
def get_mouse_point():
  po = POINT()
  windll.user32.GetCursorPos(byref(po))
  print("mouse point:",po.x,po.y)
  return int(po.x), int(po.y)




def get_color_at_point(image,x,y):
    a=image.getpixel((x,y))

    return a

def get_color_at_point_in_screen(x,y):
    im = ImageGrab.grab()
    temp = get_color_at_point(im, x,y)
    print("color", temp)
    return temp

def get_color_at_mouse_position(wait_time):
    time.sleep(wait_time)
    x,y=get_mouse_point()
    im = ImageGrab.grab()
    temp = get_color_at_point(im,x,y)
    print("color",temp)
    return temp


def if_is_the_color_at_point(r,g,b,x,y,error):

        im=ImageGrab.grab()
        temp=get_color_at_point(im,x,y)
        if (temp[0]>r-error and temp[0]<r+error ) and (temp[1]>r-error and temp[1]<r+error ) and (temp[2]>r-error and temp[2]<r+error ):
            return True
        else:
            return False




def if_box_area_contains_the_color(startx,starty,endx,endy,r,g,b,error):
        im = ImageGrab.grab()
        for i in range(startx,endx):
            for j in range(starty,endy):
                temp = get_color_at_point(im, i, j)
                if (temp[0] > r - error and temp[0] < r + error) and (temp[1] > r - error and temp[1] < r + error) and (
                        temp[2] > r - error and temp[2] < r + error):
                    print("true")
                    return True
                else:
                    print('false')
                    return False




# Example:
# 1\ get the color at mouse position
#get_color_at_mouse_position(3)

# 2\ judge the area made by mouse if there is a white color in  (which color is 255, 255, 255)
print("get startX and startY in 3 seconds")
time.sleep(3)
sX,sY = get_mouse_point()
print("get endX and endY in 3 seconds")
time.sleep(3)
eX,eY = get_mouse_point()

a=1
while a:
    a= if_box_area_contains_the_color(sX,sY,eX,eY,255,255,255,3)
    a= 1 if not a else 0#if False, continue, else stop



# 3\ use raspberry's camera to detect if there is one certain thing by color