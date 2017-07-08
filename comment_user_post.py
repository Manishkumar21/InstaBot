 #Files and Functions are Imported
import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_user_id import get_user_id

def comment_user_post1(insta_username):
    #Function Logic for post a Comment

    post_id = get_user_id(insta_username)   #Get the User's Id
    print(post_id)
    message = raw_input("Enter ur comment....\n")
    request_url = (BASE_URL + 'media/%s/comments') % (post_id)
    payload = {"access_token":APP_ACCESS_TOKEN, "text": message}
    post_a_comment = requests.post(request_url, payload).json()
    print 'POST request url : %s' % (request_url)

    print(post_a_comment['meta']['code'])   #Check if Comment is Posted Or Not
    if post_a_comment['meta']['code'] == 200:
        print("Post comment successfully")
    else :
        print('not successful')


