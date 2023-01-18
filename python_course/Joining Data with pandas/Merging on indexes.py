#Index merge for movie ratings

movies_ratings = movies.merge(ratings, on = "id", how="left")
print(movies_ratings.head())


#Do sequels earn more?

sequels_fin = sequels.merge(financials, on='id', how='left')
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']
titles_diff = orig_seq[['title_org','title_seq','diff']]

print(titles_diff.sort_values("diff", ascending = False).head())