# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:00:11 2023

@author: Isinsu
"""
import cv2
import numpy as np
import glob,os
import tkinter as tk
from tkinter import *

import time, datetime
from urllib.request import urlopen
from pathlib import Path
from skimage.filters import threshold_local

from PIL import ImageTk
import PIL
from PIL import ImageDraw, ImageFont
from PIL import Image


# GUI
window = Tk()
window.configure(background="white")
window.title("Document Scanner")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')
window.iconbitmap('./meta_data/icon.png')
window.resizable(0, 0)
launch = False
w = 400 ;h = 600
size = (w, h)
# window.mainloop()

def open_cam():
    url = entry_text.get() 
    capture_button= tk.Button(window,text="Capture Image",bg= "pink",width=20,
                              height=2, font=('times',20,'italic bold'),activebackground='purple')
    capture_button.place(x=50,y=600)
    
    pdf_img = PIL.Image.open('./meta_data/pdf.png')
    pdf_img = pdf_img.resize((130, 80),PIL.Image.ANTIALIAS)
    pdf_img = ImageTk.PhotoImage(pdf_img)
    
    button_pdf_img = Button(window, borderwidth=0, command=pdf_generator, image=pdf_img, bg='white')
    button_pdf_img.pack()
    button_pdf_img.image = pdf_img
    button_pdf_img.place(x=700, y=15)


def crop_img():
    pass


def pdf_generator():
    pass


label_url = tk.Label(window,text="Enter your URL: ",width=15,height=1,fg="purple",bg="white",font=('arial',15))
label_url.place(x=20,y=20)

entry_text = tk.Entry(window,width=30,fg="black",bg="white",font=('arial',15,'bold'))
entry_text.place(x=180,y=20)
entry_text.insert(0,'http://192.168.1.1:8080/pic.jpg')

button_turn = tk.Button(window,text='Turn on',bg='purple',fg='white',width=10,
                        height=1,font=('arial',15),command=open_cam,activebackground='pink')
button_turn.place(x=520,y=15)

window.mainloop()
