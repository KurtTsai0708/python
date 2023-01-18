#Height and weight

data = brfss.dropna(subset=['_HTMG10', 'WTKG3'])

sns.boxplot(x="_HTMG10",y="WTKG3",data=data,whis=10)

plt.yscale("log")

sns.despine(left=True, bottom=True)
plt.xlabel('Height in cm')
plt.ylabel('Weight in kg')
plt.show()

#Distribution of income

income = brfss["INCOME2"]
Pmf(income).bar()

plt.xlabel('Income level')
plt.ylabel('PMF')
plt.show()

#Income and height

data = brfss.dropna(subset=['INCOME2', 'HTM4'])

sns.violinplot(x="INCOME2",y="HTM4",data=data,inner=None)

sns.despine(left=True, bottom=True)
plt.xlabel('Income level')
plt.ylabel('Height in cm')
plt.show()
