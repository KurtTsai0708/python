#Calculating relative errors

attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)
mean_attrition_srs50 = attrition_srs50['Attrition'].mean()
rel_error_pct50 = 100 * abs(mean_attrition_pop - mean_attrition_srs50) / mean_attrition_pop
print(rel_error_pct50)

