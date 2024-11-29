import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

def RGB_v_HSV(slika):
    #slika = plt.imread(slika)
    #slika = Image.open(slika)
   # H = slika.height
    #W = slika.width
    #nekaj = np.array(slika)
    #nekaj = np.reshape(nekaj, (H, W, 3)).astype(np.uint8)  
    neke = np.array(slika)
    h, w, c = neke.shape

    #maxv = np.amax(neke, axis=2)
    #maxc = np.argmax(neke, axis=2)
    #minv = np.amin(neke, axis=2)
    #minc = np.argmin(neke, axis=2)

    hsv = np.zeros(neke.shape, dtype='uint8')
    for i in range(h):
        for j in range(w):
            r = neke[i, j, 0] / 255
            g = neke[i, j, 1] / 255
            b = neke[i, j, 2] / 255

            value = max(r, g, b)
            chroma = value - min(r, g, b)
            saturation = 0 if value == 0 else (chroma / value)*255

            if chroma == 0:
                hue = 0
            elif value == r:
                hue = 60 * (0 + (g - b) / chroma)
            elif value == g:
                hue = 60 * (2 + (b - r) / chroma)
            else:
                hue = 60 * (4 + (r - g) / chroma)

            if (hue < 0):
                hue = hue + 360
            h = hue / 2
            s = saturation
            v = value * 255
    
    
    
    #hsv[maxc == minc, 0] = np.zeros(hsv[maxc == minc, 0].shape)
    #hsv[maxc == 0, 0] = (((neke[..., 1] - neke[..., 2]) * 60.0 / (maxv - minv + np.spacing(1))) % 360.0)[maxc == 0]
    #hsv[maxc == 1, 0] = (((neke[..., 2] - neke[..., 0]) * 60.0 / (maxv - minv + np.spacing(1))) + 120.0)[maxc == 1]
    #hsv[maxc == 2, 0] = (((neke[..., 0] - neke[..., 1]) * 60.0 / (maxv - minv + np.spacing(1))) + 240.0)[maxc == 2]
    #hsv[maxv == 0, 1] = np.zeros(hsv[maxv == 0, 1].shape)
   # hsv[maxv != 0, 1] = (1 - minv / (maxv + np.spacing(1)))[maxv != 0]
    #hsv[..., 2] = maxv

            hsv[i, j, 0] = math.trunc(h)
            hsv[i, j, 1] = math.trunc(s)
            hsv[i, j, 2] = math.trunc(v)

    return hsv

def HSV_v_RGB(slika):
    neke = np.array(slika)
    height, width, c = neke.shape

    rgb = np.zeros(neke.shape, dtype='uint8')
    for i in range(height):
        for j in range(width):
            h = neke[i, j, 0] * 2
            s = neke[i, j, 1] / 255
            v = neke[i, j, 2] / 255

            chroma = v * s
            h_section = h / 60
            druga_najvecja = chroma * (1 - abs(h_section % 2 - 1))
            ujemajoce = v - chroma

            if h_section >= 0 and h_section <= 1:
                r = round(255 * (chroma + ujemajoce))
                g = round(255 * (druga_najvecja + ujemajoce))
                b = round(255 * (ujemajoce))
            elif h_section > 1 and h_section <= 2:
                r = round(255 * (druga_najvecja + ujemajoce))
                g = round(255 * (chroma + ujemajoce))
                b = round(255 * (ujemajoce))
            elif h_section > 2 and h_section <= 3:
                r = round(255 * (ujemajoce))
                g = round(255 * (chroma + ujemajoce))
                b = round(255 * (druga_najvecja + ujemajoce))
            elif h_section > 3 and h_section <= 4:
                r = round(255 * (ujemajoce))
                g = round(255 * (druga_najvecja + ujemajoce))
                b = round(255 * (chroma + ujemajoce))
            elif h_section > 4 and h_section <= 5:
                r = round(255 * (druga_najvecja + ujemajoce))
                g = round(255 * (ujemajoce))
                b = round(255 * (chroma + ujemajoce))
            else:
                r = round(255 * (chroma + ujemajoce))
                g = round(255 * (ujemajoce))
                b = round(255 * (druga_najvecja + ujemajoce))

            rgb[i, j, 0] = math.trunc(r)
            rgb[i, j, 1] = math.trunc(g)
            rgb[i, j, 2] = math.trunc(b)

    return rgb

def RGB_v_YCbCr(slika):
    neke = np.array(slika)
    height, width, c = neke.shape

    ycbcr = np.zeros(neke.shape, dtype='uint8')
    for i in range(height):
        for j in range(width):
            r = neke[i, j, 0]
            g = neke[i, j, 1]
            b = neke[i, j, 2]

            ycbcr[i, j, 0] = math.trunc(.299 * r + .587 * g + .114 * b)
            ycbcr[i, j, 1] = math.trunc(128 - .168736 * r - .331264 * g + .5 * b)
            ycbcr[i, j, 2] = math.trunc(128 + .5 * r - .418688 * g - .081312 * b)


    return ycbcr

def YCbCr_v_RGB(slika):
    neke = np.array(slika)
    height, width, c = neke.shape

    rgb = np.zeros(neke.shape, dtype='uint8')
    for i in range(height):
        for j in range(width):
            y = neke[i, j, 0]
            cb = neke[i, j, 1]# - 128
            cr = neke[i, j, 2]# - 128

            rgb[i, j, 0] = min(max(0, round(y + 1.402 * (cr - 128))), 255)
            rgb[i, j, 1] = min(max(0, round(y - 0.3441 * (cb - 128) - 0.714 * (cr - 128))), 255)
            rgb[i, j, 2] = min(max(0, round(y + 1.772 * (cb - 128))), 255)

    return rgb

if __name__ == '__main__':
    print("Modul za pretvorbo barvnih prostorov!")