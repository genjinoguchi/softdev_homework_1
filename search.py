import urllib2
from beautifulsoup import listTexts
from regexp import processNames, processDates
#from pygoogle import pygoogle

def getAnswers(query):
  results={}

  urllist=[]
  
  #g = pygoogle("What is your problem")
  #g.pages = 1
  #urllist = g.get_urls()

  urllist.append("http://www.politifact.com/texas/statements/2014/mar/19/kesha-rogers/four-us-citizens-killed-obama-drone-strikes-3-were/")
  urllist.append("https://docs.python.org/2/howto/urllib2.html")
  urllist.append("http://www.politifact.com/texas/statements/2014/mar/19/kesha-rogers/four-us-citizens-killed-obama-drone-strikes-3-were/")


  stringlist=listTexts(urllist)
  
  if query.find("Who")>=0 or query.find("who")>=0:
    results = processNames(stringlist)
    #print results
  elif query.find("When")>=0 or query.find("when")>=0:
    results = processDates(stringlist)
  else:
    results["I'm sorry, I didn't understand that"]=5;
  return results
