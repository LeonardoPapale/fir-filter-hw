import matplotlib.pyplot as plt 
import numpy as np
import scipy.signal as signal
from scipy.io import savemat
import os
import csv


def save_results(taps_coeffs, folder_name):

    #generate the filter frequency response
    w, h = signal.freqz(taps_coeffs)

    #plot and save the frequency response
    plt.title("The frequency response of the FIR filter, the frequency is normalized to 1")
    plt.plot(w,20*np.log10(np.abs(h)),'b')
    plt.ylabel("Amplitude Response (dB)")
    plt.xlabel("Normalized frequency")
    plt.grid()
    save_path = os.path.join(folder_name, f'FIR_filter_response.png')
    plt.savefig(save_path)
    plt.close()

    np.savetxt(folder_name + "/filter_coefficients.csv", taps_coeffs, delimiter=',')
    mdic = {"taps_coefficients": taps_coeffs, "label":"experiment"}
    savemat(folder_name + "/filter_coefficients.mat", mdic)
    

