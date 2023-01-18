#Generating random numbers

normals = np.random.normal(loc=5, scale=2, size=5000)

plt.hist(normals,bins=np.arange(-2,13.5,0.5))
plt.show()