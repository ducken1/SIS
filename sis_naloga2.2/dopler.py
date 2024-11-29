import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
import warnings
warnings.filterwarnings('ignore')

def normaliziraj(vektor):
    return vektor / np.max(np.abs(vektor))          #v pomoc je bila stran https://www.fridh.nl/2015/02/01/auralization-doppler-effect/

def interpolacija(vektor, times, vektor_fvz):

    k_r = np.arange(0, len(vektor), 1) #vektor indikatorjev - merjenih enot
   # k = np.zeros((len(vektor)*2))

   # times = times.reshape((len(times)*2,))
    #test = (times * vektor_fvz)
   # k = np.zeros((len(vektor)*2),)
    k = k_r - times * vektor_fvz

    kf = np.floor(k).astype(int)  #zaokrozi navzdol v obliki int

    R = ( (1.0-k+kf) * vektor[kf] + (k-kf) * vektor[kf+1] ) * (kf >= 0) #pomojem to poskrbi, da je zvok prihajajoc in odhajajoc torej Dopplerjev pojav

    return R

def dopler_efekt_mono(vektor, vektor_fvz, zacetna_oddaljenost, hitrost):
    dolzina = ((zacetna_oddaljenost * 2) / hitrost) 

    samples = int(vektor_fvz * dolzina)
    times = np.arange(samples) / vektor_fvz

    vektor = np.sin(2.0*np.pi * 5000 * times)

    x = times * hitrost                         #v tej funkciji podanemu zvoku spremenimo cas ter zvok pozicionalno prirejamo s podanim soundspeed
    x -= x.max()/2.0                            #nato podamo nove vrednosti ter priredbe v fukcijo interpolacija kjer nam dokonca dopplerjev efekt
    y = np.zeros(samples)
    z = 100.0 * np.ones(samples)

    position_source = np.vstack((x,y,z)).T
    position_receiver = np.zeros(3)

    distance = np.linalg.norm((position_source - position_receiver), axis=-1)
    soundspeed = 343.0 #recimo da je to konstanta hitrosti zvoka

    delay = distance / soundspeed
    delayed_linear = interpolacija(vektor, delay, vektor_fvz)
    delayed_linear = np.reshape(delayed_linear, (-1,1))

    return normaliziraj(delayed_linear) #normalizacija sicer ni potrebna ker so vse vrednosti med 1 in 0 oz 1 in -1


if __name__ == '__main__':
    import sounddevice as sd
    t = np.arange(int(44100)*2) / 44100 # vektor časovnih indeksov
    signal = np.sin(2.0 * np.pi * 5000 * t)
    
    #sd.play(signal, 44100)

    DopplerSignal = dopler_efekt_mono(signal, 44100, 100, 25)
    sd.play(DopplerSignal)