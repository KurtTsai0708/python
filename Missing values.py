#Finding missing values

import matplotlib.pyplot as plt
print(avocados_2016.isna())
print(avocados_2016.isna().any())

avocados_2016.isna().sum().plot(kind="bar")
plt.show()

#Removing missing values

avocados_complete = avocados_2016.dropna()
print(avocados_complete.isna().any())

#Replacing missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()