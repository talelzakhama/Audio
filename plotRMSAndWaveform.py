import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd

def plotRMSAndWaveform(path,Frame_Length,Hop_Length):
	file,sr=librosa.load (path)
	# Extracting RMSE with Librosa
	rms = librosa.feature.rms(file,frame_length=Frame_Length,hop_length=Hop_Length)[0]
	frames=range(len(rms))
	print (f"frames are {frames}\n")
	t=librosa.frames_to_time(frames,hop_length=Hop_Length)

	plt.figure(figsize=(15, 10))
	librosa.display.waveplot(file, alpha=0.5)
	plt.plot(t, rms, color="r")
	plt.xlabel("Time (s)")
	plt.ylim((-1, 1))
	plt.ylabel("Magnitude (dB)")
	plt.title("rms")
	plt.show()


path="/Users/talelzakhama/Downloads/POLQA-F2-S1-48k.wav"
Frame_Length=1024
Hop_Length=512
plotRMSAndWaveform(path, Frame_Length, Hop_Length)