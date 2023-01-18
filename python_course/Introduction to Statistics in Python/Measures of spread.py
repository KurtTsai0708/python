#Quartiles, quantiles, and quintiles

print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))
print(np.quantile(food_consumption["co2_emission"],[0,0.2,0.4,0.6,0.8,1]))
print(np.quantile(food_consumption["co2_emission"],
                    [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]))


#Variance and standard deviation

print(food_consumption.groupby("food_category")["co2_emission"].agg([np.var,np.std]))

import matplotlib.pyplot as plt

food_consumption[food_consumption["food_category"]=="beef"]["co2_emission"].hist()
plt.show()

food_consumption[food_consumption["food_category"]=="eggs"]["co2_emission"].hist()
plt.show()


#Finding outliers using IQR

emissions_by_country = food_consumption.groupby("country")["co2_emission"].sum()
print(emissions_by_country)

q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)