import numpy as np  
import scipy as sp  
from scipy.io.wavfile import read  
from scipy.io.wavfile import write     
from scipy import signal  


(Fvz, array) = read('input.wav')  

len(array)  

FourierTransformation = sp.fft(array)  

scale = sp.linspace(0, Fvz, len(array))  

GuassianNoise = np.random.rand(len(FourierTransformation))  


NewSound = GuassianNoise + array  

b,a = signal.butter(5, 1000/(Fvz/2), btype='highpass')  

filteredSignal = signal.lfilter(b, a, NewSound)  


c,d = signal.butter(5, 380/(Fvz/2), btype='lowpass') # ButterWorth low-filter  

newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal  

write("zvonjenje.wav", Fvz, np.int16(newFilteredSignal/np.max(np.abs(newFilteredSignal)) * 32767))
