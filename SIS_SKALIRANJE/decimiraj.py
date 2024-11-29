from turtle import position
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

def decimiraj_sliko(slika, faktor, filter, gauss_sigma=None):
    width, height = slika.size

    newHeight = int(height / faktor)
    newWidth = int(width / faktor)

    decimirana_slika = np.zeros((newHeight, newWidth, 3), dtype='uint8')
    for i in range(newWidth):
        for j in range(newHeight):

            r, g, b = slika.getpixel((i*faktor, j*faktor))
           # grayscale = (0.299*r + 0.587*g + 0.114*b)

            decimirana_slika[j, i, 0] = r
            decimirana_slika[j, i, 1] = g
            decimirana_slika[j, i, 2] = b

    return decimirana_slika

   
if __name__ == '__main__':
    print("Modul za skaliranje slike!")
