#Right join to find unique movies

action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
movies_and_scifi_only = movies.merge(scifi_only, left_on = "id",right_on = "movie_id")

print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)


#Popular genres with right join

genres_movies = movie_to_genres.merge(pop_movies, how='right', 
                                      left_on ="movie_id", 
                                      right_on="id")
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

genre_count.plot(kind='bar')
plt.show()

#Using outer join to select actors
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how="outer",
                                     on= "id",
                                     suffixes=["_1","_2"])
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

print(iron_1_and_2[m].head())