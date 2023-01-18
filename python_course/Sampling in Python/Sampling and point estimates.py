#Simple sampling with pandas

spotify_sample = spotify_population.sample(n=1000)
print(spotify_sample)

mean_dur_pop = spotify_population["duration_minutes"].mean()
mean_dur_samp = spotify_sample["duration_minutes"].mean()

print(mean_dur_pop)
print(mean_dur_samp)

#Simple sampling and calculating with NumPy

loudness_pop = spotify_population['loudness']
loudness_samp = loudness_pop.sample(n=100)

mean_loudness_pop = np.mean(loudness_pop)
mean_loudness_samp = np.mean(loudness_samp)

print(mean_loudness_pop)
print(mean_loudness_samp)