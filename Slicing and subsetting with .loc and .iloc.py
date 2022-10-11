#Slicing index values

temperatures_srt = temperatures_ind.sort_index()
print(temperatures_srt.loc["Pakistan":"Russia"])
print(temperatures_srt.loc["Lahore":"Moscow"])
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])

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