import pycurl
import os

access_token = os.environ.get('fb_access_token')

def upload_status(status,image):

    c = pycurl.Curl()
    values = [
        ('file' , (c.FORM_FILE, image)),
        ('access_token', access_token),
        ('message', status),
      ]

    c.setopt(c.POST, 1)
    c.setopt(c.URL,'https://graph.facebook.com/v2.11/me/photos')
    c.setopt(c.HTTPPOST,  values)
    c.perform()
    c.close()