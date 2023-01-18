#Make a histogram

plt.hist(agecon, bins=20, histtype='step')

plt.xlabel('Age at conception')
plt.ylabel('Number of pregnancies')

plt.show()

#Compute birth weight

full_term = nsfg["prglngth"] >= 37
full_term_weight = birth_weight[full_term]
print(full_term_weight.mean())

#Filter

full_term = nsfg['prglngth'] >= 37
single = nsfg["nbrnaliv"] == 1

single_full_term_weight = birth_weight[single & full_term]
print('Single full-term mean:', single_full_term_weight.mean())

mult_full_term_weight = birth_weight[~single & full_term]
print('Multiple full-term mean:', mult_full_term_weight.mean())