#coding=utf-8

###some things borrowed from https://stackoverflow.com/questions/29859565/create-the-economist-style-graphs-from-python
import matplotlib.pylab as plt
import matplotlib
matplotlib.rc('font', family='Arial') #нужно на OS X, за да се изобразява българския
from numpy import zeros, arange, linspace
#plt.ion()
#plt.xkcd()

y_max1 = 150 #лява скала
y_max2 = 800 #дясна скала

trakia_dict ={"until 1995":133, #trakia
            1995:32,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:4,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:15,
            2007:35.2,
            2008:22,
            2009:0,
            2010:0,
            2011:0,
            2012:81.78,
            2013:34.28,
            2014:0.,
            2015:0.}

haemus_dict ={"until 1995":127.9, #hemus
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:5.47,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:12.8,
            2006:0,
            2007:0,
            2008:0,
            2009:0,
            2010:0,
            2011:0,
            2012:0,
            2013:16.46,
            2014:0.,
            2015:4.989}

maritsa_dict ={"until 1995":19.14, #martisa
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:0,
            2007:16.66,
            2008:0,
            2009:0,
            2010:3.62, #в уикипедия информацията е малко противоречива
            2011:0,
            2012:0,
            2013:0,
            2014:5.,
            2015:34.22+8.69+31.4} #34.22+ 8.690 

struma_dict ={"until 1995":0, 
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:0,
            2007:19.,
            2008:0,
            2009:0,
            2010:0,
            2011:0,
            2012:0,
            2013:13.98,
            2014:0.,
            2015:14.7 + 37.48}

lyulin_dict ={"until 1995":0, 
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:0,
            2007:0,
            2008:0,
            2009:0,
            2010:0,
            2011:19.,
            2012:0,
            2013:0,
            2014:0.,
            2015:0.}

kalotina_dict ={"until 1995":0, 
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:0,
            2007:0,
            2008:0,
            2009:0,
            2010:0,
            2011:0,
            2012:0,
            2013:0,
            2014:0.,
            2015:0.}

cherno_more_dict ={"until 1995":10, 
            1995:0,
            1996:0,
            1997:0,
            1998:0,
            1999:0,
            2000:0,
            2001:0,
            2002:0,
            2003:0,
            2004:0,
            2005:0,
            2006:0,
            2007:0,
            2008:0,
            2009:0,
            2010:0,
            2011:0,
            2012:0,
            2013:0,
            2014:0.,
            2015:0.}

class highway(object):
    def __init__(self, name, proj_length, year_started, timeline):
        self.name=name
        self.proj_lenth=proj_length
        self.year_started=year_started
        self.timeline=timeline #km built between 1995 and the current year
        self.curr_length=0

    def calculate_length(self):
        self.curr_length = 0
        for key in self.timeline.keys():
            self.curr_length+=self.timeline[key]
        return self.curr_length

    def show_length(self):
        print self.curr_length

    def show_timeline(self):
        for key in self.timeline.keys():
            print key, self.timeline[key]


