import requests
import pandas
import os
from bs4 import BeautifulSoup
import scrapetube

from comments.comments import CommentDownloader

FILENAME = "./data/comments.csv"

def get_channel_id_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    
    res = soup.find("meta", itemprop="channelId")['content']
    if res:
      return soup.find("meta", itemprop="channelId")['content']
    
    return ""


def retrieve_vids(url):
  channel_id = get_channel_id_from_url(url)
  videos = scrapetube.get_channel(channel_id)
  return list(videos)

async def retrieve_comments(id, downloader):
  comments = []
  async for com in downloader.get_comments_from_url("https://www.youtube.com/watch?v=" + id, sort_by=0):
     comments.append(com)

  df_comment = pandas.DataFrame(comments)
  print("retrieved " + str(id))

  if not os.path.isfile(FILENAME):
    df_comment.to_csv(FILENAME, encoding='utf-8', index=False)
  else:  # else it exists so append without writing the header
    df_comment.to_csv(FILENAME, mode='a', encoding='utf-8', index=False, header=False)

async def retrieve_comments_task(id_queue):
    downloader = CommentDownloader()
    while not id_queue.empty():
        try:
           url = await id_queue.get()
           await retrieve_comments(url, downloader)
        except:
           continue
