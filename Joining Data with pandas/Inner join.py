#Your first inner join

taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))
print(taxi_own_veh['fuel_type'].value_counts())

#Inner joins and number of rows returned

wards_census = wards.merge(census,on="ward")
print('wards_census table shape:', wards_census.shape)