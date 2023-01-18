#Plot income and education

grouped = gss.groupby("educ")
mean_income_by_educ = grouped["realinc"].mean()

plt.clf()
plt.plot(mean_income_by_educ,"o",alpha=0.5)

plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.show()

#Non-linear model of education

import statsmodels.formula.api as smf

gss['educ2'] = gss["educ"]**2
results = smf.ols("realinc~ educ + educ2 + age + age2",data=gss).fit()

print(results.params)