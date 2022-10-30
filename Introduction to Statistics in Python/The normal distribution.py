#Distribution of Amir's sales

amir_deals['amount'].hist(bins=10)
plt.show()

#Probabilities from the normal distribution

prob_less_7500 = norm.cdf(7500, 5000, 2000)
print(prob_less_7500)

prob_over_1000 = 1 - norm.cdf(1000,5000,2000)
print(prob_over_1000)

prob_3000_to_7000 = norm.cdf(7000,5000,2000) - norm.cdf(3000,5000,2000)
print(prob_3000_to_7000)

pct_25 = norm.ppf(0.25,5000,2000)
print(pct_25)

#Simulating sales under new market conditions

new_mean = 5000*1.2
new_sd = 2000*1.
new_sales = norm.rvs(new_mean,new_sd,size=36)

plt.hist(new_sales)
plt.show()