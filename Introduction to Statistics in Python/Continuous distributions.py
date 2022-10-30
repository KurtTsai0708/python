#Data back-ups

min_time = 0
max_time = 30

from scipy.stats import uniform

prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)

prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)

prob_between_10_and_20 = uniform.cdf(20, min_time, max_time) - uniform.cdf(10, min_time, max_time)
print(prob_between_10_and_20)

#Simulating wait times

np.random.seed(334)

from scipy.stats import uniform

wait_times = uniform.rvs(0, 30, size=1000)
plt.hist(wait_times)
plt.show()