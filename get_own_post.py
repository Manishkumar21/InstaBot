import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
import urllib

def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print("\n\n")
            print "Your Recent image has been downloaded to C:\Users\Game Is Here\PycharmProjects\InstaBot"
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'

#get_own_post()