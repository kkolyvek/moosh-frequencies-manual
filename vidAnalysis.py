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

    # Initialize
    data_array = []                 # data array of dictionaries
    time_arr = []                   # general array to count frames
    input_arr = []                  # general array to count user input events
    frame_counter = 0               # frame number iterator

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


    # POST PROCESSING AND CLEANUP
    # ==============================================

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()
    
    # HANDLE DATA
    data_array = handleData(vidObj, data_array)


    # DISPLAY DATA
    displayData(data_array)

    # SAVE DATA
    saveData(data_array)