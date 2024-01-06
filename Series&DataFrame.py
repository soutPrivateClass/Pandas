import numpy as np
import pandas as pd
import os 

os.system('clear')

"""
SUMBER DATA SERIES DAPAT DARI BEBERAPA SUMBER YAITU :
1. DATA LIST
2. DICTIONARY
"""

# 1. DATA LIST :
dataKolom = [10,20,30]
dataIndex = ['a','b','c']

dataSeries = pd.Series(data = dataKolom, index = dataIndex)
print(dataSeries)

# SLICING :
print(dataSeries['b'])

# CONVERT KEDALAM BENTUK DATA FRAME (JADI LEBIH TERATUR) :
dataBaru = dataSeries.to_frame()
print(dataBaru)

# 2. DATA DICTIONARY :
dataDictionary1 = {
    'Angka 1' : 100,
    'Angka 2' : 200,
    'Angka 3' : 300
}

dataDictionary2 = {
    'Angka 1' : 100,
    'Angka 2' : 200,
    'Angka 3' : 300,
    'Angka 4' : 400,
    'Angka 5' : 500
}

dataDict_1 = pd.Series(dataDictionary1)
dataDict_2 = pd.Series(dataDictionary2)

# JUMLAH 2 DATA SERIES : 
jumlah = dataDict_1 + dataDict_2
print(jumlah)

"""
DATA FRAME :
"""

# BILANGAN RANDOM UNTUK MEMBENNTUK SEBUAH DATA FRAME : 
dataFrame = pd.DataFrame(np.random.randn(3,3),['A','B','C'], ['One','Two','Three'])
print(dataFrame)

# SLICING :
print(dataFrame['One'])

# ADDING KOLOM :
dataFrame['Total'] = dataFrame['One'] + dataFrame['Two'] + dataFrame['Three']
print(dataFrame)

# DELETE KOLOM :
dataFrame.drop('Three', axis='columns', inplace=True) # PARAMETER AXIS BERISI 0 DAN 1, 0 UNTUK INDEX / BARIS 1 UNTUK KOLOM, BISA JUGA DIISIKAN INDEX ATAU COLUMNS, inplace = True UNTUK AGAR SUPAYA TANPA MELAKUKAN RE ASSIGNMENT
print(dataFrame)

# DELETE INDEX / BARIS :
dataFrame.drop('C', axis='index', inplace=True)
print(dataFrame)

# CEK DIMENSI DATA :
shapeData = dataFrame.shape
print(shapeData)

"""
METHOD - METHOD UNTUK MEMAHAMI DATA SERIES DAN DATA FRAME
"""

dataFrame = pd.DataFrame(np.random.randn(3,3),['A','B','C'], ['Angka1','Angka2','Angka3'])
print(dataFrame)

dataSeries = dataFrame['Angka1']


# .descibe() UNTUK MENGHASILKAN STATISTIK DESKRIPTIF SEBUAH DATA
statistik = dataSeries.describe()
print(statistik)

# .count() UNUTK MENJUMLAH BERAPA BANYAK DATA YANG TERTAMPUNG DALAM DATA (TIDAK TERMASUK DATA KOSONG)
jumlahData = dataSeries.count()
print(jumlahData)

# .mean() = RATA - RATA
mean = dataSeries.mean()
print(mean)

# .median() = NILAI TENGAH
median = dataSeries.median()
print(median)

# .sum()
sum = dataSeries.sum()
print(sum)

# .std (STANDART DEVIASI)
std = dataSeries.std()
print(std) 

# .dropna() DIGUNAKAN UNTUK MENAMPILKAN DATA MISSING VALUE ATAU TANPA DATA KOSONG PADA DATA SERIES
# DATA PADA BARIS / INDEX AKAN HILANG JIKA BERNILAI NAN ATAU KOSONG
dropSeries = dataSeries.dropna()
print(dropSeries)

# .dropna() DIGUNAKAN UNTUK MENAMPILKAN DATA MISSING VALUE ATAU TANPA DATA KOSONG PADA DATA FRAME
# DATA PADA BARIS / INDEX AKAN HILANG JIKA BERNILAI NAN ATAU KOSONG
dropFrame = dataFrame.dropna()
print(dropFrame)

# .dropna(axis=1) DIGUNAKAN UNTUK MENAMPILKAN DATA MISSING VALUE ATAU TANPA DATA KOSONG PADA DATA FRAME
# DATA PADA KOLOM AKAN HILANG JIKA BERNILAI NAN ATAU KOSONG
dropFrame = dataFrame.dropna(axis='columns') # BISA MENGGUNAKAN axis = 1 atau axis = 'columns'
print(dropFrame)

# thresh = 3 DIGUNAKAN UNTUK APABILA ADA MINIMAL 3 DATA TERISI DALAM SATAU INDEX ATAU BARIS, MAKA AKAN DIPERTAHANKAN
# UNTUK NILAI PADA thresh BERSIFAT OPTIONAL (DAPAT DIISI BERAPAPUN SESUAI DENGAN KETENTUAN)
dropFrame = dataFrame.dropna(axis='index', thresh = 3)
print(dropFrame)

# .fillna UNUTK MNGISI NILAI KOSONG PADA SEBUAH DATA (HANYA BERLAKU UNTUK DATA NUMERIK)
dataKapal = pd.read_csv('kapal_titanic.csv')

kolomAge = dataKapal.age
dataAge = kolomAge.fillna(mean)
print(dataAge)

print(dataAge.values)
