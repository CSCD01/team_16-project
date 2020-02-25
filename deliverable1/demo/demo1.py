from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,4,6,7,5,6,5,6]

# plt.xkcd()
# part 1 - comment Ctrl+K,C -- uncomment Ctrl+K,U
plt.plot(x, y)#, label="first line")

# part 2 - title and labels
# plt.title('wow, such graph, much exciting')
# plt.xlabel('days')
# plt.ylabel('units of work done')

# part 3 - add second line
# y2 = [5,7,9,10,9,11,10,7]
# plt.plot(x, y2, label="second line")
# plt.legend()

plt.show()