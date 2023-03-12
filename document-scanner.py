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
    global capture_button, button_pdf_img
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
    
    try:
        if url== '':
            msg= tk.Label(window,text="It is not the correct URL! Please check it.", width=40,height=1,
                          fg='white',bg='red',font=('arial',15))
            msg.place(x=20,y=60)
            window.after(2000,destroy_widget,msg)
        else:
            global disp, imgFrame, button_turnOff, img
            imgFrame = tk.Frame(window)
            imgFrame.place(x=20,y=80)
            
            disp= tk.Label(imgFrame)
            disp.grid()
            
            button_turnOff = tk.Button(window,text='Turn off',bg='pink',fg='white',width=10,
                                    height=1,font=('arial',15),command=destroy_cam,activebackground='purple')
            button_turnOff.place(x=520,y=15)
            
            def show_frame():
                global img
                img_url = urlopen(url)
                img_arr = np.array(bytearray(img_url.read()), dtype=np.uint8)
                frame = cv2.imdecode(img_arr, -1)
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                rgb = cv2.cvtColor(cv2image, cv2.COLOR_RGBA2RGB)
                img = PIL.Image.fromarray(rgb)
                img1 = img.resize(size, PIL.Image.ANTIALIAS)
                imgtk = ImageTk.PhotoImage(image=img1)
                disp.imgtk = imgtk
                disp.configure(image=imgtk)
                disp.after(10, show_frame)
            show_frame()
            
    except Exception as e:
        print(e)
        msg1 = tk.Label(window, text='Connection could not be opened', width=40, height=1, fg="white", 
                        bg="red",font=('arial',15))
        msg1.place(x=20, y=60)
        window.after(2000, destroy_widget, msg1)
        imgFrame.destroy()
        disp.destroy()
        button_turnOff.destroy()
        capture_button.destroy()

def crop_img():
    pass

def destroy_widget(widget):
    widget.destroy()

def destroy_cam():
    imgFrame.destroy()
    disp.destroy()
    button_turnOff.destroy()
    capture_button.destroy()
    
def pdf_generator():
    pass


label_url = tk.Label(window,text="Enter your URL: ",width=15,height=1,fg="purple",bg="white",font=('arial',15))
label_url.place(x=20,y=20)

entry_text = tk.Entry(window,width=30,fg="black",bg="white",font=('arial',15,'bold'))
entry_text.place(x=180,y=20)
entry_text.insert(0,'http://192.168.1.5:8080/shot.jpg')

button_turn = tk.Button(window,text='Turn on',bg='purple',fg='white',width=10,
                        height=1,font=('arial',15),command=open_cam,activebackground='pink')
button_turn.place(x=520,y=15)

window.mainloop()
