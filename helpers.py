# IMPORT PACKAGES
import cv2

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