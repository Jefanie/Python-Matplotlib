import csv
row1 = []
row2 = []

with open('5_CN.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #print(plots)
    for row in plots:
        if row[0] == 'Date':
                row1 = row[1:]
        if row[0] == '2018/10/1':
                row2 = row[1:]
print(row1)
print(row2)

import matplotlib.pyplot as plt
plt.pie(row2, labels=row1)

plt.title('pie chart')
plt.show()
