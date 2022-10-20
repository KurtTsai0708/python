#Concatenation basics

tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join='inner',
                               sort=True)
print(tracks_from_albums)


#Concatenating with keys

inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=["7Jul","8Aug","9Sep"])
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({"total":"mean"})

avg_inv_by_month.plot(kind = "bar")
plt.show()


#Using the append method

metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort=False)
tracks_invoices = metallica_tracks.merge(invoice_items,on="tid")
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({"quantity":"sum"})

print(tracks_sold.sort_values(["quantity"],ascending=False))


#Concatenate and merge to find common songs

classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)
classic_pop = classic_18_19.merge(pop_18_19, on='tid')
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

print(popular_classic)