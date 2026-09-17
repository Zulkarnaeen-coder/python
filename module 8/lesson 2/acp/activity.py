import pandas as pd

Marks = [85,78,82.5,90.5,72.2]
Students = pd.Series(Marks,index=["Robiul","Mamun","Salam","Molla","Mamuni"])

print(Students)
print("\n" * 2)

data ={
    "Students":["Robiul","Mamun","Salam","Molla","Mamuni"],
    "Scores":[85,78,82.5,90.5,72.2],
    "    Favourite Subject":["Math","B.G.S","English","Bangla","Religion"],
}

df = pd.DataFrame(data)
print(df)

print("\n" * 2)

print(f"Row 0: {df.loc[0]}")
print(f"Row 2 and 3: {df.loc[[2,3]]}")