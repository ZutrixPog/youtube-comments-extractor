import sys
import asyncio
import pandas

from comments import utils
from comments.executor import CommentExecutor

TASKS_NUM = 5

async def main():
    videos_file = sys.argv[1]
    videos = pandas.read_csv(videos_file)
    videos = videos['videoId']

    executor = CommentExecutor()

    await executor.add_video(videos)
    await executor.execute(utils.retrieve_comments_task, num_workers=5)

# running the event loop
if __name__ == "__main__":
    asyncio.run(main())