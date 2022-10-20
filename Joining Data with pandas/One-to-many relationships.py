#One-to-many merge

licenses_owners = licenses.merge(biz_owners, on="account")
counted_df = licenses_owners.groupby("title").agg({'account':'count'})
sorted_df = counted_df.sort_values(by="account", ascending = False)
print(sorted_df.head())