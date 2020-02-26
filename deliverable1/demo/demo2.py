from matplotlib import pyplot as plt

x = [1,1.8,3,4,5,6.2,7]
y1 = [10,9.2,8.5,8.3,8.5,9.2,10]
y2 = [10,8.7,8,7.8,8,8.7,10]

# part 4
fig, ax1 = plt.subplots()
#fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(x,y1)
ax1.plot(x,y2)

# part 1 - set titles and labels - comment Ctrl+K,C -- uncomment Ctrl+K,U
ax1.set_title("very original new title")
ax1.set_xlabel("x-axis")
ax1.set_ylabel("y-axis")

# # part 2 - add circles and change view limit
# ax1.set_xlim((-2,10))
# ax1.set_ylim((5,15))
# c1 = plt.Circle((2, 11), 0.5, color="r")
# c2 = plt.Circle((6, 11), 0.5, color="r")
# c3 = plt.Circle((4,10), 4.5, color="k", fill=False) 
# ax1.add_artist(c1)
# ax1.add_artist(c2)
# ax1.add_artist(c3)

# # part 3 - arrows/annotations
# ax1.annotate("Poke here",
#              xy=(6, 11),
#              xytext=(9, 13),
#              arrowprops=dict(arrowstyle="fancy", connectionstyle="arc3,rad=-0.5"),
#              bbox=dict(boxstyle="round", fc="w"))

# # part 4 - 2 plots on 1 screen
# x2 = [1,2,3,4,5,6,7,8]
# y3 = [50000, 45000, 47500, 48000, 45000, 46000, 45600, 47000]

# ax2.set_ylabel("widgets made")
# ax2.set_xlabel("day")
# ax2.plot(x2, y3)
# ax2.set_ylim((43000,52000))

# part 4 - save to file
# fig.savefig('myfig.png')

plt.show()