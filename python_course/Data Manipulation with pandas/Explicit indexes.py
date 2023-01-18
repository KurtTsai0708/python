#Setting and removing indexes

print(temperatures)

temperatures_ind = temperatures.set_index("city")
print(temperatures_ind)
print(temperatures_ind.reset_index())
print(temperatures_ind.reset_index(drop=True))

#Subsetting with .loc[]

cities = ["Moscow", "Saint Petersburg"]

print(temperatures[temperatures["city"].isin(cities)])
print(temperatures_ind.loc[cities])

#Setting multi-level indexes

temperatures_ind = temperatures.set_index(["country","city"])
rows_to_keep = [("Brazil","Rio De Janeiro"),("Pakistan","Lahore")]
print(temperatures_ind.loc[rows_to_keep])

#Sorting by index values

print(temperatures_ind.sort_index())
print(temperatures_ind.sort_index(level="city"))
print(temperatures_ind.sort_index(level=["country","city"], ascending=[True,False]))

#Slicing in both directions

print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad")])
print(temperatures_srt.loc[:,"date":"avg_temp_c"])
print(temperatures_srt.loc[("India","Hyderabad"):("Iraq","Baghdad"),"date":"avg_temp_c"])

#Slicing time series

temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & ( temperatures["date"] <= "2011-12-31")]
print(temperatures_bool)

temperatures_ind = temperatures.set_index("date").sort_index()
print(temperatures_ind.loc["2010":"2011"])
print(temperatures_ind.loc["2010-08":"2011-02"])

#Subsetting by row/column number

print(temperatures.iloc[22,1])
print(temperatures.iloc[0:5])
print(temperatures.iloc[:,2:4])
print(temperatures.iloc[0:5,2:4])