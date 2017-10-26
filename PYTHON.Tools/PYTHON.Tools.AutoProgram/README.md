# PYTHON.TOOLS.
## AutoKeyboardMouseCtrl.py
利用python程序化鼠标键盘控制操作
- **mouse_moveTo(x, y)**             
 move mouse to the location(x,y) in the screen. Input is two int, not turple
- **mouse_getPosition(sleep_time)** 
reutrn the position(two int) after sleep_time(unit: s)
- **mouse_click(x, y, click_type, times)** 
left(click_type == "L", default) or right (click_type == "R") click at the (x,y) position for times(default 1)
- **mouse_hold(x, y, click_type)** 
keep mouse down
- **mouse_release()** 
release
- **key_stringInput(str)** 
control the keyboard to input some string
- **key_keyInput(c)** 
key c, c is e.g. "ctrl", "leftshift", "a", "b" and so on, more details on VK_CODE in the file.
- **key_holdKey(c)** 
keep key c down
- **key_releaseKey(c)** 
key release

## PicLocate.py
you need aircv: https://github.com/NetEaseGame/aircv
输入一张图片，返回这张图片在屏幕中的位置（如果找不到，会返回最相近图片的位置）
- **locate_pic(filename, position)**
 filename: the filename of the picture you need to locate in the screen.
 position: default is "center", options are "left", "leftup", "leftdown", "right", "rightup", "rightdown", "up" and "down". Returns the location as following fig.1 shows:

![](http://i.imgur.com/H2deupy.jpg)
## GetPointColor.py
获取某一点的颜色，日后拓展功能

## color_detect.py
包含了GetPointColor的功能，此外可检测矩形区域是否有某种颜色，检测某点是否为某种颜色。推荐用于树莓派中对特别物体的检测，可作简易颜色传感器。
