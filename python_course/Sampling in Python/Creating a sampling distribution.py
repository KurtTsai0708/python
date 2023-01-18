#Replicating samples

mean_attritions = []

for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)

plt.hist(mean_attritions, bins=16)
plt.show()