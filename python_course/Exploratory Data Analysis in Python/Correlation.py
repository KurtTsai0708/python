#Computing correlations

columns = ["AGE","INCOME2","_VEGESU1"]
subset = brfss[columns]

print(subset.corr())