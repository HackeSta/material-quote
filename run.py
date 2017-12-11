import os
import tweepy
import pyimgur
import facebook
from config import *
from functions import *
from InstagramAPI import InstagramAPI


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_api(failbork):
    graph = facebook.GraphAPI(failbork['access_token'])
    return graph

print('Generating image')
generate()

tag = random.choice(tags)
pic = 'data/image.jpg'
texts = title, tag
splat = ' '.join(texts)

if not testmode:
    try:
        print('Tweeting')
        api.update_with_media(pic, splat)
    except tweepy.TweepError as e:
        print(e.reason)

    try:
        print('Failborking')
        fb = get_api(failbork)
        fb.put_photo(image=open(pic, 'rb'), message=splat)
    except:
        print('Failborked')

    try:
        print('Instaspamming')
        InstagramAPI = InstagramAPI(instauser, instapass)
        InstagramAPI.login()
        InstagramAPI.uploadPhoto(pic, caption=splat)
    except:
        print('Instafail')

    try:
        print('Imguring')
        im = pyimgur.Imgur(imgurid)
        uploaded_image = im.upload_image(pic, title=splat)
        # print(uploaded_image.link)
        with open('data/imgur.txt', 'a') as f:
            f.write(uploaded_image.link + '\n')
    except:
        print('Imgurfail')

else:
    print('TEST MODE')
