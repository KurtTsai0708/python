#Using StatsModels

from scipy.stats import linregress
import statsmodels.formula.api as smf

subset = brfss.dropna(subset=['INCOME2', '_VEGESU1'])
xs = subset['INCOME2']
ys = subset['_VEGESU1']
res = linregress(xs, ys)
print(res)

results = smf.ols('_VEGESU1 ~ INCOME2', data=brfss).fit()
print(results.params)