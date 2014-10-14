import urllib
import urllib2

url = "http://www.google.com/"

urllist = []

def our_urls():
    return urllib2.urlopen(url).geturl()

question = "Who played chase on house?"

print our_urls()

