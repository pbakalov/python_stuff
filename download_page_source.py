#import urllib
#url = "http://www.promacedonia.org/bmark/cepenkov/bio/cepenkov.html"
#urllib.urlretrieve (url, "cepenkov.txt")

url = "https://www.cik.bg/bg/pvr2016/foreign/registered"
#urllib.urlretrieve (url, "cik.txt")

#doesn't work 
import urllib2
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request(url, None, headers)
response = urllib2.urlopen(req)
page = response.read()
response.close()

print len(page)
