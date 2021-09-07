# IMPORT PACKAGES
import cv2
import numpy as np
# from scipy import optimize
from matplotlib import pyplot as plt

# Function to get and print frame info
def getVideoInfo(vidObj):
    # Create a new dictionary
    vidInfo = dict()
    # Get info on the video
    vidInfo['frame_width'] = int(vidObj.get(3))
    vidInfo['frame_height'] = int(vidObj.get(4))
    vidInfo['length'] = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    vidInfo['fps']    = vidObj.get(cv2.CAP_PROP_FPS)
    return vidInfo

# Function to handle user inputted data
def handleData(vidObj, calc_freqs, time_arr, input_arr):
    if calc_freqs == True:
        # HANDLE DATA
        vidInfo = getVideoInfo(vidObj)

        # create time / input arrays only including inputted data points
        time_arr_new = []
        input_arr_new = []
        for i in range(len(input_arr)):
            if input_arr[i] != 0:
                time_arr_new.append(time_arr[i])
                input_arr_new.append(input_arr[i])

        # FREQUENCIES
        FT = np.fft.fft(input_arr) / len(input_arr) # FFT with normalized amplitude
        FT = FT[range(int(len(input_arr) / 2))]
        values = np.arange(int(len(input_arr) / 2))
        timePeriod = len(input_arr) / vidInfo['fps']
        freqs = values / timePeriod

        # -----------------------------------------------------------

        # Plots
        fig, (ax1, ax2) = plt.subplots(2)
        # plot original input data
        ax1.plot(time_arr_new, input_arr_new, 'b-', label='Original data')
        ax1.set(title = 'Time History of User Inputted Events',
                xlabel = 'time (s)',
                ylabel = 'recorded events')

        ax2.loglog(freqs, abs(FT), 'r-')
        # plot FT of data
        ax2.set(title = 'Fourier Transform',
                xlabel = 'freqs (hz)',
                ylabel = 'amp')

        plt.show()
    else:
        return False