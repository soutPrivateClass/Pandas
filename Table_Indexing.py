import pandas as pd
import os

os.system("clear")

data = pd.read_csv('kapal_titanic.csv')
print(data)

# SLICING PADA KOLOM AGE MENJADI DATA SERIES (SATU DATA)
dataAge = data['age']
print(dataAge)

# ATAU MENGGUNAKAN DOT NOTATION, EX :
dataSurvived = data.survived
print(dataSurvived)

# SLICING PADA KOLOM AGE DAN DECK MENJADI DATA FRAME (LEBIH DARI 2 DATA)
duaData = data[['age','deck']]
print(duaData)

# SLICING .iloc MENENTUKAN BARIS & KOLOM DENGAN RENTANG TERTENTU
barisPertama = data.iloc[0]
print(barisPertama)

kolomPertama = data.iloc[:,0]
print(kolomPertama)

barisKolom = data.iloc[4:11] # DARI BARIS KE-4 SAMPAI BARIS KE-10
print(barisKolom)

# SLICING .iloc MENENTUKAN BARIS & KOLOM DENGAN SPESIFIK
baris = data.iloc[[1,20,89]] # MENAMPILKAN DATA PADA INDEX 1,20,89
print(baris)

barisDanKolom = data.iloc[[1,20,89],[0,1,2]]
print(barisDanKolom)


# .loc UNTUK MENENTUKAN DATA TANPA NOMOR INDEX / MENGGUNAKAN KOLOM SEBAGAI INDEXING
dataBaru = pd.read_csv('kapal_titanic.csv', index_col= 'sex')
print(dataBaru)

indexMale = dataBaru.loc['male','age'] # READ DATA MALE SEBAGAI KOLOM INDXING DAN KOLOM age, MENJADI DATA SERIES
print(indexMale)

indexMaleFemale = dataBaru.loc[['male','female'],['age', 'survived']] # READ DATA male & female SEBAGAI KOLOM INDXING DAN KOLOM age & survived, MENJADI DATA FRAME
print(indexMaleFemale)