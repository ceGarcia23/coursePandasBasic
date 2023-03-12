#Create a DataFrame from tow Series:
import pandas as pd

data  = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

DataFrame = pd.DataFrame(data)

print(DataFrame)
