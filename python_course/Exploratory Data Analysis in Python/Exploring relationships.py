#PMF of age

age = brfss["AGE"]

pmf_age = Pmf(age)
pmf_age.bar()

plt.xlabel('Age in years')
plt.ylabel('PMF')
plt.show()

#Scatter plot

brfss = brfss[:1000]

age = brfss['AGE']
weight = brfss['WTKG3']

plt.plot(age,weight,"o",alpha=0.1)

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')

plt.show()

#Jittering

brfss = brfss[:1000]

age = brfss['AGE'] + np.random.normal(0,2.5,size=len(brfss))

weight = brfss['WTKG3']
plt.plot(age,weight,"o",markersize=5,alpha=0.2 )

plt.xlabel('Age in years')
plt.ylabel('Weight in kg')
plt.show()