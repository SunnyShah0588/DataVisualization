import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import datetime as dt
import pandas as pd
import math
from mpl_finance import candlestick_ohlc
from matplotlib import style

style.use('ggplot')
# print(plt.style.available)

def onclick(event):
    # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
    #       ('double' if event.dblclick else 'single', event.button,
    #        event.x, event.y, event.xdata, event.ydata))

    update_ax3(mdates.num2date(event.xdata))

# def moving_average(values, window):
#     weights = np.repeat(1.0, window) / window
#     smas = np.convolve(values,weights,'valid')
#     return smas

def convert_date(date_bytes):
    return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))

def update_ax3(data):
    ax3.cla()
    print(data)
    dint = mdates.date2num(data)
    dintmin = math.floor(dint - 15)
    dintmax = math.floor(dint + 15)
    # print(mdates.num2date(dintmin),mdates.num2date(dintmax))
    d1 = []
    flag=0
    for i in range(len(d)):
        if(d[i] > dintmin):
            flag = 1
            istart = i
            d1.append(d[i])
        if(d[i] > dintmax):
            iend = i
            break
    # print(istart - len(d1),iend)
    # print(d[istart - len(d1)])
    istart = iend - len(d1) + 1
    # print(istart,iend)
    # print(len(d1))

    ohlc_selected = []

    for i in range(istart,iend + 1):
        append_me = d[i], o[i], h[i], l[i], c[i]
        ohlc_selected.append(append_me)

    candlestick_ohlc(ax3, ohlc_selected, width=0.4, colorup='g', colordown='r')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))
    plt.show()
    #you have start and end index for date, start from there


d,o,h,l,c,p=np.loadtxt('../Data/GSPC_RAW_change.csv',delimiter=',',unpack=True,converters={0:convert_date})

d1=[]
p1=[]

start_date_string = "01-01-2016"
end_date_string = "31-12-2017"

start_date = dt.datetime.strptime(start_date_string, "%d-%m-%Y")
end_date = dt.datetime.strptime(end_date_string, "%d-%m-%Y")

i_int_start_date = mdates.date2num(start_date)
i_int_end_date = mdates.date2num(end_date)

for i in range(len(d)):
    if d[i]>i_int_start_date and d[i]<i_int_end_date:
        d1.append(d[i])
        p1.append(p[i])

print("D,P",len(d1),len(p1))

# d1 = dt.datetime.strptime(d[0], "%d-%m-%y")
# d1 = d1.date()
# print(mdates.num2date(d[0]))

i=0
y=len(d1)
# ohlc=[]

# while(i < y):
#     append_me = d[i],o[i],h[i],l[i],c[i]
#     ohlc.append(append_me)
#     i+=1


fig = plt.figure()

# ax1 = plt.subplot2grid((10,1),(0,0),rowspan=3, colspan=1)
# plt.title("Demo Graph \ntutorials")
# plt.xlabel("Date")
# plt.ylabel("S&P 500 OHLC")
ax2 = plt.subplot2grid((10,1),(0,0),rowspan=4, colspan=1)
plt.xlabel("Date")
plt.ylabel("S&P 500 Percent change")
ax3 = plt.subplot2grid((10,1),(6,0),rowspan=4, colspan=1)

# candlestick_ohlc(ax1,ohlc,width=0.4,colorup='g',colordown='r')

close = '{:.2f}'.format(c[-1])
# print(close)
bbox_prop = dict(boxstyle='larrow')
ax2.annotate('Last Price\n' + str(close),(d[-1],c[-1]),
            xytext=(d[-1] + 30, c[-1] - 20),
            bbox=bbox_prop)


# d1=d
# d2=d

# print(type(p))
d2 = np.asarray(d1)
p2 = np.asarray(p1)

# ax1.plot_date(d[-start:],ma1[-start:])
# ax1.plot_date(d[-start:],ma2[-start:])
ax2.plot_date(d2,p2,'-',linewidth=0.5,color='k')
# ax3.plot_date(d2,h)

ax2.fill_between(d2,p2,0,where=(p2>0),facecolor='g',edgecolor='g',alpha=0.5)
ax2.fill_between(d2,p2,0,where=(p2<0),facecolor='r',edgecolor='r',alpha=0.5)

# for label in ax1.xaxis.get_ticklabels():
#     label.set_rotation(45)

for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)
#
# for label in ax3.xaxis.get_ticklabels():
#     label.set_rotation(45)
# ax1.xaxis.set_major_locator(mtick.MaxNLocator(5))

# ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))



cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
