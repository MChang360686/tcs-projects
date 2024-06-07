import matplotlib.pyplot as plt

x = [1, 3, 4]
y = [1, 2, 3]

x_2 = [1, 3, 6]
y_2 = [2, 6, 8]

x_3 = [1, 2, 3, 4, 5]
y_3 = [10, 23, 15, 66, 13]

x_4 = [1, 2, 3]
y_4 = [1, 2, 3]

#plt.plot(x, y, color="red", linestyle="dotted", marker='o', markerfacecolor="green", markersize=12)
#plt.plot(x_2, y_2, label="line 2")
plt.bar(x_3, y_3)
#plt.scatter(x_4, y_4, label='stars', color='red')
#plt.xlabel("x axis")
#plt.ylabel("y axis")
#plt.title("Basic Graph")
plt.show()