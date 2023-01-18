#Distribution of income

income = gss['realinc']
log_income = np.log10(income)

mean = log_income.mean()
std = log_income.std()
print(mean, std)

from scipy.stats import norm
dist = norm(mean,std)

#Comparing CDFs

xs = np.linspace(2, 5.5)
ys = dist.cdf(xs)

plt.clf()
plt.plot(xs, ys, color='gray')

Cdf(log_income).plot()

plt.xlabel('log10 of realinc')
plt.ylabel('CDF')
plt.show()

#Comparing PDFs

xs = np.linspace(2, 5.5)
ys = dist.pdf(xs)

plt.clf()
plt.plot(xs, ys, color='gray')

sns.kdeplot(log_income)

plt.xlabel('log10 of realinc')
plt.ylabel('PDF')
plt.show()