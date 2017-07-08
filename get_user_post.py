# Files and Functions are Imported

import requests
import urllib
from get_user_id import get_user_id
from constant_variable import APP_ACCESS_TOKEN,BASE_URL

def get_user_post(insta_username):
    # Function Logic to Download user's Recent Post..

    user_id = get_user_id(insta_username)        #Get the User's Id
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:       #Check if there is any user or not
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            (urllib.urlretrieve(image_url, image_name))
            print(user_media['data'][0]['id'])
            print 'Your image has been downloaded!'
            return user_media['data'][0]['id']

        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'