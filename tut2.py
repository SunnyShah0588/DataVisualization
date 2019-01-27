import matplotlib.pyplot as plt

x=[1,2,3]
y=[10,30,20]

x2=[1,2,3]
y2=[40,20,35]

plt.plot(x,y,label="plot1")
plt.plot(x2,y2,label="plot2")

plt.xlabel("Plot Number")
plt.ylabel("Plot Value")
plt.title("Demo Graph \ntutorial 2")
plt.legend()

plt.show()