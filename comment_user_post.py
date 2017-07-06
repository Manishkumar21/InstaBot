import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_user_post import get_user_post


def comment_user_post(insta_username):
    media_id = get_user_post(insta_username)
    print(media_id)
    message = raw_input("Enter ur comment....\n")
    payload = {"access_token" : APP_ACCESS_TOKEN, "message":message}
    request_url = (BASE_URL + "media/" + media_id + "/comments")
    post_a_comment = requests.post(request_url,payload).json()
    print 'POST request url : %s' % (request_url)

    print(post_a_comment['meta']['code'])
    if post_a_comment['meta']['code'] == 200:
        print("Post comment successfully")
    else :
        print('not successful')


