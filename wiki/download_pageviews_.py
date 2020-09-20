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
#article = 'Apple_Inc.' 
granularity = 'daily' #daily, monthly 
start = '20150101'
end = '20170101'
#end = '20150105'

def get_views(project, access, agent, article, granularity, start, end):
    try:
        response = urlreq.urlopen('https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{0}/{1}/{2}/{3}/{4}/{5}/{6}'.format(project, access, agent, article, granularity, start, end))
    except: #urllib.error.HTTPError:
        response = None
        print ("Got no response for ", article )
    return response

def load_tickers_and_articles():
    f = open('tickers_and_pages.json', 'r')
    text = f.read()
    f.close()
    data = json.loads(text)
    ticks = {}

    count = 0 
    for item in data:
        #print (item['id'], item['ticker'], item['idLabel'], item['article'])
        try:
            ticks[item['ticker'].upper()] = item['article']
        except KeyError:
            print ("no article data for",  item['id'], item['ticker'], item['idLabel'])
            count +=1
            continue
        #input()
    print ("No article data for ", count , " items out of ", len(data))
    return ticks

def in_universe(ticker): #Q500US tickers
    if ticker in ['AA','AAPL','ABT','ADSK','TAP','ADBE','ADI','ADM','AEP','AET','AFL','AGN','HES','AIG','ALTR','AMAT','AMD','TWX','AMGN','AON','APA','APC','APD','ASH','ADP','AXP','AZO','BA','BAC','BAX','BBBY','BBY','BCR','BDX','BEAV','BEN','BHI','BK','BMY','BSX','CAG','CAT','CB','CBI','CCE','C','CAH','CELG','CERN','CI','CL','CLF','CLX','CMCSA','COG','COO','COST','CSCO','CSX','CTL','CMI','D','DD','DE','DHR','DIS','DOV','DOW','DHI','DUK','DVN','ECL','ED','EMC','EMR','EOG','EQT','EA','ESRX','ESV','ETN','ETR','F','FAST','M','FDO','FDX','FITB','FMC','S','NEE','GD','GE','GILD','GIS','GLW','GPS','GT','GWW','HAL','MNST','HBAN','HCN','HCP','HD','HOG','HFC','HOT','HP','HSY','HUM','HPQ','IBM','BIIB','INTC','IP','IPG','IR','ISIS','ITW','JCI','JCP','JNJ','K','KEY','KLAC','KMB','KO','KR','KSS','KSU','LEN','LLTC','LLY','LNC','LOW','LRCX','LB','LUV','SM','MAS','MAT','MCD','MDT','CVS','MGM','MHFI','MMC','MMM','MO','MHK','MSI','MRK','MRO','MSFT','MU','MUR','MYL','NBL','NBR','NE','NEM','NKE','THC','JWN','NOC','NSC','NUE','OII','OMC','ORCL','OXY','PAYX','PCAR','PCG','PCP','PEG','PEP','PFE','PG','PGR','PH','PHM','PNC','PNR','PPG','PPL','PRGO','PVH','PX','QCOM','RAD','REGN','ROK','ROST','RTN','T','SBUX','SCHW','SHW','SLB','PII','SO','TRV','SPLS','STT','STI','STJ','SYK','SWK','SWN','SYMC','SYY','TIF','TJX','TMO','TOL','TRN','TROW','TSO','TXN','TYC','TSN','UHS','UNH','UNP','UTX','VFC','VLO','VRTX','WDC','WEC','WFC','WFM','WHR','WMB','WMT','WY','X','XLNX','XOM','XRX','FL','CREE','CHK','ACT','ACE','INTU','GGP','ORLY','RCL','RIG','PETM','BWA','EQR','GMCR','SIG','ATVI','HST','INCY','NFX','PTEN','URBN','SPG','EMN','MLM','AKS','BRK.B','SIRI','O','SSYS','COF','FOXA','MCK','DLTR','LMT','DRI','LH','DDD','DISH','CAM','FCX','SUNE','PCYC','EL','NTAP','SNDK','CTXS','HIG','ALXN','EIX','YHOO','ETFC','ANF','OCN','CBST','DNR','NUS','DGX','KMX','AMTD','IVZ','AMZN','BBT','MS','PXD','CHRW','NLY','YUM','FE','CAR','URI','BRCM','LVLT','LLL','VTR','AVB','CTSH','WM','RRC','CCI','WFT','NVDA','PCLN','GS','PNRA','FFIV','JNPR','RAI','SBAC','UTHR','BMRN','RHT','AKAM','BLK','PLUG','UPS','TGT','EW','MET','SINA','CYH','MRVL','ENDP','ILMN','VZ','XEL','LNG','COH','EXC','MCO','MON','SLXP','GRMN','BTU','ADS','FTI','MDLZ','ABC','JOY','ZMH','ANTM','CVX','AAP','PRU','GME','JBLU','NFLX','SWKS','COP','CNP','DKS','WYNN','XEC','CME','EQIX','GLNG','STX','CCL','A','CNX','AMT','SRE','PLD','NOV','EBAY','RL','FLR','ALL','STZ','PSA','JPM','USB','HON','ISRG','ACN','WLL','MAR','TRW','DTV','NRG','GNW','CRM','GOOGL','NRF','LVS','HLF','WIN','HUN','LBTYA','DRC','EXPE','CF','ROC','AMP','ICE','SPWR','UA','CMG','UAL','GPOR','MDVN','MA','WYN','WU','CSIQ','HTZ','FSLR','SE','TWC','TMUS','DAL','CLR','JAZZ','COV','DFS','TEL','LULU','CXO','VMW','TDC','ATHN','RF','ULTA','CPN','PM','V','DPS','AGNC','LO','RAX',
        'DISCA','MJN','AVGO','CFN','DG','CHTR','LYB','OAS','TSLA','GM','FLT','NLSN','KMI','HCA','LNKD','MOS','YNDX','P','MPC','Z','ARCP','GRPN','DLPH','TRIP','KORS','ZNGA','SLCA','YELP','PSX','SPLK','FB','NOW','PANW','KRFT','ICPT','WDAY','FANG','RH','ABBV','SCTY','ZTS','DATA','MNK','FEYE','TWTR','AAL','HLT','GPRO','MBLY']: return True
    else: return False

    

