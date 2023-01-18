#Clean a variable 

nsfg['nbrnaliv'].replace([8],np.nan , inplace=True)
print(nsfg['nbrnaliv'].value_counts())

#Compute a variable

agecon = nsfg["agecon"] / 100
agepreg = nsfg["agepreg"] / 100

preg_length = agepreg - agecon

print(preg_length.describe())