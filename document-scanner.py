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

def start_app():
    capture_button= tk.Button(window,text="Capture",bg= "pink",width=20,
                              height=2, font=('times',20,'italic bold'))
    
    capture_button.pack()
    capture_button.place(x=50,y=600)


def crop_img():
    pass


def pdf_generator():
    pass

start_app()
window.mainloop()
