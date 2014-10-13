import urllib2

url = "http://www.google.com/"

urllist = []

try:
  result = urllib2.urlopen(url)
  urllist.append(result)
except urllib2.URLError, e:
  handleError(e)

print urllist
