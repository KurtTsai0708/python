#Which avocado size is most popular?

import matplotlib.pyplot as plt
print(avocados.head())

nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
nb_sold_by_size.plot(kind = "bar")

plt.show()

#Changes in sales over time

import matplotlib.pyplot as plt

nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
nb_sold_by_date.plot(kind="line")

plt.show()

#Avocado supply and demand

avocados.plot(x = "nb_sold",y = "avg_price", kind = "scatter", title = "Number of avocados sold vs. average price")

plt.show()

#Price of conventional vs. organic avocados

avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

plt.legend(["conventional", "organic"])
plt.show()

