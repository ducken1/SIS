from turtle import position
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

def RGB_hist(slika):
    neke = np.array(slika)
    #width, height = neke.shape

    r = np.zeros(256).reshape(256,1)
    g = np.zeros(256).reshape(256,1)
    b = np.zeros(256).reshape(256,1)

    hist = np.zeros(neke.shape, dtype='uint8')
    for i in range(0, neke.shape[1]):
        for j in range(0, neke.shape[0]):
            r[slika[j][i][0]] = r[slika[j][i][0]] + 1
            g[slika[j][i][1]] = g[slika[j][i][1]] + 1
            b[slika[j][i][2]] = b[slika[j][i][2]] + 1

    hist = np.column_stack((r,g,b))
    return hist

def GRAY_hist(slika):
    neke = np.array(slika)
   
    hist = np.zeros((256, 1), dtype='uint8')
    for i in range(0, neke.shape[0]):
        for j in range(0, neke.shape[1]):
            hist[neke[i][j]] = hist[neke[i][j]] + 1

    return hist

if __name__ == '__main__':
    print("Modul za izdelavo histograma slike")
