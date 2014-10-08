from bs4 import BeautifulSoup

def getText(doc):
    f=open(doc,'r')
    s=f.read()
    f.close()
    soup = BeautifulSoup(s)
    return soup.get_text()

print getText("sample.html")
