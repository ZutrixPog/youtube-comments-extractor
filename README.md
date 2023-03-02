# Youtube Persian Comments Extractor
The Project is intended to facilitate Youtube comments extraction. In order to achieve this and overcome youtube API restrictions, innertube API is used under the hood. The code is fairly optimized and comment extraction is fully async. This project serves two main purposes; **Retrieving channel videos and Retrieving a videos's comments.**Refer to Usage section for more info.


# Usage
You can utilize project functionalities via the two main scripts present in the root directory.

## channel_videos.py
Given a csv file containing one column for channel ids, the script would find all related video ids and store them in a csv file located in the /data folder.
Example:
	
	`python ./channel_videos.py ./channels.csv`

## video_comments.py
Given a csv file containing Video ids, the script would retrieve all comments posted on the video. An example of required csv file is given in the ./data folder.
Example: 

    python ./video_comments.py ./data/videos.csv

