#Tracking lead responses

from scipy.stats import poisson
prob_5 = poisson.pmf(5, 4)
print(prob_5)

prob_coworker = poisson.pmf(5, 5.5)
print(prob_coworker)

prob_2_or_less = poisson.cdf(2, 4)
print(prob_2_or_less)

prob_over_10 = 1-poisson.cdf(10,4)
print(prob_over_10)