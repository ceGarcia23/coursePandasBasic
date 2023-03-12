#Crate your own labels
import pandas as pd

a = [1, 7, 2]

Series = pd.Series(a, index=["x", "y", "z"])

print(Series)
print(Series["y"])


