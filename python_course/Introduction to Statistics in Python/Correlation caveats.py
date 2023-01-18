#What can't correlation measure?

sns.scatterplot(x="gdp_per_cap",y="life_exp",data=world_happiness)
plt.show()

cor = world_happiness["gdp_per_cap"].corr(world_happiness["life_exp"])
print(cor)

#Transforming variables

sns.scatterplot(x="gdp_per_cap",y="happiness_score",data=world_happiness)
plt.show()

cor = world_happiness["gdp_per_cap"].corr(world_happiness["happiness_score"])
print(cor)

#

world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)

#Does sugar improve happiness?

sns.scatterplot(x="grams_sugar_per_day", y="happiness_score",data=world_happiness)
plt.show()

cor = world_happiness["grams_sugar_per_day"].corr(world_happiness["happiness_score"])
print(cor)