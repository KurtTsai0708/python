#Creating a probability distribution

restaurant_groups["group_size"].hist(bins=[2,3,4,5,6])
plt.show()

size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
size_dist = size_dist.reset_index()
size_dist.columns = ["size_dist","prob"]

expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])

groups_4_or_more = size_dist[size_dist['group_size'] >= 4]
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)

