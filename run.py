import os
import tweepy
import facebook
from InstagramAPI import InstagramAPI
from config import *
from functions import *


def get_api(failbork):
    graph = facebook.GraphAPI(failbork['access_token'])
    return graph

generate()

tag = random.choice(tags)
pic = 'data/image.jpg'
texts = title, tag
splat = ' '.join(texts)

if not testmode:
    try:
        print('Tweeting fancy quote')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        api.update_with_media(pic, splat)
    except tweepy.TweepError as e:
        print(e.reason)

    try:
        print('Failborking fancy quote')
        fb = get_api(failbork)
        fb.put_photo(image=open(pic, 'rb'), message=splat)
    except:
        print('Failborked')

    try:
        print('Instaspamming fancy quote')
        InstagramAPI = InstagramAPI(instauser, instapass)
        InstagramAPI.login()
        InstagramAPI.uploadPhoto(pic, caption=splat)
    except:
        print('Instafail')
else:
    print('TEST MODE')
