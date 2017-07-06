import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_user_id import get_user_id
from get_user_post import get_user_post

def comment_user_post1(insta_username):
    post_id = get_user_id(insta_username)
    print(post_id)
    message = raw_input("Enter ur comment....\n")
    request_url = (BASE_URL + "media/" + post_id + "/comments")
    payload = {"access_token": APP_ACCESS_TOKEN, "Message": message}
    post_a_comment = requests.post(request_url, payload).json()
    print 'POST request url : %s' % (request_url)

    print(post_a_comment['meta']['code'])
    if post_a_comment['meta']['code'] == 200:
        print("Post comment successfully")
    else :
        print('not successful')



