#Relationships between variables

sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
plt.show()

#

sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)
plt.show()

cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
print(cor)