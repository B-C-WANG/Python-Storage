import cv2
import numpy as np


# opencv中的设置为b,g,r
class ImageMatting():
    def __init__(self):
        print("use load_image(filename=,flags=) to load")





    # **kwargs是以<params_name>=parameter传递参数，这里直接传给cv2除了filename外的其他参数
    def load_image(self,filename,**kwargs):

        self.image = cv2.imread(filename=filename,**kwargs)
        self.image_name = filename#获得传递的参数
        self.image_shape = self.image.shape
        self.gray = (len(self.image_shape) == 2)
        self.display_info()

    """
    通过pixel的颜色值和逻辑选出相应位置，返回一个位置数组，比如原图的(100,200)位置是(255,255,255)，
    select_by_color((255,255,255),("=","=","="))就会返回[(100,200)]
    (100,200,300),(">=","<=","==")就是选出R>=100,G<=200,B==300的像素点的位置
    如果是灰度图，就只有一个值
    """


    #色彩设置有问题，是(b,g,r)而不是(r,g,b)
    def select_position_by_color(self,color,logic):

        if self.gray:# 灰度图
            assert type(color) == int
            assert type(logic) == str


            temp = self._select_position_by_color_filter(color=color,logic=logic,gray=1)
            result = []
            for i in range(len(temp[0])):
                result.append((temp[0][i], temp[1][i]))


        else:
            assert type(color) == tuple
            assert type(color[0]) == int
            assert type(logic) == tuple
            assert type(logic[0]) == str
            #对于每一个进行比较，筛选求交集
            temp1 = self._select_position_by_color_filter(color=color,logic=logic,rgb=0)
            temp2 = self._select_position_by_color_filter(color=color,logic=logic,rgb=1)
            temp3 = self._select_position_by_color_filter(color=color,logic=logic,rgb=2)
            result1,result2,result3 = [],[],[]
            for i in range(len(temp1[0])):
                result1.append((temp1[0][i], temp1[1][i]))
            for i in range(len(temp2[0])):
                result2.append((temp2[0][i], temp2[1][i]))
            for i in range(len(temp3[0])):
                result3.append((temp3[0][i], temp3[1][i]))
            # 取交集
            result = list(set(result1).intersection(set(result2).intersection(set(result3))))

        result = np.array(result)
        return result
    #对于每个点，计算rgb平均值，求得最突出的那个颜色
    def select_position_by_color_average(self,color,scale):
        result = []
        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                a = self.image[i][j]
                #这里要注意rgb值是uint8，最大值为255，所以直接相加是不行的
                #print(type(a[0]))
                a0 = int(a[0])
                a1 = int(a[1])
                a2 = int(a[2])

                if a[color] > ((a0+a1+a2)/3.0)*scale:


                    result.append((i,j))
        return np.array(result)







    def _select_position_by_color_filter(self,color,logic,gray=0,rgb=0):
         if gray:
            if logic == "<":
                return np.where(self.image<color)
            elif logic == "<=":
                return np.where(self.image <= color)
            elif logic == "==":
                return np.where(self.image == color)
            elif logic == ">=":
                return np.where(self.image >= color)
            elif logic == ">":
                return np.where(self.image > color)
         else:
             #按照rgb的序列对应处理
             if logic[rgb] == "<":
                 return np.where(self.image[:,:,rgb] < color[rgb])
             elif logic[rgb] == "<=":
                 return np.where(self.image[:,:,rgb] <= color[rgb])
             elif logic[rgb] == "==":
                 return np.where(self.image[:,:,rgb] == color[rgb])
             elif logic[rgb] == ">=":
                 return np.where(self.image[:,:,rgb] >= color[rgb])
             elif logic[rgb] == ">":
                 return np.where(self.image[:,:,rgb] > color[rgb])












    def select_color_by_position(self,position):
        result = []
        for i in position:
            result.append(self.image[i[0],i[1]])
        return result


    '''
    生成一个矩形区域位置'''
    def get_rectangle_position(self):
        pass

    '''
        根据位置填充颜色，color可以是一个int。一个list，如果是灰度，list是int数组，3通道每个就是(r,g,b)的数组
        ，也可以是一个单独的值，或是三个值，对应rgb
        对象是self_image
        '''
    def replace_color_in_position(self,position_list,color):
        if self.gray:
         if type(color) == int:
            for i in range(position_list.shape[0]):
                self.image[position_list[i][0]][position_list[i][1]] = color
         elif type(color) == list and type(color[0] == int):
            temp1 = len(color)
            for i in range(temp1):
                self.image[position_list[i][0]][position_list[i][1]] = color[i]
         else:
             raise ("color must be an int or its list ")
        else:
            if len(color) == 1:
                for i in range(position_list.shape[0]):
                    self.image[position_list[i][0]][position_list[i][1]] = color
            else:
                temp1 = len(color)
                try:
                    for i in range(temp1):
                        self.image[position_list[i][0]][position_list[i][1]] = color[i]
                except:
                    print("color__len__ is more than position_list__len__")




    def display_info(self):
        print("--------Information--------")
        print("Image name  | ",self.image_name)
        print("Image shape | ",self.image_shape)

    def image_show(self,**kwargs):
        cv2.imshow(winname=self.image_name,mat=self.image)
        cv2.waitKey(0)

    def image_save(self,filename):
        cv2.imwrite(filename,self.image)





#a = ImageMatting()
#a.load_image("stop.jpg")
#a.image_show()


b = ImageMatting()
a = ImageMatting()
b.load_image("stop.jpg",flags=3)
a.load_image("leaves.jpg",flags=3)


#position = b.select_position_by_color((255,255,200),("<=","<=",">="))


# 选出红色最突出的，
position = b.select_position_by_color_average(color=2,scale=1.5)

# 按照这个所选出的位置在另一张图取样
color = a.select_color_by_position(position)




# 将位置上的像素进行取代
b.replace_color_in_position(position,color)

b.image_show()
b.image_save("output.jpg")




