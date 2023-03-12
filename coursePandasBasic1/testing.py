import pandas
import pandas as pd

mydataset = {
    'cars': ["bmw", "Volvi", "Ford"],
    'Passings': [3,7,2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
