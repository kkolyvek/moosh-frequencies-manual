# Manual Shark Tail-Beat Frequency Processing

## About

This program is intended to aid in frequency estimations from video files. Requires user input.

## Usage

1. In `main.py`, declare the path to the video file you'd like to inspect.
2. Modify your desired pickle file name in `helpers.py` under `saveData()`.
3. Run the file from the terminal using `python main.py`.
4. When you'd like to begin tracking oscillations, press `I`.
5. Press `O` at the apex (points of maximum deflection, both positive and negative) of each oscillation.
6. To end tracking a segment, press `P`.
7. Press `Q` at any point to end the video display and present data.

## NOTES

- Multiple segments may be recorded in the same video, simply press `I` again after you have ended a previous segment by pressing `P`.
- Upon quitting via `Q` or end of video, segment data will be printed in command line and matplotlib charts will display.
- Segments not ended by pressing `P` **will not** be saved or analyzed.
- Data is saved in the following format:

        data array: [
            {
                'segment_number'            - an integer denoting segment i.e. 1 for first segment, 2 for second, etc...
                'unfiltered_user_input'     - an array of equal length to frame count with user inputs logged with 1s and -1s, zero otherwise
                'unfiltered_frame_count'    - an array of the frame number
                'filtered_user_input'       - an array of just user inputted events (1s and -1s)
                'filtered_frame_count'      - an array of frame numbers of user inputted events
                'filtered_time'             - an array of time (in seconds) of when user inputted event was recorded
                'wavelengths'               - an array of periods (in seconds) of shark tail oscillations
                'avg_segment_period'        - a float of average period (in seconds) of shark tail oscillations in a segment
                'avg_segment_freq'          - a float of average frequency (in hz) of shark tail oscillations in a segment
            },
            {cont. with next segment...}
        ]

- Data will be saved into your local repository directory.
