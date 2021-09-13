# IMPORT PACKAGES
import cv2

# IMPORT METHODS
from helpers import handleData, displayData, saveData

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
    frame_counter = 0 # time series array
    # first recorded keystroke is positive
    input_val = 1

    # Initialize array of dictionaries. Each dictionary corresponds to 
    # a frequency recording segment with the following layout:
    # data array: [
    #   {
    #       'segment_number'            - an integer denoting segment i.e. 1 for first segment, 2 for second, etc...
    #       'unfiltered_user_input'     - an array of equal length to frame count with user inputs logged with 1s and -1s, zero otherwise
    #       'unfiltered_frame_count'    - an array of the frame number
    #       'filtered_user_input'       - an array of just user inputted events (1s and -1s)
    #       'filtered_time'             - an array of time (in seconds) of when user inputted event was recorded
    # },
    # {cont. with next segment...}
    # ]
    data_array = []
    time_arr = []
    input_arr = []
    frame_counter = 0

    while (True):
        ret, frame = vidObj.read()


        if ret == True:
            cv2.imshow('vid', frame)

            frame_counter += 1

            key = cv2.waitKey(1)

            if listening == True:
                time_arr.append(frame_counter)

            # Keystroke listeners
            # ==============================================================

            # Press Q to quit video
            if key == ord('q'):
                break

            # Press I to begin a calculation segment
            if key == ord('i'):
                listening = True

                # manually add first item
                time_arr.append(frame_counter)

            # Press O to store a keystroke frame
            if listening == True:
                if key == ord('o'):
                    input_arr.append(input_val)
                    input_val *= -1
                else:
                    input_arr.append(0)

            # Press P to end calculation segment and add to array
            if key == ord('p'):
                # add data to data object in array
                segment_data = {
                    'unfiltered_user_input': input_arr,
                    'unfiltered_frame_count': time_arr
                }
                data_array.append(segment_data)
                # reset data arrays
                input_arr = []
                time_arr = []

                listening = False

            # ==============================================================

        # Break loop at error or end of vid
        else:
            print('Read error or end of video.')
            break
    
    # HANDLE DATA
    data_array = handleData(vidObj, data_array)

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()

    # DISPLAY DATA
    displayData(data_array)

    # SAVE DATA
    saveData(data_array)