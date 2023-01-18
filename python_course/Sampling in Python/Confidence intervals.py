#Calculating confidence intervals

point_estimate = np.mean(bootstrap_distribution)
standard_error = np.std(bootstrap_distribution, ddof=1)

lower_se = norm.ppf(0.025, loc=point_estimate, scale=standard_error)
upper_se = norm.ppf(0.975, loc=point_estimate, scale=standard_error)

print((lower_se, upper_se))