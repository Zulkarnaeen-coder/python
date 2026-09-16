import pandas as pd

score = [9807050,7501230,5240580,4251305,4253651]
players = pd.Series(score,index=["Ironhammer","Darksoul","Mamunyt","(/{CM_GHOST/})","Robs Play"])

print(players)
print("\n" * 2)

data ={
    "Player":["Ironhammer","Darksoul","Mamunyt","(/{CM_GHOST/})","Robs Play"],
    "Scores":[9807050,7501230,5240580,4251305,4253651],
    "Match Wins":[215,192,173,153,130],
    "Level":[312,253,186,122,98]
}

df = pd.DataFrame(data)
print(df)

print("\n" * 2)

print(f"Row 0: {df.loc[0]}")
print(f"Row 2 and 3: {df.loc[[2,3]]}")