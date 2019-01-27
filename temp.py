import numpy as np

a=[[1,2,3,4,5,6,7,8,9,10,
   11, 12], [13, 14, 15, 16, 17, 18, 19, 20,
   21, 22, 23, 24, 25]]
b=np.asfarray(a)
# a=[1,2,3,4,5]
# if(a.index(6)==1):
#     print("yes")
# else:
#     print("no")

# print(np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. ))
# print(np.sin(np.array(( 120., 135., 150., 180.)) * np.pi / 180. ))
# print(np.sin(np.array(( 210., 225., 240., 270.)) * np.pi / 180. ))
# print(np.sin(np.array(( 300., 330., 345., 360.)) * np.pi / 180. ))
# c=b.T*(2*0.2*np.random.random(25)+1-0.2)[:,None]
print(b,b.T)