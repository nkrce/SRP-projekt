import pandas as pd

"""
1. Predprocesiranje skupa podataka

"""

# Određivanje putanje do CSV datoteke
CSV_FILE_PATH = "/content/book1000k-1100k.csv"

# Učitavanje CSV datoteke (provjerite svoje delimiter u csv datoteci), ispis broja redaka i stupaca
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')
print("CSV size before: ", df.shape)

df = df.drop(columns=['Language']) # Brisanje nepotrebnog stupaca (stupac ima previse nedostajucih vrijednosti)
df = df.dropna() # Brisanje redaka s nedostajućim vrijednostima
print("CSV size after: ", df.shape) # Ispis broja redaka i stupaca nakon predprocesiranja
print(df.head()) # Ispis prvih redaka dataframe-a

# Random dijeljenje skupa podataka na dva dijela 80:20 (trebati će nam kasnije)
df20 = df.sample(frac=0.2, random_state=1)
df = df.drop(df20.index)
print("CSV size 80: ", df.shape)
print("CSV size 20: ", df20.shape)

# Spremanje predprocesiranog skupa podataka u novu CSV datoteku
df.to_csv("book1000k-1100k_PROCESSED.csv", index=False) # Spremanje predprocesiranog skupa podataka u novu CSV datoteku
df20.to_csv("book1000k-1100k_PROCESSED_20.csv", index=False) # Spremanje 20% skupa podataka u novu CSV datoteku