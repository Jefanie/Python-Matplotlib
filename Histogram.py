import pandas as pd
df = pd.read_excel('3_histogram_grade.xlsx', sheet_name=0)
#print(df)
math_grade = df['Math grade'].tolist()
print(math_grade)

import matplotlib.pyplot as plt

y = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(math_grade, y, histtype='bar', rwidth=0.8)

plt.title('Histogram')
plt.ylabel('Frequency')
plt.xlabel('Bins')
plt.legend()
plt.show()
