import pandas as pd

df = pd.read("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

del df["brown_dwarf"]
del df["constellation"]
del df["right_ascension"]
del df["declination"]
del df["app_mag"]
del df["distance"]
del df["spectral_type"]
del df["mass"]
del df["radius"]
del df["discovery_year"]

df = df.rename({
                'app_mag': "apparent_magnitude", 
            }, axis='columns')

df.to_csv('main.csv') 