import numpy as np
def analiziraj_vzorcevalno_mono(signal, dominantna_frekvenca):
    fft_signal = np.fft.fft(signal, axis=0)

    dolzina = fft_signal.shape[0]

    abs = np.argmax(fft_signal)
    #print(abs)
    Fvz = dominantna_frekvenca / (abs / dolzina)
    #print(Fvz)
    return Fvz

if __name__ == '__main__':
    import numpy as np
    t = np.arange(0, 1 * 250, 1) / 250
    sig = 1 * np.sin(2 * np.pi * 7 * t + 0 * np.pi)
    sig.shape = (-1, 1)
    analiza = analiziraj_vzorcevalno_mono(sig, 7)
    print(analiza)