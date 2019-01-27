import matplotlib.pyplot as plt
import numpy as np

import csv
import datetime
import matplotlib.dates as mdates
#
x=[]
y=[]
#
with open('../Data/GSPC_2years.csv','r') as csvfile:
    plots=csv.reader(csvfile, delimiter=',')
    # print(plots)
    for row in plots:
        if(row[0]=='Date'):
            continue
        d = datetime.datetime.strptime(row[0], "%d-%m-%y")
        d = d.date()
        x.append(datetime.datetime.strftime(d, '%d-%m-%y'))
        y.append(float(row[4]))

# md = mdates.strpdate2num('%d-%m-%y').
#
# print(md)
# d, o, h, l, c, ac, v = np.loadtxt('../Data/GSPC_RAW.csv', delimiter=',', unpack = True)

# print(d)

# print(yearmax,yearmin)

years = mdates.YearLocator()
months = mdates.MonthLocator()
yearsfmt = mdates.DateFormatter("%y")

fig, ax = plt.subplots()
ax.plot(x,y,'-',label="S&P 500 Time series")

# print(x)

# ax.xaxis.set_major_locator(years)
# ax.xaxis.set_major_formatter(yearsfmt)
# ax.xaxis.set_minor_locator(months)
# # ax.set_xlim(2013,2018)
# ax.format_xdata = mdates.DateFormatter('%d-%m-%y')
print(ax.format_xdata)
# fig.autofmt_xdate()
#
# plt.xlabel("Date")
# plt.ylabel("S&P 500 Index")
# plt.title("Demo Graph \ntutorials")
# plt.legend()
#
# plt.show()