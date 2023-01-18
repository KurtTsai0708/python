#Make a PMF

pmf_year = Pmf(gss["year"], normalize=False)
print(pmf_year)

#Plot a PMF
age = gss['age']
pmf_age = Pmf(age)
pmf_age.bar()

plt.xlabel('Age')
plt.ylabel('PMF')
plt.show()