import pandas as pd
df = pd.read_excel('3_histogram_grade.xlsx', sheet_name=0)
#print(df)
math_grade = df['Math grade'].tolist()
print(math_grade)
stu_ID = [x for x in range(len(math_grade))]

import matplotlib.pyplot as plt
plt.axis([0, 25, 0, 100])
plt.scatter(stu_ID, math_grade, label='Math Label', color='b', marker='*', s=10)

y = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(math_grade, y, histtype='bar', rwidth=0.8)

plt.title('Scatter Plot')
plt.ylabel('scores')
plt.xlabel('stu_ID')
plt.legend()
plt.show()
