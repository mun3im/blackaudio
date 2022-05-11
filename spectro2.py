#import the pyplot and wavfile modules 

import matplotlib.pyplot as plot
from scipy.io import wavfile

# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read('tuwu.wav')
 
# Plot the signal read from wav file

plot.subplot(211)
plot.title('Spectrogram of a wav file of Asian koel')
plot.plot(signalData)
plot.xlabel('Sample')
plot.ylabel('Amplitude')

plot.subplot(212)
plot.specgram(signalData,Fs=samplingFrequency, cmap='Blues')
plot.xlabel('Time')
plot.ylabel('Frequency')

plot.show()