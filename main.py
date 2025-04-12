# This script is used to design a low-pass FIR filter, and then to convert it in a HDL code for FPGA implementation.

#importing libraries
import matplotlib.pyplot as plt
import numpy as np 
import scipy.signal as signal
import argparse
import config
import os

# folder to save the results 
folder_name = "/home/papaple/2025_04_12_FIR_filter/results"

parser = argparse.ArgumentParser(description = "Take the settings to generate and convert the FIR filter")
args = config.get_args(parser)

if args.filter_type == "LPF":
    taps_coeffs = signal.firwin(args.number_of_taps, args.cut_off_freq_1)
elif args.filter_type == "BPF":
    taps_coeffs = signal.firwin(args.number_of_taps, [args.cut_off_freq_1, args.cut_off_freq_2], pass_zero = False)
elif args.filter_type == "HPF":
    taps_coeffs = signal.firwin(args.number_of_taps, args.cut_off_freq_1, pass_zero = False)
else: print(f"please, select one of type of filter among LPF, BPF, HPF")

w, h = signal.freqz(taps_coeffs)

plt.title("The frequency response of the FIR filter, the frequency is normalized to 1")
plt.plot(w,20*np.log10(np.abs(h)),'b')
plt.ylabel("Amplitude Response (dB)")
plt.xlabel("Normalized frequency")
plt.grid()
save_path = os.path.join(folder_name, f'FIR_filter_response.png')
plt.savefig(save_path)
plt.close()



