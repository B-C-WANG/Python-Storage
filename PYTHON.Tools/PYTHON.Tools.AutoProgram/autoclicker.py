#-*- coding: UTF-8 -*-
from PyQt5 import QtWidgets,QtCore
from autoclicker import Ui_MainWindow
import sys
import os
import time
import win32gui
import win32api
import win32con
from ctypes import *
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QFileDialog
VK_CODE = {
  'backspace':0x08,
  'tab':0x09,
  'clear':0x0C,
  'enter':0x0D,
  'shift':0x10,
  'ctrl':0x11,
  'alt':0x12,
  'pause':0x13,
  'caps_lock':0x14,
  'esc':0x1B,
  'spacebar':0x20,
  'page_up':0x21,
  'page_down':0x22,
  'end':0x23,
  'home':0x24,
  'left_arrow':0x25,
  'up_arrow':0x26,
  'right_arrow':0x27,
  'down_arrow':0x28,
  'select':0x29,
  'print':0x2A,
  'execute':0x2B,
  'print_screen':0x2C,
  'ins':0x2D,
  'del':0x2E,
  'help':0x2F,
  '0':0x30,
  '1':0x31,
  '2':0x32,
  '3':0x33,
  '4':0x34,
  '5':0x35,
  '6':0x36,
  '7':0x37,
  '8':0x38,
  '9':0x39,
  'a':0x41,
  'b':0x42,
  'c':0x43,
  'd':0x44,
  'e':0x45,
  'f':0x46,
  'g':0x47,
  'h':0x48,
  'i':0x49,
  'j':0x4A,
  'k':0x4B,
  'l':0x4C,
  'm':0x4D,
  'n':0x4E,
  'o':0x4F,
  'p':0x50,
  'q':0x51,
  'r':0x52,
  's':0x53,
  't':0x54,
  'u':0x55,
  'v':0x56,
  'w':0x57,
  'x':0x58,
  'y':0x59,
  'z':0x5A,
  'numpad_0':0x60,
  'numpad_1':0x61,
  'numpad_2':0x62,
  'numpad_3':0x63,
  'numpad_4':0x64,
  'numpad_5':0x65,
  'numpad_6':0x66,
  'numpad_7':0x67,
  'numpad_8':0x68,
  'numpad_9':0x69,
  'multiply_key':0x6A,
  'add_key':0x6B,
  'separator_key':0x6C,
  'subtract_key':0x6D,
  'decimal_key':0x6E,
  'divide_key':0x6F,
  'F1':0x70,
  'F2':0x71,
  'F3':0x72,
  'F4':0x73,
  'F5':0x74,
  'F6':0x75,
  'F7':0x76,
  'F8':0x77,
  'F9':0x78,
  'F10':0x79,
  'F11':0x7A,
  'F12':0x7B,
  'F13':0x7C,
  'F14':0x7D,
  'F15':0x7E,
  'F16':0x7F,
  'F17':0x80,
  'F18':0x81,
  'F19':0x82,
  'F20':0x83,
  'F21':0x84,
  'F22':0x85,
  'F23':0x86,
  'F24':0x87,
  'num_lock':0x90,
  'scroll_lock':0x91,
  'left_shift':0xA0,
  'right_shift ':0xA1,
  'left_control':0xA2,
  'right_control':0xA3,
  'left_menu':0xA4,
  'right_menu':0xA5,
  'browser_back':0xA6,
  'browser_forward':0xA7,
  'browser_refresh':0xA8,
  'browser_stop':0xA9,
  'browser_search':0xAA,
  'browser_favorites':0xAB,
  'browser_start_and_home':0xAC,
  'volume_mute':0xAD,
  'volume_Down':0xAE,
  'volume_up':0xAF,
  'next_track':0xB0,
  'previous_track':0xB1,
  'stop_media':0xB2,
  'play/pause_media':0xB3,
  'start_mail':0xB4,
  'select_media':0xB5,
  'start_application_1':0xB6,
  'start_application_2':0xB7,
  'attn_key':0xF6,
  'crsel_key':0xF7,
  'exsel_key':0xF8,
  'play_key':0xFA,
  'zoom_key':0xFB,
  'clear_key':0xFE,
  '+':0xBB,
  ',':0xBC,
  '-':0xBD,
  '.':0xBE,
  '/':0xBF,
  '`':0xC0,
  ';':0xBA,
  '[':0xDB,
  '\\':0xDC,
  ']':0xDD,
  "'":0xDE,
  '`':0xC0}
class POINT(Structure):
  _fields_ = [("x", c_ulong),("y", c_ulong)]
def mouse_move(x,y):
  windll.user32.SetCursorPos(x, y)
def get_mouse_point():
  po = POINT()
  windll.user32.GetCursorPos(byref(po))
  return int(po.x), int(po.y)
