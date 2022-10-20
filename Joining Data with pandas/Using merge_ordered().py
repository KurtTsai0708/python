#Correlation between GDP and S&P500

gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')
gdp_returns = gdp_sp500[['gdp','returns']] 
print(gdp_returns.corr())          


#Phillips curve using merge_ordered()

inflation_unemploy = pd.merge_ordered(inflation,unemployment,on="date",
                                    how="inner")
print(inflation_unemploy) 

inflation_unemploy.plot(kind= "scatter" ,x = "unemployment_rate",y = "cpi",)
plt.show()

#merge_ordered() caution, multiple columns

date_ctry = pd.merge_ordered(gdp, pop, on=['country','date'], 
                             fill_method='ffill')
print(date_ctry)                             