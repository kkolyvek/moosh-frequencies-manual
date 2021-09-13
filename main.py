"""
MANUAL PROCESS FOR TAIL-BEAT FREQUENCY ESTIMATION

Koppi Kolyvek
(c) Moosh Systems - September 2021
"""

# FREQUENCY ESTIMATION BY KEYSTROKE
# - press [I] to begin a listener segment
# - press [O] to log a notable event
# - press [P] to end segment

# -----------------------------------------------------------

# IMPORT PACKAGES
import cv2

# IMPORT METHODS
from vidAnalysis import vidAnalysis

"""
MAIN
===============================================================
"""

def main():
    # DECLARE PATH TO VIDEO
    dirName = 'C:\\Users\\koppa\\Desktop\\Personal\\Projects\\moosh-frequencies\\videos\\DJI_0024_Trim.mp4'
    print(dirName)

    # Init VideoCapture Object
    vidObj = cv2.VideoCapture(dirName)

    vidAnalysis(vidObj)

if __name__ == "__main__":
    main()