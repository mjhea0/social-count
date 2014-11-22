import urllib2
import json

TWITTER = 'https://cdn.api.twitter.com/1/urls/count.json?url={0}'
FACEBOOK = "https://api.facebook.com/method/links.getStats?urls={0}&format=json"
LINKEDIN = "https://www.linkedin.com/countserv/count/share?url={0}&format=json"


def get_twitter(url):
    request = urllib2.urlopen(TWITTER.format(url))
    results = json_decode(request)
    print "\nTwitter:"
    print "Tweets:", results['count']


def get_facebook(url):
    request = urllib2.urlopen(FACEBOOK.format(url))
    results = json_decode(request)
    print "\nFacebook:"
    print "Shares:", results[0]['share_count']
    print "Likes:", results[0]['like_count']
    print "Comments:", results[0]['comment_count']
    print "Clicks:", results[0]['click_count']
    print "TOTAL:", results[0]['total_count']


def get_linkedin(url):
    request = urllib2.urlopen(LINKEDIN.format(url))
    results = json_decode(request)
    print "\nLinkedIn:"
    print "Shares:", results['count']


# helper

def json_decode(request):
    return json.loads(request.read())


if __name__ == '__main__':
    url = raw_input("Enter a URL: ")
    get_twitter(url)
    get_facebook(url)
    get_linkedin(url)
