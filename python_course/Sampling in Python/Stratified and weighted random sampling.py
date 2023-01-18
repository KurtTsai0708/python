#Proportional stratified sampling

education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)
print(education_counts_pop)

attrition_strat = attrition_pop.groupby('Education')\
	.sample(frac=0.4, random_state=2022)

education_counts_strat = attrition_strat["Education"].value_counts(normalize=True)
print(education_counts_strat)

#Equal counts stratified sampling

attrition_eq = attrition_pop.groupby('Education')\
	.sample(n=30, random_state=2022)      

education_counts_eq = attrition_eq["Education"].value_counts(normalize=True)

print(education_counts_eq)

#Weighted sampling

attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

attrition_weight["YearsAtCompany"].hist(bins=np.arange(0,41,1))
plt.show()