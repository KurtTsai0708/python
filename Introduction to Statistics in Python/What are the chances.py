#Calculating probabilities

counts = amir_deals["product"].value_counts()
probs = counts / amir_deals.shape[0]

print(probs)


#Sampling deals

np.random.seed(24)

sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)