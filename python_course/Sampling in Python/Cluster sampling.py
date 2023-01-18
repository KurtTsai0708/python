#Cluster sampling

job_roles_pop = list(attrition_pop['JobRole'].unique())

job_roles_samp = random.sample(job_roles_pop, k=4)

jobrole_condition = attrition_pop['JobRole'].isin(job_roles_samp)
attrition_filtered = attrition_pop[jobrole_condition]

attrition_filtered['JobRole'] = attrition_filtered['JobRole'].cat.remove_unused_categories()

attrition_clust = attrition_filtered.groupby("JobRole")\
    .sample(n=10, random_state=2022)
print(attrition_clust)    