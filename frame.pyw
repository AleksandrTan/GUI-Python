from tkinter import *

from buttonolx import MyButton
from exitbuton import MyButtonExit
from labelclass import LabelClass
from newwindow import NewWindow
from dialogwindow import DialogWindow

root = Tk()

class MyFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        root.title('Main Window')
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        labels = LabelClass(parent=self, text='', height=3, width=90)
        MyButton(parent=self)
        NewWindow(labels, parent=self)
        DialogWindow(parent=self)
        MyButtonExit(parent=self)

if __name__ == '__main__':
    MyFrame(parent=root).mainloop()