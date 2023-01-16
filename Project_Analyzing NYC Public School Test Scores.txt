import pandas as pd

schools = pd.read_csv("schools.csv")

## Which schools produce the highest math scores?

best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending=False)

## Who are the top 10 schools based on average results across reading, math, and writing?

schools["average_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
TOP_10_schools = schools.sort_values("average_SAT", ascending=False)[["school_name","average_SAT"]].head(10)

## Which NYC borough has the largest standard deviation for SAT results?

boroughs = schools.groupby("borough")["average_SAT"].agg(["count","mean","std"]).round(0).sort_values("mean",ascending=False)
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

## Completing the project

schools_analysis = {"best_math_schools": best_math_schools,
                    "top_10_schools": TOP_10_schools,
                    "largest_SAT_std_dev": largest_std_dev }

print(schools_analysis)
