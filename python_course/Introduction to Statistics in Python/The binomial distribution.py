#Simulating sales deals

from scipy.stats import binom

np.random.seed(10)

deals = binom.rvs(3,0.3,size=52)
print(np.mean(deals))

#Calculating binomial probabilities

prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)
print(prob_less_than_or_equal_1)

prob_greater_than_1 = 1 - binom.cdf(1,3,0.3)
print(prob_greater_than_1)

#How many sales will be won?

won_30pct = 3 * 0.3
print(won_30pct)

won_25pct = 3 * 0.25
print(won_25pct)

won_35pct = 3 * 0.35
print(won_35pct)