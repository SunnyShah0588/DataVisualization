from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt

# Number of possibly sharp edges
n = 8
# magnitude of the perturbation from the unit circle, should be between 0 and 1
r = .2
# number of points in the Path
N = n*3+1
# There is the initial point and 3 points per cubic bezier curve. Thus, the curve will only pass though n points,
# which will be the sharp edges, the other 2 modify the shape of the bezier curve

angles = np.linspace(0,2*np.pi,N)
# print("ANGLES: ",angles)
codes = np.full(N,Path.CURVE4)
# print("CODES: ",codes)
codes[0] = Path.MOVETO
# print("CODES: ",codes)

# print("SIN: ", np.sin(angles))
# print("COS: ",np.cos(angles))
verts = np.stack((np.cos(angles),np.sin(angles)))
# print("VERTS: ",verts)
# print("VERTS T: ",verts.T)
verts1 = verts.T*(2*r*np.random.random(N)+1-r)[:,None]
# print("VERTS1: ",verts1)
# np.append(verts,verts[0])
verts1[-1,:] = verts1[0,:] # Using this instad of Path.CLOSEPOLY avoids an innecessary straight line
# print("VERTS1: ",verts1)
path = Path(verts1, codes)
print("PATH: ",path)

xy = path.get_extents().get_points()
# print(xy)
width = xy[1][0] - xy[0][0]
height = xy[1][1] - xy[0][1]

xpos = xy[1][0] + (width/2)
ypos = xy[0][1] + (height/2)


fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax.add_patch(patch)

ax.set_xlim(np.min(verts1)*1.1, np.max(verts1)*1.1)
ax.set_ylim(np.min(verts1)*1.1, np.max(verts1)*1.1)
# ax.axis('off') # removes the axis to leave only the shape

plt.show()