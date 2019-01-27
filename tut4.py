import matplotlib.pyplot as plt
#<<<----------------------------------------------------->>>
'''tutorial 1'''
# x=[1,2,3]
# y=[10,30,20]

'''tutorial 2'''
# x2=[1,2,3]
# y2=[40,20,35]

'''tutorial 3'''
# x3=[2,4,6,8,10]
# y3=[40,20,80,100,60]

# x4=[1,3,5,7,9]
# y4=[30,70,10,90,50]
# age=[22,55,62,45,21,22,34,42,4,9,99,110,75,82,87]
#not needed for histogram
# id=[x for x in range(len(age))]
# bins=[0,10,20,30,40,50,60,70,80,90,100,110,120]

'''tutorial 4'''
x5=[1,2,3,4,5,6,7,8]
y5=[70,50,30,10,80,20,60,40]

#<<<<------------------------------------------------------------------>>>
#tutorial 1
# plt.plot(x,y,label="plot1")

#tutorial 2
# plt.plot(x2,y2,label="plot2")

#tutorial 3
# plt.bar(x3,y3,label="bar", color="red")
# plt.bar(x4,y4,label="bar2", color="green")

# plt.hist(age, bins,  histtype="bar", rwidth=0.8)

#tutorial 4
plt.scatter(x5,y5,label="skitskat",color='k', marker='*', s=500) #s=size

#<<<--------------------------------------------------------------------->>>
plt.xlabel("Plot Number")
plt.ylabel("Plot Value")
plt.title("Demo Graph \ntutorials")
plt.legend()

plt.show()