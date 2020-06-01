import urllib.request as urlreq
import json
import matplotlib.pylab as plt
plt.ion()

#basic template:
# https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}
#
# e.g.:
# https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/desktop/user/Apple_Inc./daily/20200101/20200229
#
# see: https://wikimedia.org/api/rest_v1/#/

project = 'en.wikipedia.org'
access =  'all-access' #all-access, desktop, mobile-web, mobile-app
agent = 'user' #all-agents, user, spider, bot 
article = 'Apple_Inc.' 
granularity = 'daily' #daily, monthly 
start = '20160101'
end = '20170101'

def get_views(project, access, agent, article, granularity, start, end):
    response = urlreq.urlopen('https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{0}/{1}/{2}/{3}/{4}/{5}/{6}'.format(project, access, agent, article, granularity, start, end))
    return response


response = get_views(project, access, agent, article, granularity, start, end)

data = json.loads(response.read())

views = []

for item in data['items']:
    print (item['timestamp'], item['views'])
    views.append(item['views'])

plt.plot(views)

input()
