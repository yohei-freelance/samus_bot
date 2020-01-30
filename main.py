import tweepy
import os
import glob
import random
import requests
from bs4 import BeautifulSoup

consumer_key = "sOTSIdDQStlhQAyDx2Uddobwr"
consumer_secret = "KQfEc3uEPE0rl2Z0RMt0RNwAIPqL1fM3gMvca0VDlLnFQhrXqo"
access_token_key = "737760200757649409-BU4MYWAqIUyKaLCKi8Ykp9q7PVqDmYJ"
access_token_secret = "WpvFyHcG5LtyNfIhga9mghQYg3gpKeCA71t8DlplhpUDb"

sam_pic="./images/samus.png"
zero_pic="./images/zero_samus.png"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

url = "https://tenki.jp/forecast/3/16/4410/13105/"
r = requests.get(url)
bsObj = BeautifulSoup(r.content, "html.parser")
today = bsObj.find(class_="today-weather")
weather = today.p.string
temp = today.div.find(class_="date-value-wrap")
temp = temp.find_all("dd")
temp_max = temp[0].span.string
temp_max_diff = temp[1].string
temp_min = temp[2].span.string
temp_min_diff = temp[3].string
content = "【今日の文京区・本郷の天気】\n"+"最高気温は"+temp_max+"℃("+temp_max_diff+")\n"+"最低気温は"+temp_min+"℃("+temp_min_diff+")"

def randomimagetwitt(folder):
    images = glob.glob(folder + "*")
    if int(temp_min) < 5:
      image_open = images[1]
    else:
      image_open = images[0]
    api.update_with_media(image_open, status=content)

randomimagetwitt("./images/")
