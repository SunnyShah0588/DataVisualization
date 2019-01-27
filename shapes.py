import matplotlib.pyplot as plt
import matplotlib.path
import matplotlib.patches as mpatch

fig, ax = plt.subplots()

rectangles = {'skinny' : mpatch.Rectangle((2,2), 8, 2),
              'square' : mpatch.Rectangle((4,6), 6, 6)}
l=len(rectangles) + 1
i=1

#reference for text in shape

# for r in rectangles:
#     # print("R",r,r.index(r))
#     ax.add_artist(rectangles[r])
#     rx, ry = rectangles[r].get_xy()
#     cx = rx + rectangles[r].get_width()/2.0
#     cy = ry + rectangles[r].get_height()/2.0
#
#     ax.annotate(r, (cx, cy), color='w', weight='bold',
#                 fontsize=6, ha='center', va='center')

#reference for multiple text in shape

# for r in rectangles:
#     # print("R",r,r.index(r))
#     ax.add_artist(rectangles[r])
#     for i in range(1,l):
#         rx, ry = rectangles[r].get_xy()
#         cx = rx + ((rectangles[r].get_width()/l) * i)
#         cy = ry + ((rectangles[r].get_height()/l) * i)
#
#         ax.annotate(r, (cx, cy), color='w', weight='bold',
#                     fontsize=6, ha='center', va='center')



ax.set_xlim((0, 15))
ax.set_ylim((0, 15))
ax.set_aspect('equal')
plt.show()