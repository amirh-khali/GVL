import pandas as pd
import os
import requests
from urllib.parse import urlparse

username = 'htlog23'
password = 'fb93dc3b1950d18'

videos_path = './videos/'
isExist = os.path.exists(videos_path)
if not isExist:
   os.makedirs(videos_path)


def download_video(url):
    filename = os.path.basename(urlparse(url).path)
    response = requests.get(url, auth=(username, password), verify=False)
    if response.status_code == 200:
        with open(videos_path + filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded {filename} successfully!")
    else:
        print(f"Failed to download {filename}.", response.reason)


video_urls = list(pd.read_csv('./cooking_video_urls.csv')['keys'])
for url in video_urls:
    download_video(url)
