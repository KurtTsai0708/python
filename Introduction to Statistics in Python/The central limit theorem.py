#The CLT in action

amir_deals["num_users"].hist()
plt.show()

np.random.seed(104)

samp_20 = amir_deals['num_users'].sample(20, replace=True)
np.mean(samp_20)
sample_means = []

for i in range(100):
     samp_20 = amir_deals['num_users'].sample(20, replace=True)
     samp_20_mean = np.mean(samp_20)
     sample_means.append(samp_20_mean)

sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
plt.show()


#The mean of means

np.random.seed(321)
sample_means = []

for i in range(30):
     cur_sample = all_deals["num_users"].sample(20,replace=True)
     cur_mean = np.mean(cur_sample)
     sample_means.append(cur_mean)

print(np.mean(sample_means))
print(np.mean(amir_deals["num_users"]))

  