for bg in [0,1,2]:
    dict_list = [trakia_dict, haemus_dict, maritsa_dict, struma_dict, lyulin_dict, cherno_more_dict, kalotina_dict]
    tot_len = 0.
    name_list = ["Тракия", "Хемус", "Марица", "Струма", "Люлин", "Черно Море", "Калотина"]
    
    for highway_dict, name in zip(dict_list, name_list):
        curr_highway = highway(name, 0, 0, highway_dict)
        tot_len+=curr_highway.calculate_length()
        print name
        curr_highway.show_length()
    print 'total', tot_len
    
    #trakia = highway("Trakia", 300, 1970, time_dict)
    #trakia.calculate_length()
    #trakia.show_length()
    #trakia.show_timeline()
    
    start_year = 1995
    end_year = 2016
    timeline = zeros(end_year-start_year, float)
    cumulative = zeros(end_year-start_year, float)
    for highway_dict in dict_list:
        for i,key in enumerate(range(start_year,end_year)):
            timeline[i] += highway_dict[key]
            cumulative[i] += highway_dict["until 1995"]
    
    for i in range(end_year-start_year):
        if i == 0:
            print "before 1995:", cumulative[i]
        cumulative[i]+= sum(timeline[:i+1])
        print start_year+i, cumulative[i]
    
    
    if bg == 1: #Български текст
        label1 = "открити, км".decode('utf-8')
        label2 = "общо, км".decode('utf-8')
        label3 = "Открити".decode('utf-8')
        label4 = "Общо".decode('utf-8')
        label5 = "*към октомври 2015".decode('utf-8')
        label6 = "Магистралите в България".decode('utf-8')
        label7 = "Прием в ЕС".decode('utf-8')
        suffix = "bg"
    elif bg == 0: #English labels
        label1 = "inaugurated, km"
        label2 = "total in use, km"
        label3 = "Inaugurated"
        label4 = "Total"
        label5 = "*as of October 2015"
        label6 = "Motorways in Bulgaria"
        label7 = "EU accession"
        suffix = "en"
    else: #Deutsch
        label1 = "fertiggestellt, km"
        label2 = "in Betrieb, km"
        label3 = "Fertiggestellt"
        label4 = "in Betrieb"
        label5 = "*Stand Oktober 2015"
        label6 = "Autobahnen in Bulgarien"
        label7 = "EU Beitritt"
        suffix = "de"
    
    color1 = 'b'
    color2 = 'g'
    
    fig1 = plt.figure(facecolor = 'k', frameon = False)
    ax1 = fig1.add_subplot(111)
    #ax1.set_axis_bgcolor('k')
    ax1.set_axis_bgcolor('1.0') #0.0 = черно, 1.0 = прозрачно
    
    inaugurated = ax1.bar(range(start_year,end_year), timeline, color = color1, width = 0.4)
    
    ax1.yaxis.set_label_coords(.05, 1.06)
    #plt.ylabel(label1, size = 30, rotation = 0, color = color1, fontstyle = 'italic')#, x = 0.1, y = 1.15)
    ax1.annotate(label1, xy=(0.02, 0.8),
                 xycoords='figure fraction', size=30, color=color1,
                 fontstyle='italic')
    plt.yticks(linspace(0,y_max1,6),size = 30, color = color1)
    ax1.set_ylim(0,y_max1)
    
    labels = range(start_year, end_year-1)
    labels.append("2015*")
    plt.xticks(arange(start_year,end_year)+0.0,labels, rotation = 45,size = 27)
    plt.tick_params(axis='x', bottom='off')
    ax1.tick_params(axis='y', right='off', left = 'off', top = 'off', bottom = 'off', length = 0.)
    
    ax1.set_axisbelow(True) #gridlines below data
    ax1.yaxis.grid(True, color = '0.65', ls = '-', lw = 1.5, zorder = 0) #horizontal gridlines
    
    ax2 = ax1.twinx()
    ax2.tick_params(axis='y', right='off', left = 'off', top = 'off', bottom = 'off', length = 0.)
    
    bar_cumul = ax2.bar(arange(start_year,end_year)+0.4, cumulative, color = color2, width = 0.4)
    
    ax2.set_ylim(0,y_max2)
    plt.xticks(arange(start_year,end_year)+0.0,labels, rotation = 45, size = 27, color = color2)
    #ax2.yaxis.set_label_coords(0.99, 1.19)
    #plt.ylabel(label2, size =30, rotation = 270, color = color2)
    #plt.ylabel(label2, size =30, rotation = 0, color = color2, fontstyle = 'italic')
    ax2.annotate(label2, xy=(0.976, 0.8),
                 xycoords='figure fraction', size=30, color=color2,
                 fontstyle='italic',
                 horizontalalignment = 'right')
    plt.yticks(linspace(0,y_max2, 6), size = 30, color = color2)
    
    #the legend
    #leg = ax1.legend((inaugurated[0], bar_cumul[0]), ('Открити'.decode('utf-8'), 'Общо'.decode('utf-8')), loc = 'upper left', fontsize=30)
    #leg = ax1.legend((inaugurated[0], bar_cumul[0]), (label3, label4), loc = 'upper left', fontsize=25, ncol = 2)
    #leg.draw_frame(False)
    
    plt.text(0.05, -.33,
            label5,
            fontsize=20,
            horizontalalignment='center',
            verticalalignment='center',
            transform=ax1.transAxes, 
            color = '0.35')
    
    # Turn off spines left, top, bottom and right (do it twice because of the twinning)
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    # We do want ticks on the bottom x-axis only
    ax1.xaxis.set_ticks_position('bottom')
    ax2.xaxis.set_ticks_position('bottom')
    
    #annotate
    ax1.annotate(label7, xy=(2006.9, 0), xytext=(2006.9, 0.9*y_max1), color='r',
                 arrowprops=dict(arrowstyle='-', edgecolor='r', ls='dashed',
                 relpos=(0,0)), fontsize=19, fontstyle='italic')
    
    #plt.title(label6, size = 38, x = 0.03, y = 1.25, horizontalalignment = 'left', textcoords = 'figure fraction')
    ax1.annotate(label6, xy=(0.02, 0.9),
                 xycoords='figure fraction', size=30,
                 horizontalalignment = 'left')
    
    fig1.subplots_adjust(top = 0.75, bottom = 0.23, left = 0.07, right = 0.92)
    
    fig1.set_size_inches(13.3,6)
    plt.savefig("highways_"+suffix+".svg", facecolor = '0.95') #1.0 = прозрачно, 0.0 = черно
    plt.close()
    #raw_inpu()

