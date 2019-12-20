import matplotlib.pyplot as plt
x = ['a', 'b', 'c', 'd', 'e']
y = [50, 72, 25, 67, 90]
plt.bar(x, y, label = 'grade', color = 'k')

plt.title('This is a line chart')
plt.xlabel('students)')
plt.ylabel('grade')
plt.legend()
plt.show()
