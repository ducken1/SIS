import numpy as np

def normaliziraj_vektorsko(vektor):
    return vektor / np.max(np.abs(vektor))

def konv_cas_mono(signal, impulz):
    
    efekt = np.zeros((signal.shape[0] + impulz.shape[0]-1))
    posnetekNorm = normaliziraj_vektorsko(signal)


    for n in np.arange(efekt.shape[0]):
        for k in np.arange(max(n-impulz.shape[0]+1, 0), min(n+1, signal.shape[0])):
            efekt[n] += posnetekNorm[k] * impulz[n-k]

    efekt = np.reshape(efekt,(-1,1))
    return normaliziraj_vektorsko(efekt)

def konv_cas_stereo(signal, impulz):
    efekt = np.zeros((signal.shape[0] + impulz.shape[0]-1, 2))
    posnetekNorm = normaliziraj_vektorsko(signal)

    for n in np.arange(efekt.shape[0]):
        for k in np.arange(max(n-impulz.shape[0]+1, 0), min(n+1, signal.shape[0])):
            efekt[n, 0] += posnetekNorm[k, 0] * impulz[n-k, 0]
            efekt[n, 1] += posnetekNorm[k, 1] * impulz[n-k, 1]
            
    #efekt = np.reshape(efekt,(-1,1))
    return normaliziraj_vektorsko(efekt)

if __name__ == '__main__':
    x = np.array([1,2,3,4,5,6,7,8,9,10])
    h = np.array([1,2,1])
    x = normaliziraj_vektorsko(x)
    h = normaliziraj_vektorsko(h)
    a = konv_cas_mono(x,h)

    print(x,"\n","\n", h, "\n","\n", a)

    x1 = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12], [13,14], [15,16], [17,18], [19,20]])
    h1 = np.array([[1,2],[2,1], [1,2]])
    x1 = normaliziraj_vektorsko(x1)
    h1 = normaliziraj_vektorsko(h1)
    b = konv_cas_stereo(x1,h1)

    print(x1,"\n","\n", h1, "\n","\n", b)

