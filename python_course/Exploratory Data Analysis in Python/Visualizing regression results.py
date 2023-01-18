#Making predictions

results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

df = pd.DataFrame()
df['educ'] = np.linspace(0,20)
df['age'] = 30
df['educ2'] = df['educ']**2
df['age2'] = df['age']**2

pred = results.predict(df)
print(pred.head())

#Visualizing predictions

plt.clf()
grouped = gss.groupby('educ')
mean_income_by_educ = grouped['realinc'].mean()
plt.plot(mean_income_by_educ,"o",alpha=0.5)

pred = results.predict(df)
plt.plot(df["educ"], pred, label='Age 30')

plt.xlabel('Education (years)')
plt.ylabel('Income (1986 $)')
plt.legend()
plt.show()