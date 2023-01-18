#Sampling distribution vs. bootstrap distribution

mean_popularity_2000_samp = []

for i in range (2000):
    mean_popularity_2000_samp.append(
        np.mean(spotify_population.sample(n=500,replace=False)["popularity"])
    )

print(mean_popularity_2000_samp)   

mean_popularity_2000_boot = []

for i in range (2000):
    mean_popularity_2000_boot.append(
        np.mean(spotify_sample.sample(n=500, replace=True)['popularity'])
    )

print(mean_popularity_2000_boot)

#Compare sampling and bootstrap means

pop_mean = np.mean(spotify_population["popularity"])
samp_mean = np.mean(spotify_sample["popularity"])

samp_distn_mean = np.mean(sampling_distribution)
boot_distn_mean = np.mean(bootstrap_distribution)

print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])

#Compare sampling and bootstrap standard deviations

pop_sd = spotify_population['popularity'].std(ddof=0)
samp_sd = spotify_sample['popularity'].std()
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])