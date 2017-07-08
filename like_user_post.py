import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_post_id import get_post_id


def like_user_post(insta_username):
    media_id = get_post_id(insta_username)
    print(media_id)
    request_url = (BASE_URL + "media/"+media_id+"/likes")
    payload = {"access_token" : APP_ACCESS_TOKEN}
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'