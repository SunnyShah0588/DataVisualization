# Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import colors as mcolors
import datetime as dt
from matplotlib.widgets import Button
import stage1_1_date_map
import stage1_1_color_map

# year = 2015

class Year(object):
    year=2016

    def update_year(self,event):
        # print(event)
        self.year = ((self.year + 1) % 2) + 2016
        print("Hi2")
        plot_data(self.year)


def convert_date(date_bytes):
    return mdates.strpdate2num('%d-%m-%y')(date_bytes.decode('utf-8'))


def plot_data(year):
    ax.cla()
    # year = ((year + 1) % 2) + 2016
    year_start_date_string="01-01-"+str(year)
    year_end_date_string="31-12-"+str(year)
    # tmp_date_string="29-02-"+str(year)
    year_start_date=dt.datetime.strptime(year_start_date_string,"%d-%m-%Y")
    year_end_date=dt.datetime.strptime(year_end_date_string,"%d-%m-%Y")
    # tmp_date=dt.datetime.strptime(tmp_date_string,"%d-%m-%Y")


    # print(mdates.num2date(mdates.date2num(year_start_date) + 1))
    day=[]
    i_int_start_date=mdates.date2num(year_start_date)
    i_int_end_date=mdates.date2num(year_end_date)
    # i_tmp_date=mdates.date2num(tmp_date)
    i_int_day=year_start_date.weekday()

    stage1_1_date_map.year_week_calculator(i_int_start_date,i_int_end_date,i_int_day,week1,week2,week3,week4,week5,week6)
    # stage1_1_date_map.year_week_calculator(i_int_start_date,i_tmp_date,i_int_day,week1,week2,week3,week4,week5,week6)
    # print(week1)
    # print(week2)
    # print(week3)
    # print(week4)
    # print(week5)
    # print(week6)

    # stage1_1_color_map.day_color_map(week1,week1_color)
    # stage1_1_color_map.day_color_map(week2,week2_color)
    # stage1_1_color_map.day_color_map(week3,week3_color)
    # stage1_1_color_map.day_color_map(week4,week4_color)
    # stage1_1_color_map.day_color_map(week5,week5_color)
    # stage1_1_color_map.day_color_map(week6,week6_color)


    d1=[]
    p1=[]
    n1=[]
    # print(len(d))
    for i in range(len(d)):
        date0 = mdates.num2date(d[i])
        # print(date0.year)
        date0_year = date0.year
        if(date0_year == year):
            d1.append(date0)
            p1.append(p[i])
            n1.append(n[i])

    stage1_1_color_map.day_color_map(week1,week1_color,d1,p1,n1)
    stage1_1_color_map.day_color_map(week2,week2_color,d1,p1,n1)
    stage1_1_color_map.day_color_map(week3,week3_color,d1,p1,n1)
    stage1_1_color_map.day_color_map(week4,week4_color,d1,p1,n1)
    stage1_1_color_map.day_color_map(week5,week5_color,d1,p1,n1)
    stage1_1_color_map.day_color_map(week6,week6_color,d1,p1,n1)

    # print(p1[0],p1[len(p1)-1])
    # print(d1[0],d1[0].day,d1[0].month,d1[0].year,d1[0].weekday())
    # print(len(week1_size))
    mypie_textprops=dict(verticalalignment='center',horizontalalignment='center',fontsize='small')
    # mypie_wedgeprops=dict(label=months)
    #
    # # Create colors
    # a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
    #
    # First Ring (outside)



    mypie= ax.pie(month_size, radius=3, labels=months,labeldistance=1.1,colors=['#000000'], startangle=90, counterclock=False)
    # print("mypie[0]",mypie[0])
    plt.setp(mypie[0], width=0.3, edgecolor='white')

    # for pie in mypie[0]:
    #     pie.set_picker(True)

    # print(mypie)

    # Second Ring (Inside)
    mypie2, temp = ax.pie(daygroups_size, radius=2.7,labels=daygroups,labeldistance=0.9,colors='c',rotatelabels=True,startangle=90,counterclock=False, textprops=mypie_textprops)
    plt.setp(mypie2, width=0.5, edgecolor='white')

    #need to create a separate array for coloring each slice
    mypie3, temp = ax.pie(week1_size, radius=2.2,startangle=90,counterclock=False,colors=week1_color)
    plt.setp(mypie3, width=0.2, edgecolor='white')
    #
    mypie4, temp = ax.pie(week2_size, radius=2,startangle=90,counterclock=False,colors=week2_color)
    plt.setp(mypie4, width=0.2, edgecolor='white')

    mypie5, temp = ax.pie(week3_size, radius=1.8,startangle=90,counterclock=False,colors=week3_color)
    plt.setp(mypie5, width=0.2, edgecolor='white')

    mypie6, temp = ax.pie(week4_size, radius=1.6,startangle=90,counterclock=False,colors=week4_color)
    plt.setp(mypie6, width=0.2, edgecolor='white')
    #
    mypie7, temp = ax.pie(week5_size, radius=1.4,startangle=90,counterclock=False,colors=week5_color)
    plt.setp(mypie7, width=0.2, edgecolor='white')

    mypie8, temp = ax.pie(week6_size, radius=1.2,startangle=90,counterclock=False,colors=week6_color)
    plt.setp(mypie8, width=0.2, edgecolor='white')

    plt.margins(0, 0)
    # print(mypie2[0])

    ax_new = plt.axes([0.85, 0.05, 0.1, 0.075])
    ax_new.cla()
    button_year = Button(ax_new,year)
    # new_year = ((year + 1) % 2) + 2016
    button_year.on_clicked(callback.update_year)
    print("Hi3")
    def onclick(event1):
        print(event1)
        for pie in mypie[0]:
            hit,_= pie.contains(event1)
            if(hit):
                # ctr = ctr + 1
                print(pie.get_label())

        month_figure.canvas.mpl_disconnect(cid)


    # show it
    print("Hi4")
    month_figure = mypie[0][0].figure
    plt.subplots_adjust(top=0.65,bottom=0.3)
    cid = month_figure.canvas.mpl_connect('button_press_event', onclick)
    plt.show()


colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
# print(colors)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_size = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dates=[]
daygroups=[]
daygroups_size=[]
week1=[]
week2=[]
week3=[]
week4=[]
week5=[]
week6=[]
week1_size=[]
week2_size=[]
week3_size=[]
week4_size=[]
week5_size=[]
week6_size=[]
week1_color=[]
week2_color=[]
week3_color=[]
week4_color=[]
week5_color=[]
week6_color=[]

day_date_group=[]
group_string=""

for i in months:
    for j in days:
        daygroups.append(j[:3])
        daygroups_size.append(1)
        dates.append(0)
        week1_size.append(1)
        week1.append([])
        week1_color.append([])
        week2_size.append(1)
        week2.append([])
        week2_color.append([])
        week3_size.append(1)
        week3.append([])
        week3_color.append([])
        week4_size.append(1)
        week4.append([])
        week4_color.append([])
        week5_size.append(1)
        week5.append([])
        week5_color.append([])
        week6_size.append(1)
        week6.append([])
        week6_color.append([])



callback = Year()

d,o,h,l,c,p,n=np.loadtxt('../Data/GSPC_RAW_change_1.csv',delimiter=',',unpack=True,converters={0:convert_date})
fig, ax = plt.subplots()
ax.axis('equal')

plot_data(2016)