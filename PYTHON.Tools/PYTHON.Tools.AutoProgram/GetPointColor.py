import AutoKeyboardMouseCtrl as akm
from PIL import ImageGrab
import time

# Attention: PIL will return (BGR) not (RGB)

def get_color_at_point(position):
    im = ImageGrab.grab()
    im = im.load()
    return im[position[0],position[1]]

def get_color_where_mouse_is(delta_time):
    time.sleep(delta_time)
    pos = akm.mouse_getPosition()
    return get_color_at_point(pos)

#print(get_color_where_mouse_is(1))


