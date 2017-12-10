import os
user = os.environ.get('instagram_username')
pwd = os.environ.get('instagram_password')

def upload_image(caption, image):
    from InstagramAPI import InstagramAPI
    InstagramAPI = InstagramAPI(user, pwd)
    InstagramAPI.login()  # login
    InstagramAPI.uploadPhoto(image, caption=caption)
