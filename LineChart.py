import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [5, 7, 2]
z = [6, 3, 1]
plt.plot(x, y, '--b', label = 'Line A')
plt.plot(x, z, '--+k', label = 'Line B')

plt.title('This is a line chart')
plt.xlabel('Time (hours)')
plt.ylabel('Distance (miles)')
plt.legend()
plt.show()
