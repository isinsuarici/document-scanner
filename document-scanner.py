# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:00:11 2023

@author: Isinsu
"""
import cv2
import numpy as np
import glob,os
import thinker as tk
from thinker import *

import time, datetime
from urllib.request import urlopen
from pathlib import Path
from skimage.filters import threshold_local

from PIL import ImageTk
import PIL
from PIL import ImageDraw, ImageFont
from PIL import Image



window = Tk()
window.configure(background="white")
window.title("Document Scanner")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{width}x{height}')

window.resizable(0, 0)
launch = False

w = 400 ;h = 600
size = (w, h)




def main():
    img = cv2.imread("C:/Users/Isinsu/Desktop/PROJECTS/document-scanner/imgs/img1.png",0)
    
    cv2.imshow('img', img)
    
    cv2.waitKey(0)    
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()

