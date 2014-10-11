from bs4 import BeautifulSoup
import urllib2


def getText(url):
    s = urllib2.urlopen(url)
    data = s.read()
    s.close()
    print s
    soup = BeautifulSoup(data)
    return soup.get_text()

    
print getText("http://love-python.blogspot.com/2008/02/get-html-source-of-url.html")


