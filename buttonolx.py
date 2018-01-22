import webbrowser
from tkinter import *

class MyButton():
    def __init__(self):
        self.widget = Button()
        self.widget.config(text='Go to OLX!!!', command=(lambda :self.brouser(self.url)))
        self.url = 'http://olx.com.ua'

    def brouser(self, url):
        webbrowser.open_new(url)

    def run(self):
        return self.widget.pack(side=TOP, expand=YES, fill=BOTH)