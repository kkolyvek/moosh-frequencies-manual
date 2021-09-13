# IMPORT PACKAGES
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle

# Function to get and print frame info
def getVideoInfo(vidObj):
    """
    Reads some video metadata.
    """

    # Create a new dictionary
    vidInfo = dict()
    # Get info on the video
    vidInfo['frame_width'] = int(vidObj.get(3))
    vidInfo['frame_height'] = int(vidObj.get(4))
    vidInfo['length'] = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    vidInfo['fps']    = vidObj.get(cv2.CAP_PROP_FPS)
    return vidInfo

# Function to handle user inputted data
def handleData(vidObj, data_array):
    """
    Handling of user inputted data is done here.
    """

    # HANDLE DATA
    vidInfo = getVideoInfo(vidObj)

    # Handle each segment:
    for i in range(len(data_array)):
        # label segment
        data_array[i]['segment_number'] = i + 1

        # create time / input arrays only including inputted data points
        data_array[i]['filtered_user_input'] = []
        data_array[i]['filtered_frame_count'] = []
        data_array[i]['filtered_time'] = []
        for j in range(len(data_array[i]['unfiltered_user_input'])):
            if data_array[i]['unfiltered_user_input'][j] != 0:
                data_array[i]['filtered_user_input'].append(data_array[i]['unfiltered_user_input'][j])
                data_array[i]['filtered_frame_count'].append(data_array[i]['unfiltered_frame_count'][j])
                data_array[i]['filtered_time'].append(data_array[i]['unfiltered_frame_count'][j] / vidInfo['fps'])

        # create array of wave peak to peak times (s)
        data_array[i]['wavelengths'] = []
        peakNum = 0
        prevTime = 0
        for j in range(len(data_array[i]['filtered_user_input'])):
            if data_array[i]['filtered_user_input'][j] == 1:
                # iterate peak number
                peakNum += 1
                
                # ignore first peak (no previous data)
                if peakNum > 1:
                    data_array[i]['wavelengths'].append(data_array[i]['filtered_time'][j] - prevTime)

                # iterate time stamp
                prevTime = data_array[i]['filtered_time'][j]
        
        # get average wavelength period (s) + frequency (hz)
        data_array[i]['avg_segment_period'] = np.array(data_array[i]['wavelengths']).sum() / len(data_array[i]['wavelengths'])
        data_array[i]['avg_segment_freq'] = 1 / data_array[i]['avg_segment_period']

    return data_array

def displayData(data_array):
    """
    Displays some (already handled) data in both the command line and in matplotlib charts.
    """

    # PRINT IMPORTANT INFO

    for i in range(len(data_array)):
        print('\n---------- Segment ' + str(data_array[i]['segment_number']) + ' ----------')
        print('Average Tail Beat Period: ' + str(data_array[i]['avg_segment_period']) + ' s')
        print('Average Tail Beat Frequency: ' + str(data_array[i]['avg_segment_freq']) + ' hz')
        print('\n')

    # -----------------------------------------------------------

    # PLOTTING

    for i in range(len(data_array)):
        fig, (ax1, ax2) = plt.subplots(2)
        fig.canvas.manager.set_window_title('Segment ' + str(data_array[i]['segment_number']))

        # plot original input data
        ax1.plot(data_array[i]['filtered_time'],
                data_array[i]['filtered_user_input'],
                'b-',
                label='Original data')
        ax1.set(title = 'User Inputted Events',
                xlabel = 'time (s)',
                ylabel = 'recorded events')

        # plot tail beat period over time
        ax2.plot(np.linspace(1, len(data_array[i]['wavelengths']), len(data_array[i]['wavelengths'])),
                data_array[i]['wavelengths'],
                'b-',
                label="Wavelength Data")
        ax2.set(title = 'Shark Tail Beat Period Over Time',
                xlabel = 'Tail Beat Number',
                ylabel = 'Tail Beat Period (s)')

    plt.show()

def saveData(data_array):
    pickleName = 'video_data'
    pickle.dump(data_array, open(pickleName + '.pickle', 'wb'))