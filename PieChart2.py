import csv
col1 = []
col2 = []

with open('5_CN.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #print(plots)
    next(plots)
    for row in plots:
        col1.append(row[0])
        col2.append(row[1])
print(col1)
print(col2)

import matplotlib.pyplot as plt
plt.pie(col2, labels=col1)

plt.title('pie chart')
plt.show()
