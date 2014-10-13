from bs4 import BeautifulSoup
import urllib2

def listTexts(urls):
    htmls = []
    for u in urls:
       htmls.add(getText(url))
    return htmls 

def getText(url):
    s = urllib2.urlopen(url)
    data = s.read()
    s.close()
    soup = BeautifulSoup(data)
    return soup.get_text()

if __name__ == '__main__':    
    #print getText("https://docs.python.org/2/howto/urllib2.html")
    #print getText("http://www.nytimes.com/2009/12/21/us/21storm.html?_r=0")
    # 303 error
    print getText("http://screenrant.com/iron-man-actor-mark-wahlberg")
    # has javascript,css,etc 
   
