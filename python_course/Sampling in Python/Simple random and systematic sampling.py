#Simple random sampling

attrition_samp = attrition_pop.sample(n=70,random_state=18900217)
print(attrition_samp)

#Systematic sampling

pop_size = len(attrition_pop)
interval = pop_size // sample_size

attrition_sys_samp = attrition_pop.iloc[::interval]
print(attrition_sys_samp)

#Is systematic sampling OK?

attrition_shuffled = attrition_pop.sample(frac=1)
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()
attrition_shuffled.plot(x="index", y="YearsAtCompany", kind="scatter")
plt.show()