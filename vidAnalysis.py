# IMPORT PACKAGES
import cv2

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

    while (True):
        ret, frame = vidObj.read()

        if ret == True:
            cv2.imshow('vid', frame)

            # Press Q to quit
            if cv2.waitKey(1) == ord('q'):
                break

        # Break loop at error or end of vid
        else:
            print('Read error or end of video.')
            break

    # Cleanup
    vidObj.release()
    cv2.destroyAllWindows()