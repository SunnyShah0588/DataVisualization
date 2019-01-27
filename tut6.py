import matplotlib.pyplot as plt

days=[1,2,3,4,5]
sleeping=[7,8,6,10,9]
eating=[2,3,1,1,2]
working=[10,12,7,8,10]
playing=[2,1,3,2,4]

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
colors=['b','g','r','y']

plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        explode=[0,0.05,0,0],
        autopct='%1.2f%%')

# plt.xlabel("Plot Number")
# plt.ylabel("Plot Value")
plt.title("Demo Graph \ntutorials")
# plt.legend()

plt.show()