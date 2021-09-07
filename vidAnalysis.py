# IMPORT PACKAGES
import cv2

# IMPORT METHODS
from helpers import handleData

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

            # Press Q to quit ungracefully
            if key == ord('q'):
                calc_freqs = False
                break

            # Press I to begin a calculation segment
            if key == ord('i'):
                listening = True
                calc_freqs = True

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
                break

            # ==============================================================

        # Break loop at error or end of vid
        else:
            print('Read error or end of video.')
            break

    handleData(vidObj, calc_freqs, time_arr, input_arr)

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()