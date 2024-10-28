import tkinter as tk
from tkinter.ttk import Label
from tkinter import *
from PIL import Image, ImageTk
class developer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('1166x740')
        self.title('Developer')
        self.maxsize(1166, 740)
        self.resizable(width=0, height=0)

        # setbackground
        self.image = Image.open("Photo/dev.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)



#----------------------end team class------------------------#