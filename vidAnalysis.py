# IMPORT PACKAGES
import cv2
from matplotlib import pyplot as plt

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
    listening = False
    calc_freqs = False

    frame_counter = 0

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
                    input_arr.append(1)
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
        # Plots
        fig, (ax1, ax2) = plt.subplots(2)
        ax1.plot(time_arr, input_arr, 'b-')
        ax1.set(title = 'Time History of User Inputted Events',
                xlabel = 'time (s)',
                ylabel = 'recorded events')


        plt.show()

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()