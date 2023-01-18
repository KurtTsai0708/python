#3 kinds of sampling

#simple sampling

attrition_srs = attrition_pop.sample(frac=0.25,random_state=2022)

#stratified sampling

attrition_strat = attrition_pop.groupby("RelationshipSatisfaction")\
    .sample(frac=0.25,random_state=2022)

#cluster sampling

satisfaction_unique = list(attrition_pop['RelationshipSatisfaction'].unique())
satisfaction_samp = random.sample(satisfaction_unique, k=2)

satis_condition = attrition_pop['RelationshipSatisfaction'].isin(satisfaction_samp)
attrition_clust_prep = attrition_pop[satis_condition]
attrition_clust_prep['RelationshipSatisfaction'] = attrition_clust_prep['RelationshipSatisfaction'].cat.remove_unused_categories()

attrition_clust = attrition_clust_prep.groupby("RelationshipSatisfaction")\
    .sample(n=len(attrition_pop) // 4, random_state=2022)

#Comparing point estimates

mean_attrition_pop = attrition_pop.groupby('RelationshipSatisfaction')['Attrition'].mean()
print(mean_attrition_pop)

mean_attrition_srs = attrition_srs.groupby("RelationshipSatisfaction")["Attrition"].mean()
print(mean_attrition_srs)

mean_attrition_strat = attrition_strat.groupby("RelationshipSatisfaction")['Attrition'].mean()
print(mean_attrition_strat)

mean_attrition_clust = attrition_clust.groupby("RelationshipSatisfaction")['Attrition'].mean()
print(mean_attrition_clust)