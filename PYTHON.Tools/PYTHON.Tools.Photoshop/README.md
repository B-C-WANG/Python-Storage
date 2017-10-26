# PYTHON.Tools.Photoshop
- **最近在“学堂在线”学习CS101公开课的时候，看到了用javascript实现的非常酷炫的图片处理效果，于是准备用python实现一下**
- **这里只是实现图片的效果，编程的强大在于，可以在此基础上实现电影中每一帧的的“photoshop”**
- **自己只是为了学习而练习，并不能够做到比较高的程度，如果今后需要会继续添加功能**

## ImageMatting: API

方法名称 | 功能
:--: | :--:
class ImageMatting | -
load_image(filename,**kwargs) | 使用opencv载入图片
select_position_by_color(color, logic) | 使用颜色逻辑选出符合条件的位置，返回一个list[set(intX,intY)]，输入如(200,200,200),("==",">=","<=")即是B==200, G>=200, R<=200的像素点的位置（opencv的格式是BGR），如果是灰度，就只需要一个数据。
select_position_by_color_average(color,scale)| 计算每个像素点颜色的平均值，将其乘以scale，如果所选color（取值为0,1,2对应于BGR）大于这个值，返回像素点所在位置，不能用于灰度图片。
_select_position_by_color_filter(...) | 内置函数，用于select_position_by_color的实现，利用numpy.where进行筛选。
select_color_by_position(position) | 输入一个位置，返回这些位置上的像素点颜色
replace_color_in_position(position_list, color) |在所有position_list中的位置，将颜色替换成color，如果color是一个定值，就替换成纯色。如果color是list，就一一对应着替换position上的颜色，如果color长度小于position_list，就替换color长度的颜色，如果color长度大于position_list，用了一个try函数保证不会中断
display_info | 打印图片信息，包括名称，大小
image_show | 调用opencv的imshow方法，其中winname为图片名称。

**demo**
```
b = ImageMatting()
a = ImageMatting()
b.load_image("stop.jpg",flags=3)
a.load_image("leaves.jpg",flags=3)
# 选出红色最突出的位置
position = b.select_position_by_color_average(color=2,scale=1.5)
# 按照这个所选出的位置在另一张图取样
color = a.select_color_by_position(position)
# 将位置上的像素进行取代
b.replace_color_in_position(position,color)
b.image_show()
b.image_save("output.jpg")
```
效果图：
![](http://i.imgur.com/ejVOBli.jpg)
![](http://i.imgur.com/kIrp4jA.jpg)
![](http://i.imgur.com/wLYfSKU.jpg)
