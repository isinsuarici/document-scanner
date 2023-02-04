# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 03:00:11 2023

@author: Isinsu
"""
import cv2

def main():
    img = cv2.imread("C:/Users/Isinsu/Desktop/PROJECTS/document-scanner/imgs/img1.png",0)
    while True:
        cv2.imshow('img', img)
        if cv2.waitKey(20) & 0xFF == 27:  # press esc to exit
            break
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()

