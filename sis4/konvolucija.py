import numpy as np

def normaliziraj_vektorsko(vektor):
    return vektor / np.max(np.abs(vektor))

def konv_frekvenca_mono(signal, impulz):

    X = np.fft.fft(signal, n=signal.shape[0]+impulz.shape[0]-1, axis=0)
    H = np.fft.fft(impulz, n=signal.shape[0]+impulz.shape[0]-1, axis=0)

    Y = X*H

    dolzina = signal.shape[0] + impulz.shape[0] - 1

    y2 = np.zeros((dolzina, 2))
    # inverzna fourierova transformacija rekonstruira originalni signal 
    # pri tem je običajno potrebno vzeti samo realni del (tudi ta funkcija vrne kompleksna števila)
    y2 = np.real(np.fft.ifft(Y, axis=0))
    y2 = np.reshape(y2, (-1, 1))
    y2 = normaliziraj_vektorsko(y2)
    return y2

def konv_frekvenca_stereo(signal, impulz):

    X = np.fft.fft(signal, n=signal.shape[0]+impulz.shape[0]-1, axis=0)
    H = np.fft.fft(impulz, n=signal.shape[0]+impulz.shape[0]-1, axis=0)

    Y = X*H

    dolzina = signal.shape[0] + impulz.shape[0] - 1

    y2 = np.zeros((dolzina, 2))
    # inverzna fourierova transformacija rekonstruira originalni signal 
    # pri tem je običajno potrebno vzeti samo realni del (tudi ta funkcija vrne kompleksna števila)
    y2 = np.real(np.fft.ifft(Y, axis=0))
    y2 = np.reshape(y2, (-1, 2))
    y2 = normaliziraj_vektorsko(y2)
    return y2

if __name__ == '__main__':
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    h = np.array([1,2,1])
    x = normaliziraj_vektorsko(x)
    h = normaliziraj_vektorsko(h)
    a = konv_frekvenca_mono(x,h)

    print(x,"\n","\n", h, "\n","\n", a)

    x1 = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [13,14], [15,16], [17,18], [19,20]])
    h1 = np.array([[1,2],[2,1], [1,2]])
    x1 = normaliziraj_vektorsko(x1)
    h1 = normaliziraj_vektorsko(h1)
    b = konv_frekvenca_stereo(x1,h1)

    print(x1,"\n","\n", h1, "\n","\n", b)
