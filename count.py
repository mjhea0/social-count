import urllib2
import json

TWITTER = 'https://cdn.api.twitter.com/1/urls/count.json?url={0}'
FACEBOOK = "https://api.facebook.com/method/links.getStats?urls={0}&format=json"
LINKEDIN = "https://www.linkedin.com/countserv/count/share?url={0}&format=json"


def get_twitter(url):
    request = urllib2.urlopen(TWITTER.format(url))
    jsonLoad = json.loads(request.read())
    print "\nTwitter:"
    print "Tweets:", jsonLoad['count']


def get_facebook(url):
    request = urllib2.urlopen(FACEBOOK.format(url))
    jsonLoad = json.loads(request.read())
    print "\nFacebook:"
    print "Shares:", jsonLoad[0]['share_count']
    print "Likes:", jsonLoad[0]['like_count']
    print "Comments:", jsonLoad[0]['comment_count']
    print "Clicks:", jsonLoad[0]['click_count']
    print "TOTAL:", jsonLoad[0]['total_count']


def get_linkedin(url):
    request = urllib2.urlopen(LINKEDIN.format(url))
    jsonLoad = json.loads(request.read())
    print "\nLinkedIn:"
    print "Shares:", jsonLoad['count']


if __name__ == '__main__':
    url = raw_input("Enter a URL: ")
    get_twitter(url)
    get_facebook(url)
    get_linkedin(url)
