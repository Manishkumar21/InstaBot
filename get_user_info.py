# Files and Functions are Imported

import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_user_id import get_user_id

def get_user_info(insta_username):
    # Function Logic to get user profile Information
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s\n' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print '\n\t\t\t****Username: %s*****' % (user_info['data']['username'])
            print '\t\t\t****No. of followers: %s*****' % (user_info['data']['counts']['followed_by'])
            print '\t\t\t****No. of people you are following: %s*****' % (user_info['data']['counts']['follows'])
            print '\t\t\t****No. of posts: %s*****' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'