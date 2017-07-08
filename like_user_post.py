# Files and Functions are Imported

import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_post_id import get_post_id


def like_user_post(insta_username):
    # Function Logic to Like User's Recent Post

    media_id = get_post_id(insta_username)
    print(media_id)
    request_url = (BASE_URL + "media/"+media_id+"/likes")
    payload = {"access_token" : APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print '\n\t\t*****Like was successful!*****'
    else:
        print '\n\t\t*****Your like was unsuccessful. Try again!*****'