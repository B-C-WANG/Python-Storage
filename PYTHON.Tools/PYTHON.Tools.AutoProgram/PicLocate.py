import AutoKeyboardMouseCtrl
from PIL import ImageGrab
import aircv as ac
import numpy as np


def pos_add(position,offset):
    return (position[0]+offset[0],position[1]+offset[1])


def locate_pic(filename,position="center"):
    im = ac.imread(filename)
    shape = im.shape
    _width = shape[1]/2
    _height = shape[0]/2
    data = np.array(ImageGrab.grab())
    pos = ac.find_template(data,im)["result"]
    # you can also use "ac.find_all_template"

    if position == "center":
        return pos
    if position == "leftup":
        return pos_add(pos,(-_width,-_height))
    if position == "up":
        return pos_add(pos,(0,-width))
    if position == "rightup":
        return pos_add(pos,(_width,-_height))
    if position == "left":
        return pos_add(pos,(-_width,0))
    if position == 'right':
        return  pos_add(pos,(_width,0))
    if position == "leftdown":
        return pos_add(pos,(-_width,_height))
    if position == "rightdown":
        return pos_add(pos,(_width,_height))
    if position == "down":
        return pos_add(pos,(0,_height))





#example: "pic3.png" is a picture of "close button" in Windows
#location = locate_pic("pic3.png")
#AutoKeyboardMouseCtrl.mouse_click(x=int(location[0]),y=int(location[1]))