def mouse_click(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_dclick(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def key_input(str=''):
  for c in str:

    win32api.keybd_event(VK_CODE[c],0,0,0)
    win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)

def keys(c):

  win32api.keybd_event(VK_CODE[c], 0, 0, 0)
  win32api.keybd_event(VK_CODE[c], 0, win32con.KEYEVENTF_KEYUP, 0)


def mouse_down(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
def mouse_up(x=None,y=None):
  if not x is None and not y is None:
    mouse_move(x,y)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


class mysignal(QtWidgets.QWidget,Ui_MainWindow):
    _signal=QtCore.pyqtSignal()

    def __init__(self):
      super(mysignal,self).__init__()
      self.setupUi(self)
      a1 = []
      global a1
      self.getkeyposition.clicked.connect(self.getp1)
      self.click.clicked.connect(self.click1)
      self.doubleclick.clicked.connect(self.dclick1)
      self.run.clicked.connect(self.run1)
      self.timesleep.clicked.connect(self.timess)
      self.hold.clicked.connect(self.down1)
      self.release.clicked.connect(self.up1)
      self.processclear.clicked.connect(self.clear1)
      self.ctrlz.clicked.connect(self.ctrlz1)
      self.keyinsert.clicked.connect(self.key11)
      self.keyinsert1.clicked.connect(self.key12)
      self.importfs.clicked.connect(self.import1)
      self.save.clicked.connect(self.save1)

    def import1(self):
        try:
          file, name = QFileDialog.getOpenFileName(self, ('需要读取的文件'),
                                                   ('D:/*.ksf'),
                                                   ('*.ksf;;'), None)
          file_object = open(file)

          a1 = file_object.readlines()
          stra1 = ('\n').join(a1)  # join是加入全部的a1，所以删去a1就够了
          self.process.setText(stra1)
          global a1, stra1
          file_object.close()
        except:
          print('')


    def save1(self):
      try:
        file, name = QFileDialog.getSaveFileName(self, ('需要读取的文件'),
                                                  ('D:/.ksf'),
                                                  ('*.ksf'), None)
        file_object = open(file, 'w')
        file_object.write(stra1)
        file_object.close()
      except:
        print('')

    def key12(self):
      keyg = self.key2.text()
      try:
        keys(keyg)
        a1 += ['''keys('{}')'''.format(keyg)]
        stra1 = ('\n').join(a1)
        self.process.setText(stra1)
        global a1, stra1
      except:
        a = QMessageBox.information(self, ('提示'), ('请输入一个功能键，全小写，如‘enter’，‘shift’等。'), QMessageBox.StandardButtons(QMessageBox.Ok))



    def key11(self):

      keyg=self.key1.text()
      if keyg!='':
            a1 += ['''key_input('{}')'''.format(keyg)]
            stra1 = ('\n').join(a1)
            self.process.setText(stra1)
            global a1, stra1


    def ctrlz1(self):
      if a1==[]:
        a = QMessageBox.information(self, ('提示'), ('无进程可供撤销。'), QMessageBox.StandardButtons(QMessageBox.Ok))
      else:
        a1.pop()#删去最后一个list
        stra1 = ('\n').join(a1)#join是加入全部的a1，所以删去a1就够了
        self.process.setText(stra1)
        global a1, stra1
    def clear1(self):
      a1=[]
      global a1
    def up1(self):
      a1 += ['mouse_up{}'.format(gmp)]
      stra1 = ('\n').join(a1)
      self.process.setText(stra1)
      global a1, stra1
    def down1(self):
      a1 += ['mouse_down{}'.format(gmp)]
      stra1 = ('\n').join(a1)
      self.process.setText(stra1)
      global a1, stra1
    def timess(self):
      time1 = self.times.text()
      try:
        time2=float(time1)#这里是：如果输入能变成int，就有效，执行下面的，否则显示对话框
        a1 += ['time.sleep({})'.format(time2)]
        stra1 = ('\n').join(a1)#加回车以便显示
        self.process.setText(stra1)
        global a1, stra1
      except:
        a = QMessageBox.information(self, ('提示'), ('请输入一个数字。'),QMessageBox.StandardButtons(QMessageBox.Ok))

    def getp1(self):
      time.sleep(2)
      gmp =get_mouse_point()
      self.mouseposition.setText(str(gmp))
      global gmp
    def click1(self):
      a1+=['mouse_click{}'.format(gmp)]
      stra1 = ('\n').join(a1)
      self.process.setText(stra1)
      global a1,stra1
    def dclick1(self):
      a1+=['mouse_dclick{}'.format(gmp)]
      stra1 = ('\n').join(a1)
      self.process.setText(stra1)
      global a1
    def run1(self):
      j=self.runt.text()#get循环次数
      try:
        j1=int(j)#这里是：如果输入能变成int，就有效，执行下面的，否则显示对话框

        for i in range(j1):
          for k in a1:
            exec(k)
      except:
        a = QMessageBox.information(self, ('提示'), ('出现错误，请检查输入。'),QMessageBox.StandardButtons(QMessageBox.Ok))


#2016年10月22日
#记住，要声明变量，要多尝试，最终发现了在click等语句后的函数中声明全局变量时，就在__init__这个函数中声明变量
#下一步：要设置run的时间间隔，开始进行按键等的设计
#bug：点了清空之后实质上并没有把a1归零


#如果要debug某个代码，就把他复制到__init__这个函数中，否者后面不会告诉你出错在哪里


#mouse 的函数参数可以改一下，因为有timesleep



#键盘按键不加时间间隔，是否可认为同时按键？

#进制的检查也很重要，print要经常用


#后续增加高级功能：连续打开txt文件















if __name__ =='__main__':

    app=QtWidgets.QApplication(sys.argv)
    myshow=mysignal()
    myshow.show()
    sys.exit(app.exec())
