# Files and Functions are Imported
import requests
from constant_variable import APP_ACCESS_TOKEN ,BASE_URL
from get_post_id import get_post_id
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt

def show_all_comment(insta_username):
    # Function Logic to Show all Comments..

    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s\n' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:     #Check if there are negative and positive comments..

        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print '\t(-)Negative comment : %s' % (comment_text)
                else:
                    print '\t(+)Positive comment : %s' % (comment_text)
        else:
            print '\t*****There are no existing comments on the post!*****'

    #Plot the pie-Chart

        print "\n\t*****Here is the Pie-Chart Analysis of Positive and Negative Comments.*****"
        var1 = blob.sentiment.p_neg
        var2 = blob.sentiment.p_pos
        str_var1 = str(var1)
        str_var2 = str(var2)
        str_var1 = len(str_var1)
        str_var2 = len(str_var2)
        labels = 'Positive Comments', 'Negative Comments'
        sizes = [str_var1, str_var2]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Negative Comment')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    else:
         print '\n\t\t*****Status code other than 200 received!*****'
