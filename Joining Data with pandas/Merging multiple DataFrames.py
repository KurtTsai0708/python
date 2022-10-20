#Total riders in a month

ridership_cal = ridership.merge(cal, on=['year','month','day'])


#Three table merge

licenses_zip_ward = licenses.merge(zip_demo, on = "zip") \
						.merge(wards, on = "ward")
print(licenses_zip_ward.groupby("alderman").agg({"income":"median"}))


#One-to-many merge with multiple tables

land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))
pop_vac_lic = land_cen_lic.groupby(["ward","pop_2010","vacant"], 
                                   as_index=False).agg({'account':'count'})
sorted_pop_vac_lic = pop_vac_lic.sort_values(["vacant","account","pop_2010"], 
                                             ascending=[False, True, False])

print(sorted_pop_vac_lic.head())