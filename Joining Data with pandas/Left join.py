#Counting missing rows with left join

number_of_missing_fin = movies_financials['budget'].isnull().sum()
print(number_of_missing_fin)


#Enriching a dataset

toystory_tag = toy_story.merge(taglines, on="id", how="left")
print(toystory_tag)
print(toystory_tag.shape)