import pandas as pd
# data = {
#     "Name": ["A", "B", "C", "D"],
#     "Marks": [90, 75, 88, 60]
# }

# df = pd.DataFrame(data)
# print(df.head(2))

# print(df[df["Marks"] > 80])

# df["Passed"] = df["Marks"] > 70
# print(df)

import pandas as pd

# data = {
#     "Name": ["A","B","C","D","E"],
#     "Marks": [90,75,88,60,95],
#     "City": ["Mumbai","Delhi","Mumbai","Delhi","Mumbai"]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.groupby("City")["Marks"].agg(["mean", "max", "min", "count"]))
# print(df.groupby("City")["Marks"].mean().reset_index())

# df1 = pd.DataFrame({
#     "ID": [1,2],
#     "Name": ["A","B"]
# })

# df2 = pd.DataFrame({
#     "ID": [1,2],
#     "Marks": [90,80]
# })

# merged_df = pd.merge(df1, df2, on="ID")
# print(merged_df)
# merged_df = merged_df.drop_duplicates()
# print(merged_df)

data = {
    "Name": ["A","B","C","D","E"],
    "Marks": [90,75,88,60,95],
    "City": ["Mumbai","Delhi","Mumbai","Delhi","Mumbai"]
}
df=pd.DataFrame(data)
print(df)
pivot_table=df.pivot_table(values="Marks",index="City",aggfunc="mean")
print(pivot_table)
print(df.groupby("City")["Marks"].max())
print(df.sort_values("Marks",ascending=False).head(1))