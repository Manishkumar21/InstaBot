import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_post_id import get_post_id

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            pass
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'