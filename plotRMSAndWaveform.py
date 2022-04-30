import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import IPython.display as ipd
import argparse

parser = argparse.ArgumentParser(description="Plotting RMS and waveform of a .wav file")
parser.add_argument('--path',type=str,metavar='',required=True,help='Path to .wav file')
parser.add_argument('-f','--frame',metavar='',required=False,help='Frame length, if not entered, default is 1024')
parser.add_argument('-H','--hop',metavar='',required=False,help='Hope length, if not entered, default is 512')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='print quiet')
group.add_argument('-v','--verbose',action='store_true',help='print verbose')
args = parser.parse_args()

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
	plt.ylabel("Magnitude (dB)")
	plt.title("rms")
	plt.show()

if __name__ == '__main__':

	if args.frame:
		Frame_Length=int (args.frame)
	else:
		Frame_Length=1024
	if args.hop:
		Hop_Length=int(args.hop)
	else:
		Hop_Length= 512
	if args.quiet:
		plotRMSAndWaveform(args.path, Frame_Length, Hop_Length)
	elif args.verbose:
		print (f"\nPlot of .wav file with frame length {Frame_Length} and hop length {Hop_Length} should now be open in a different window\n")
		plotRMSAndWaveform(args.path, Frame_Length, Hop_Length)
	else:
		print ("\nYou should now see plot on a different window\n")
		plotRMSAndWaveform(args.path, Frame_Length, Hop_Length)