#Pivot temperature by city and year

temperatures["year"] = temperatures["date"].dt.year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c",index = ["country","city"], columns = "year")
print(temp_by_country_city_vs_year)

#Subsetting pivot tables

temp_by_country_city_vs_year.loc["Egypt":"India"]
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi")]
temp_by_country_city_vs_year.loc[("Egypt","Cairo"):("India","Delhi"), "2005":"2010" ]

#Calculating on a pivot table

mean_temp_by_year = temp_by_country_city_vs_year.mean()
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = "columns")
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])