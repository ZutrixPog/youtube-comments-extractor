from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import sys
import pandas

from comments import utils

def main():
    channels_file = sys.argv[1]
    channels = pandas.read_csv(channels_file)


    video_urls = []
    count = 0

    with ThreadPoolExecutor(max_workers = 5) as executor:

        future_to_url = {executor.submit(utils.retrieve_vids, id): id for id in channels}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                count += len(data)
                video_urls.extend(data)
                print(str(count) + " videos")
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('working')


    out = pandas.DataFrame(video_urls)
    out.columns = ['url']

    out.to_csv("videos.csv")
    print("wrote video urls to videos.csv")


if __name__ == "main":
    main()