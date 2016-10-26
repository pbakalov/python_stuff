#coding=utf-8

###some things borrowed from https://stackoverflow.com/questions/29859565/create-the-economist-style-graphs-from-python
import matplotlib.pylab as plt
import matplotlib
matplotlib.rc('font', family='Arial') #нужно на OS X, за да се изобразява българския
from numpy import zeros, arange, linspace, array
plt.ion()
plt.xkcd()

bansko= [[1,58],
[2,112],
[3,170],
[4,224],
[5,280],
[6,340],
[9,500],
[13,700],
[20,800],
[100,1500]]

kuehtai= [[1  ,36],
[2  ,71],
[3  ,104],
[4  ,133],
[5  ,162],
[6  ,188],
[7  ,213],
[8  ,237],
[9  ,257],
[10 ,279],
[11 ,299],
[12 ,318],
[13 ,333],
[14 ,349],
[140,430]]

zillertal= [[1  ,49.5 ],
[2  ,97.5 ],
[2.5,116.5],
[3  ,136.5],
[3.5,156.5],
[4  ,170.5],
[5  ,204  ],
[6  ,237  ],
[7  ,268.5],
[8  ,298.5],
[9  ,327  ],
[10 ,356.5],
[11 ,384  ],
[12 ,410.5],
[13 ,437  ],
[14 ,463.5],
[15 ,488  ]]

vallees = [[1, 59],
[2, 115   ],
[3, 171   ],
[4, 225   ],
[5, 274   ],
[6, 289   ],
[7, 335   ],
[8, 381   ],
[9, 427   ],
[10, 473  ],
[11, 519  ],
[12, 565  ],
[13, 611  ],
[14, 657  ],
[140, 1240]]

alpedhuez =  [[1, 49.50 ],
[2, 97.50 ],
[3, 142.00],
[4, 182.50],
[5, 221.00],
[6, 255.00],
[7, 288.00],
[8, 288+ 32.00],
[9, 288+ 2*32.00],
[10, 288+ 3*32.00],
[11, 288+ 4*32.00],
[12, 288+ 5*32.00],
[13, 288+ 6*32.00],
[14, 288+ 7*32.00]]

symbols = ['o', 'x', 'd', 'v', '>', '^', '-o', '-x']
colors = ["b", "g", "r", "c", "m", "y", "k"]

names = ["Банско".decode('utf-8'),
"Kuehtai",
"Zillertal",
"3 Vallees",
"Alpe d'Huez"]

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
for i,resort in enumerate([bansko, kuehtai, zillertal, vallees, alpedhuez]):
    x = []
    y = []
    for pair in resort:
        if pair[0]<=15:
            x.append(pair[0])
            y.append(pair[1]*1./pair[0])
            #print y[-1]/y[0]
        else:
            break
    print "\n"
    if i == 0:
        plt.plot(x,array(y)/y[0], '-'+symbols[i], label = names[i], linewidth = 3, markersize = 10)
    else:
        plt.plot(x,array(y)/y[0], '-'+symbols[i], color = 'grey', label = names[i], linewidth = 3, markersize = 10, alpha = 0.5)
    plt.xlim(.5,15.5)
    plt.ylim(.5,1.03)
    plt.xlabel("Продължителност на картата/дни".decode('utf-8'), size = 30)
    plt.ylabel("Еквивалентна цена на ден/цена \nна еднодневна карта".decode('utf-8'), size = 30)
    plt.xticks(size = 27)
    plt.yticks(linspace(.5,1.,3), size = 27)
    plt.title("Цени на многодневни карти спрямо\nцената на еднодневна карта\nв Банско и някои други курорти".decode('utf-8'), size = 30, x = 0.5, y = 1.05)#, horizontalalignment = 'left')

fig1.subplots_adjust(top = 0.8, bottom = 0.15, left = 0.22, right = 0.9)

ax1.annotate("Сезон 2015/16".decode('utf-8') , xy=(0.72, 0.16),
             xycoords='figure fraction', size=15, #color=color1,
             fontstyle='italic')
ax1.annotate("Данни и източници: https://gist.github.com/pbakalov/33c019970422553a1c66".decode('utf-8') , xy=(0.02, 0.02),
             xycoords='figure fraction', size=15, #color=color1,
             fontstyle='italic')
leg = ax1.legend(loc = 'best' , fontsize=25)
leg.draw_frame(False)
fig1.set_size_inches(9.,9.)
plt.savefig("bansko_ceni.svg", facecolor = '.95') #1.0 = прозрачно, 0.0 = черно
#plt.savefig("bansko_ceni.jpg", facecolor = '.95') #1.0 = прозрачно, 0.0 = черно

