# Files and Functions are Imported

import requests
from constant_variable import APP_ACCESS_TOKEN, BASE_URL

def self_info():
    # Function Logic to Show Own Profile Information

    print("Hello")
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:    #Check if Username and password is true and show data of own
        if len(user_info['data']):
            print '\n\t\t\t****Username: %s****' % (user_info['data']['username'])
            print '\t\t\t****No. of followers: %s****' % (user_info['data']['counts']['followed_by'])
            print '\t\t\t****No. of people you are following: %s****' % (user_info['data']['counts']['follows'])
            print '\t\t\t****No. of posts: %s****' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'
