import urllib
import urllib2

url = "http://www.google.com/"
question = "Who played chase on house?"

urllist = []

def our_urls():
    urllist.append(urllib2.urlopen(url).geturl())
    return urllist
    #return urllib2.urlopen(url).geturl()

print our_urls()

