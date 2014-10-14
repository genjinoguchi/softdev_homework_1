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
  print "I'm here now"
  print stringlist
  
  if query.find("Who")>=0 or query.find("who")>=0:
    names = processNames(stringlist)
    print names
    for name in names:
      if name in results.keys():
        results[name]+=1
      else:
        results[name]=1
  else:
    dates=processDates(stringlist)
    for date in dates:
      if date in results.keys():
        results[date]+=1
      else:
        results[date]=1
  return results
      
