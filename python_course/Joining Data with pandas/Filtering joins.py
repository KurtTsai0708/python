#Performing an anti join

empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']
print(employees[employees['srid'].isin(srid_list)])


#Performing a semi join
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':"count"})
print(cnt_by_gid.merge(genres, on="gid"))
