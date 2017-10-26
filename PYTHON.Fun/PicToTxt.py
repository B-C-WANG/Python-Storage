import cv2
import numpy as np

class image_to_txt():
    def __init__(self,image_path):
        self.image_path=image_path
        self.image_data=self.image_read(image_path)
        self.image_shape=self.image_data.shape
    def image_read(self,image_path):
        return cv2.imread(image_path,flags=0)


    #IN: Gray value
    #OUT: Nearest String (According to color_dict)
    def color_trans(self,color):
        color_dict={

        "B ":0,
       #"￥":40,
        #"《":70,
        #"（":100,
        "c ":130,
        #"；":160,
        #"":190,
        #"、":220,
        "b ":255,

        }
        color_distance=color_dict
        for key,value in color_dict.items():
            gd=abs(color-value)
            color_distance[key]=gd
        minv=min(color_distance.values())

        for key, value in color_distance.items():
            if value==minv:
                return key

    def show_data(self):
        print("image_data is",self.image_data)
        print("image shape is",self.image_data.shape)

    def write_to_txt(self,txt_path):
        str=""
        file=open(txt_path,"w")
        for i in range(self.image_shape[0]):
            str+="\n"
            print(i)
            for j in range(self.image_shape[1]):
                    color=(self.color_trans((self.image_data[i][j])))
                    str+=color
        file.write(str)
        file.close()


filename="timg"
tem=image_to_txt(image_path="{}.jpg".format(filename))
tem.show_data()
tem.write_to_txt("{}.txt".format(filename))





