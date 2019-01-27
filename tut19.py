import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import datetime as dt

from mpl_finance import candlestick_ohlc
from matplotlib import style

MA1=10
MA2=30

style.use('ggplot')
# print(plt.style.available)

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values,weights,'valid')
    return smas

def convert_date(date_bytes):
    return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))

d,o,h,l,c=np.loadtxt('../Data/GSPC_2Years_RAW_OHLC.csv',delimiter=',',unpack=True,converters={0:convert_date})

i=0
y=len(d)
ohlc=[]

while(i < y):
    append_me = d[i],o[i],h[i],l[i],c[i]
    ohlc.append(append_me)
    i+=1

ma1 = moving_average(c,MA1)
ma2 = moving_average(c,MA2)
start = len(d[MA2-1:])
# print(ma1[-start],ma2[-start],c[-start])

fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
# ax3 = fig.add_subplot(222)


ax1 = plt.subplot2grid((8,1),(0,0),rowspan=3, colspan=1)
plt.title("Demo Graph \ntutorials")
ax2 = plt.subplot2grid((8,1),(4,0),rowspan=3, colspan=1)
candlestick_ohlc(ax1,ohlc,width=0.4,colorup='g',colordown='r')

close = '{:.2f}'.format(c[-1])
# print(close)
bbox_prop = dict(boxstyle='larrow')
ax2.annotate('Last Price\n' + str(close),(d[-1],c[-1]),
            xytext=(d[-1] + 30, c[-1] - 20),
            bbox=bbox_prop)


# d1=d
# d2=d

# ax1.plot_date(d[-start:],ma1[-start:])
# ax1.plot_date(d[-start:],ma2[-start:])
ax2.plot_date(d,c)
# ax3.plot_date(d2,h)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)
#
# for label in ax3.xaxis.get_ticklabels():
#     label.set_rotation(45)
# ax1.xaxis.set_major_locator(mtick.MaxNLocator(5))
# ax2.xaxis.set_major_locator(mtick.MaxNLocator(5))
# ax2.xaxis.set_major_locator(mtick.MaxNLocator(10))
#
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
# ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))
# ax3.xaxis.set_major_formatter(mdates.DateFormatter('%m/%y'))

plt.xlabel("Date")
plt.ylabel("S&P 500 Index")

plt.show()