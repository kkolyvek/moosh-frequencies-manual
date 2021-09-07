# IMPORT PACKAGES
import cv2
import numpy as np
from scipy.optimize import leastsq
from matplotlib import pyplot as plt

# IMPORT METHODS
from helpers import getVideoInfo

# METHOD
# ------------------------------------------------------

def vidAnalysis(vidObj):
    """
    Function for semi-manual calculation of tail beat frequencies.

    Plays video and listens for keystrokes that indicate the start of
    a calculation segment, occurence of a key event, and the end of a 
    calculation segment.
    """

    # video windows
    cv2.namedWindow('vid', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('vid', 1920, 1080)

    # States
    listening = False # toggle recording
    calc_freqs = False # toggle graceful / ungraceful exit
    frame_counter = 0 # time series array
    # first recorded keystroke is positive
    input_val = 1

    # Data init
    time_arr = []
    input_arr = []

    while (True):
        ret, frame = vidObj.read()


        if ret == True:
            cv2.imshow('vid', frame)

            key = cv2.waitKey(1)

            if listening == True:
                time_arr.append(frame_counter)
                frame_counter += 1

            # Keystroke listeners
            # ==============================================================

            # Press Q to quit
            if key == ord('q'):
                break

            # Press I to begin a calculation segment
            if key == ord('i'):
                print('listening')
                listening = True

                # manually add first item
                time_arr.append(frame_counter)
                frame_counter += 1

            # Press O to store a keystroke frame
            if listening == True:
                if key == ord('o'):
                    input_arr.append(input_val)
                    input_val *= -1
                else:
                    input_arr.append(0)

            # Press P to end calculation segment and video
            if key == ord('p'):
                print('end segment')
                calc_freqs = True
                break

            # ==============================================================

        # Break loop at error or end of vid
        else:
            print('Read error or end of video.')
            break

    if calc_freqs == True:
        # HANDLE DATA
        vidInfo = getVideoInfo(vidObj)

        # guess_mean = np.mean(input_arr)
        # guess_std = 3*np.std(input_arr) / (2**0.5) / (2**0.5)
        # guess_phase = 0
        # guess_freq = 1
        # guess_amp =1

        # first_pass = guess_std*np.sin(time_arr+guess_phase) + guess_mean

        # FREQUENCIES
        FT = np.fft.fft(input_arr) / len(input_arr) # FFT with normalized amplitude
        FT = FT[range(int(len(input_arr) / 2))]
        values = np.arange(int(len(input_arr) / 2))
        timePeriod = len(input_arr) / vidInfo['fps']
        freqs = values / timePeriod

        # -----------------------------------------------------------

        # Plots
        fig, (ax1, ax2) = plt.subplots(2)
        ax1.plot(time_arr, input_arr, 'b-')
        # ax1.plot(time_arr, first_pass, 'r-')
        ax1.set(title = 'Time History of User Inputted Events',
                xlabel = 'time (s)',
                ylabel = 'recorded events')

        ax2.loglog(freqs, abs(FT), 'r-')
        ax2.set(title = 'Fourier Transform',
                xlabel = 'freqs (hz)',
                ylabel = 'amp')

        plt.show()

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()