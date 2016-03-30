from requests_oauthlib import OAuth1Session
import configparser
import os
import sys
import json

config = configparser.ConfigParser()
config.read("config.ini")
token = config["token"]

CK = token["CK"]                # Consumer Key
CS = token["CS"]                # Consumer Secret
AT = token["AT"]                # Access Token
AS = token["AS"]                # Access Token Secret

DEL_NUM = 120                   # 一度に消すツイートの数

with open("tweet_list.js") as f:
    twi_list = json.load(f)

start = 0
if os.path.exists("./cnt.txt"):
    with open("cnt.txt", "r") as f:
        start = int(f.read().rstrip())

twitter = OAuth1Session(CK, CS, AT, AS)
del_url = "https://api.twitter.com/1.1/statuses/destroy/{}.json"
cnt = 0
for i in range(start, start+DEL_NUM):
    twitter.post(del_url.format(twi_list[i]["id"]))
    cnt += 1

print("全部で{}件ツイートを削除しました。".format(cnt))

with open("cnt.txt", "w") as f:
    f.write(str(start+DEL_NUM))
