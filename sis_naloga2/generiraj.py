import numpy as np


def generiraj_ton_mono(cas, vzorcevalna_frekvenca, bitna_locljivost, frekvenca_tona):
    MAX = (pow(2, bitna_locljivost) / 2 - 1)
    MIN = (pow(2, bitna_locljivost) / 2 )

    #if np.issubdtype(MAX, np.int8): #& isinstance(MIN, np.uint8):
     #   type = "int8"
   # elif np.issubdtype(MAX, np.int16):# & isinstance(MIN, np.uint16):
    #    type = "int16"
    #elif np.issubdtype(MAX, np.int32):# & isinstance(MIN, np.uint32):
    #    type = "int32"
   # else:
     #   type = "int64"  

    if MAX < 128 and MIN >= -128:
        type = 'int8'
    elif MAX < 32768 and MIN >= -32768:
        type = 'int16'
    elif MAX < 2147483648 and MIN >= -2147483648:
        type = 'int32'
    else:
        type = 'int64'

    t = np.arange(0, cas * vzorcevalna_frekvenca, 1, dtype=type) / vzorcevalna_frekvenca # vektor časovnih indeksov

    s1 = MAX * np.sin(2 * np.pi * frekvenca_tona * t)

    signal = np.zeros((len(s1), 1))
    signal = signal.astype(type)

    i = 0
    while i < len(s1):
        signal[i] = s1[i]
        i += 1



    return signal

if __name__ == '__main__':
    print(generiraj_ton_mono(1, 10, 8, 5))