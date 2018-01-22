from tkinter import *

from buttonolx import MyButton
from exitbuton import MyButtonExit
from labelclass import LabelClass
from newwindow import NewWindow
from dialogwindow import DialogWindow

root = Tk()

class MyFrame(Frame):
    def __init__(self, parent=root):
        Frame.__init__(self, parent)
        root.title('Main Window')
        self.make_widgets()

    def make_widgets(self):
        LabelClass(text='Hello Alex Tan!!!', height=3, width=90)
        MyButton().run()
        NewWindow()
        DialogWindow()
        MyButtonExit()

if __name__ == '__main__':
    MyFrame().mainloop()