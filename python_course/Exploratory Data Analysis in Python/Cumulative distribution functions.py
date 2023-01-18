#Make a CDF

age = gss['age']
cdf_age = Cdf(age)
print(cdf_age(30))

#Compute IQR

percentile_75th = cdf_income.inverse(0.75)
percentile_25th = cdf_income.inverse(0.25)

iqr = percentile_75th - percentile_25th 
print(iqr)

#Plot a CDF

income = gss["realinc"]
cdf_income = Cdf(income)
cdf_income.plot()

plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.show()