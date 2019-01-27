# Libraries
import matplotlib.pyplot as plt

# Make data: I have 3 groups and 7 subgroups
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_size = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
dates=[]
daygroups=[]
daygroups_size=[]
week1_size=[]
week2_size=[]
week3_size=[]
week4_size=[]
week5_size=[]

day_date_group=[]
group_string=""
for i in range(1,32):
    dates.append(str(i))

for i in months:
    for j in days:
        daygroups.append(j)
        daygroups_size.append(1)
        week1_size.append(1)
        week2_size.append(1)
        week3_size.append(1)
        week4_size.append(1)
        week5_size.append(1)

# print(dates)
print(daygroups)

# subgroup_names = ['A.1', 'A.2', 'A.3', 'B.1', 'B.2', 'C.1', 'C.2', 'C.3', 'C.4', 'C.5']
# subgroup_size = [4, 3, 5, 6, 5, 10, 5, 5, 4, 6]

# group_string=""
# for i in range(len(months)):
#     for j in dates:
#         group_string = ""
#         if(i==1):
#             if(int(j)<=29):
#                 group_string+=months[i]+"."+days[int(j)%7]+"."+j
#                 day_date_group.append(group_string)
#             else:
#                 continue
#
#
#
# #separate counter needed for date-day mapping
#         if(i==3 or i==5 or i==8 or i==10):
#             if(int(j)<=30):
#                 group_string+=months[i]+"."+days[int(j)%7]+"."+j
#                 day_date_group.append(group_string)
#
# print(day_date_group)

mypie_textprops=dict(verticalalignment='center',horizontalalignment='center')
# mypie_wedgeprops=dict(label=months)
#
# # Create colors
a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]
#
# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(month_size, radius=3, labels=months,labeldistance=1.1,colors=[a(0.6), b(0.6), c(0.6)], startangle=90, counterclock=False)
plt.setp(mypie, width=0.3, edgecolor='white')

# Second Ring (Inside)
mypie2, temp = ax.pie(daygroups_size, radius=2.7,labels=daygroups,labeldistance=0.8,rotatelabels=True,startangle=90,counterclock=False, textprops=mypie_textprops)
plt.setp(mypie2, width=1, edgecolor='white')


mypie3, temp = ax.pie(week1_size, radius=1.7,startangle=90,counterclock=False)
plt.setp(mypie3, width=0.1, edgecolor='white')
#
# mypie4, temp = ax.pie(week2_size, radius=0.4,startangle=90,counterclock=False)
# plt.setp(mypie2, width=0.1, edgecolor='white')
#
# mypie5, temp = ax.pie(week3_size, radius=0.4,startangle=90,counterclock=False)
# plt.setp(mypie2, width=0.1, edgecolor='white')
#
# mypie6, temp = ax.pie(week4_size, radius=0.2,startangle=90,counterclock=False)
# plt.setp(mypie2, width=0.1, edgecolor='white')
#
# mypie7, temp = ax.pie(week5_size, radius=0.1,startangle=90,counterclock=False)
# plt.setp(mypie2, width=0.1, edgecolor='white')

plt.margins(0, 0)
print(mypie2[0])

# show it
plt.subplots_adjust(top=0.65,bottom=0.3)
plt.show()