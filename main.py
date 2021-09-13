"""
MANUAL PROCESS FOR TAIL-BEAT FREQUENCY CALCULATION

Koppi Kolyvek
(c) Moosh Systems - September 2021
"""

# FREQUENCY CALCULATION BY KEYSTROKE
# - press [I] to begin the calculation segment
# - press [O] to log a notable event
# - press [P] to end segment and present graph

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