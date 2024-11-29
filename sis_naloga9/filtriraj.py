import numpy as np
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
img = 'https://ultralytics.com/images/zidane.jpg'
results = model(img)
results.show()

def normaliziraj_vektorsko(vektor):
    return vektor / np.max(np.abs(vektor))

def has_len(obj):
    return hasattr(obj, '__len__') #preveri ce objektu lahko prestejemo vrednosti

def avektor(n, a, filt_signal): #vektor koeficientov
    vsota = 0

    if(has_len(a)):
        for i in range(1, np.size(a)):
            if(n - i >= 0):
                vsota = vsota + (a[i] * filt_signal[n - i])
    else:
        return 0
    return vsota

def bvektor(n, b, signal):
    vsota = 0

    for i in range(np.size(b)):
        if(n - i >= 0):
            vsota = vsota + (b[i] * signal[n - i])
            
    return vsota

def filtriraj_mono(signal, b, a):
    filt_signal = np.zeros(len(signal))

    if (has_len(a)):
        koeficient = a[0]
    else:
        koeficient = a
    
    if (koeficient == 0):
        koeficient = 1

    for i in range(np.size(signal)):
        filt_signal[i] = (bvektor(i, b, signal) - avektor(i, a, filt_signal)) / koeficient

    return filt_signal.reshape(-1, 1)

def filtriraj_stereo(signal, b, a):
    filt_signal = np.zeros(np.shape(signal))

    if (has_len(a)):
        koeficient = a[0]
    else:
        koeficient = a
    
    if (koeficient == 0):
        koeficient = 1

    for i in range(signal.shape[0]):
        filt_signal[i, 0] = (bvektor(i, b, signal[:, 0]) - avektor(i, a, filt_signal[:, 0])) / koeficient #[:, 0] "slicne" array.. : vzame vse vrste,, ter 0 prvi stolpec
        filt_signal[i, 1] = (bvektor(i, b, signal[:, 1]) - avektor(i, a, filt_signal[:, 1])) / koeficient

    return filt_signal.reshape(-1, 2)

if __name__ == '__main__':
    print("Modul za filtriranje signala!")