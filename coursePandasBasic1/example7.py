# Create a simple Pandas a DataFrame
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df)
print(df.loc[0])

# use a list of indexes:
print(df.loc[[0, 1]])


