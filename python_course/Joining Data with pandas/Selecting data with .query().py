#Subsetting rows with .query()

gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

recent_gdp_pop.plot(rot=90)
plt.show()