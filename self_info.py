import requests
from constant_variable import APP_ACCESS_TOKEN, BASE_URL


def self_info():
    #logic of the function
    print("Hello")
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print '\n\t\t\t****Username: %s****' % (user_info['data']['username'])
            print '\t\t\t****No. of followers: %s****' % (user_info['data']['counts']['followed_by'])
            print '\t\t\t****No. of people you are following: %s****' % (user_info['data']['counts']['follows'])
            print '\t\t\t****No. of posts: %s****' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'
