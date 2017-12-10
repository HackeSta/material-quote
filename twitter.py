import os
from twython import Twython

app_key = os.environ.get('app_key')
app_secret = os.environ.get('app_secret')
token = os.environ.get('token')
token_secret = os.environ.get('token_secret')
twitter = Twython(app_key,app_secret,token,token_secret)


def upload_status(tweet, image):
    response = twitter.upload_media(media=image)
    twitter.update_status(status=tweet, media_ids=[response['media_id']])
