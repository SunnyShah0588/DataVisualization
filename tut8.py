import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

def convert_date(date_bytes):
    return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))

x,y=np.loadtxt('../Data/GSPC_2Years_RAW.csv',delimiter=',',unpack=True,converters={0:convert_date})

fig = plt.figure()
ax = plt.subplot2grid((1,1),(0,0))

# plt.plot_date(x,y,'-')
ax.plot_date(x,y,'-', label="S&P 500 data Time Series",color='k')

for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)

ax.grid(True,color='g',linestyle='-')

ax.plot([],[],label="loss",color='r',alpha=0.5)
ax.plot([],[],label="profit",color='g',alpha=0.5)
ax.axhline(y=1750, color='k', linewidth=1)

ax.fill_between(x,y,1750,where=(y > 1750),facecolor='g',alpha=0.5)
ax.fill_between(x,y,1750,where=(y < 1750),facecolor='r',alpha=0.5)

ax.spines['left'].set_color('b')
ax.spines['left'].set_linewidth(5)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.tick_params(axis='x')

# ax.xaxis.label.set_color('b')
# ax.yaxis.label.set_color('b')
# ax2.set_yticks([0,25,50,75])    #only the specified values wll be visible

plt.subplots_adjust(left=0.15, bottom=0.18, right=0.94, top=0.80, wspace=0.2, hspace=0)
plt.xlabel("Date")
plt.ylabel("S&P 500 Index")
plt.title("Demo Graph \ntutorials")
plt.legend()
plt.show()