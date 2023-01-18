#Population & sampling distribution means

mean_of_means_5 = np.mean(sampling_distribution_5)
mean_of_means_50 = np.mean(sampling_distribution_50)
mean_of_means_500 = np.mean(sampling_distribution_500)

print(mean_of_means_5)
print(mean_of_means_50)
print(mean_of_means_500)

#Population & sampling distribution variation

sd_of_means_5 = np.std(sampling_distribution_5,ddof=1)
sd_of_means_50 = np.std(sampling_distribution_50,ddof=1)
sd_of_means_500 = np.std(sampling_distribution_500,ddof=1)

print(sd_of_means_5)
print(sd_of_means_50)
print(sd_of_means_500)