ticks = load_tickers_and_articles()

print (ticks['AAPL'] ) 
print (ticks['AMZN'] ) 
print (ticks['TSLA'] ) 


csv = []
fail_count = 0 
tot_count = 0

#for tick in ['AAPL', 'AMZN', 'TSLA', 'MSFT']: 
for tick in sorted(ticks): 
    if not in_universe(tick): continue
    print (tick, ticks[tick], ticks[tick].split("/")[-1])
    if tick == 'TSLA':
        response = get_views(project, access, agent, 'Tesla_Motors,_Inc.', granularity, start, end)
    elif tick == 'AMZN':
        response = get_views(project, access, agent, 'Amazon.com', granularity, start, end)
    else:
        response = get_views(project, access, agent, ticks[tick].split("/")[-1], granularity, start, end)

    if response is not None:
        tot_count +=1
        pageviews_data = json.loads(response.read())
        #views = []
        
        for item in pageviews_data['items']:
            #print (item['timestamp'], item['views'])
            #views.append(item['views'])
            ts = item['timestamp']
            csv.append(",".join([ts[:4]+'-'+ts[4:6]+'-'+ts[6:8], tick, str(item['views']) ]))

        #plt.figure()
        #plt.plot(views, label=tick)
        #plt.legend(loc = 'best')
    else:
        fail_count +=1

print (fail_count, " out of ", tot_count, 'failed')

f = open('pageviews_data.csv', 'w')
csv = "\n".join(csv)
f.write(csv)
f.close()
#input()
