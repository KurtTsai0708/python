#Extract education levels

educ = gss['educ']

bach = (educ >= 16)
assc = (educ >= 14) & (educ < 16)
high = (educ <= 12)
print(high.mean())

#Plot income CDFs

income = gss['realinc']

Cdf(income[high]).plot(label='High school')
Cdf(income[assc]).plot(label='Associate')
Cdf(income[bach]).plot(label='Bachelor')

plt.xlabel('Income (1986 USD)')
plt.ylabel('CDF')
plt.legend()
plt.show()