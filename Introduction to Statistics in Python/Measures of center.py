#Mean and median

import numpy as np

be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

be_and_usa = food_consumption[(food_consumption['country'] == "Belgium") | (food_consumption['country'] == 'USA')]
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))

#Mean vs. median

import matplotlib.pyplot as plt

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
rice_consumption['co2_emission'].hist()
plt.show()

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))