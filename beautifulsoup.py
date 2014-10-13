from bs4 import BeautifulSoup, SoupStrainer, Comment
import urllib2, httplib

def listTexts(urls):
    htmls = []
    for u in urls:
       htmls.add(getText(url))
    return htmls 

def getText(url):
    try:
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
        soup = BeautifulSoup(data)
        h = ""
        for line in soup.findAll('p'):
            h += " "+line.getText();
    except (urllib2.HTTPError, urllib2.URLError) as e:
        print "\nERROR\n"
        h = ""
    return h


if __name__ == '__main__':    
    #print getText("https://docs.python.org/2/howto/urllib2.html")
    
    #print getText("http://www.politifact.com/texas/statements/2014/mar/19/kesha-rogers/four-us-citizens-killed-obama-drone-strikes-3-were/") 
    #print getText("http://screenrant.com/iron-man-actor-mark-wahlberg")
    print getText("http://www.nytimes.com/2013/07/18/opinion/the-drone-that-killed-my-grandson.html?_r=0")
    print getText("https://www.youtube.com/watch?v=VBmMU_iwe6U")
