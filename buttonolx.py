import webbrowser
from tkinter import *

class MyButton(Button):
    def __init__(self, parent=None):
        Button.__init__(self, parent)
        self.pack(side=TOP, expand=YES, fill=BOTH)
        self.url = 'http://olx.com.ua'
        self.config(text='Go to OLX!!!', command=(lambda :self.brouser(self.url)))

    def brouser(self, url):
        webbrowser.open_new(url)