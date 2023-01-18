#Modeling time between leads

from scipy.stats import expon as ex

print(ex.cdf(1, scale=2.5))
print(1 - expon.cdf(4, scale=2.5))
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))