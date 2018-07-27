import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fftpack import fft
from scipy.io import wavfile

T = []

#Discrete Fourier Transform
def myOwnDFT(input):
    start = time.time() #Times how long it takes to iterate through the code
    output = []
    N = len(input)
    for n in np.arange(N):
        U = 0
        for k in np.arange(N):
           angle = (1j*2*np.pi*(k)*(n)/N)
           U += input[k] *np.exp(-angle)
        output = np.append(output,U)
        output = np.absolute(output)
    end = time.time()
    T.append(end - start)
    return (output)

if __name__ == '__main__':
    InputSin = 1000+200
    for i in range(200,InputSin,200):
        t = np.linspace(0,1,i)
        Sin10Hz = np.sin(2 * np.pi * 10 * t)
        lengthOfSin = np.arange(len(Sin10Hz))
        DFT10Hz = myOwnDFT(Sin10Hz)

		# Plots
        fig = plt.figure()
        fig.suptitle('myOwnDFT, size ' + str(i) , fontsize = 16)
        x = plt.subplot(11,1,1)
        x.set_title("10Hz")
        plt.plot(lengthOfSin, DFT10Hz)

        x = plt.subplot(11,1,6)
        x.set_title("20Hz")
        Sin20Hz = np.sin(2 * np.pi * 20 * t)
        DFT20Hz = myOwnDFT(Sin20Hz)
        plt.plot(lengthOfSin, DFT20Hz)

        x = plt.subplot(11,1,11)
        x.set_title("30Hz")
        Sin30Hz = np.sin(2 * np.pi * 30 * t)
        DFT30Hz = myOwnDFT(Sin30Hz)
        plt.plot(lengthOfSin, DFT30Hz)

	# Plot times
    print(T)
    print(len(T))
    timePlot = plt.figure()
    timePlot.suptitle("Time")
    timeList = np.linspace(0, 14, len(T))
    plt.stem(timeList, T, ':')
    plt.xlabel("Iteration")
    plt.ylabel("Time it takes to complete (s)")

    #Plot Wav File
    wavPlot = plt.figure()
    wavPlot.suptitle("WavFile")
    # Wav file time
    fs, wavdata = wavfile.read("kpt.wav")
    wavDFT = myOwnDFT(wavdata)
    timed = len(wavdata)/fs
    r = np.arange(len(wavdata))
    freqLabel = r/timed
    plt.plot(freqLabel, wavDFT)
    plt.show()
