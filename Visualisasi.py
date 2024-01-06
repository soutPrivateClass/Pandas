import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

import os

os.system('clear')

"""
MACAM - MACAM BENTUK TAMPIILAN VISUALISASI DATA MENGGUNAKAN MATPLOTLIB & SEABORN 
"""

data = pd.read_csv('kapal_titanic.csv')
dataAge = data.age
dataAge.head()

# HISTOGRAM :
dataAge.hist()
plt.show()

dataAge.hist(bins= 30) # .hist(bins=30) UNTUK MENGUKUR KETEBALAN PADA BATANG GRAFIK :
plt.show()

# MENGGUNAKAN .plot AGAR TAMPILAN LEBIH BERSIH
dataAge.plot.hist(bins=30)
plt.ylabel('Frequency') # MEMBERIKAN LABEL NAMA 'Frequency' PADA SUMBU Y
plt.show()

sns.set() # TAMPILAN LEBIH PROFESIONAL MENGGUNAKAN LIBRARY SEABORN
dataAge.plot.hist(bins = 30, alpha = 0.4) # alpha UNTUK MENGATUR TINGKAT TRANSPARANSI / KECERAHAN PADA BATANG GRAFIK, RANGE 0-1
plt.ylabel('Frequency')
plt.show()

"""
MEMBUAT DATA FRAME MANUAL UNTUK DIVISUALISASIKAN :
"""

baris = []
for i in range(0,100):
    baris.append(i)
kolom = ['Januari','Februari','Maret','April','Mei']

data2 = pd.DataFrame(np.random.rand(100,5),baris,kolom)

# VISUALISASI PLOT AREA / LUAS PERMUKAAN :
data2.plot.area(alpha=0.4)
plt.show()


data3 = pd.DataFrame(np.random.rand(4,5),[0,1,2,3],['A','B','C','D','E'])

data3.plot.bar(stacked=True) # stacked = True MENJADIKAN GRAFIK BERMODEL STACK
plt.show()

# SCATTER PLOT BERDASARKAN WARNA :
sns.set()
data2.plot.scatter(x='Januari', y='Februari', c='Maret', cmap='ocean') # SUMBU X & Y KOLOM DATA HORIZONTAL DAN VERTIKAL, C = UNTUK DATA TAMBAHAN ATAU MENGGANTI WARNA FORMAT RGB INTEGER, SEDANGKAN cmap UNTUK MENGGANTI WARNA
plt.show()

# SCATTER PLOT BERDASARKAN UKURAN DENGAN PARAMETER  'S' :
sns.set()
data2.plot.scatter(x = 'Januari', y = 'Februari', s = data2.Maret*100) # s = data2.Maret*100 UNTUK MENENTUKAN UKURAN
plt.show()

# BOX PLOT :
sns.set()
data2.plot.box()
plt.show()

# LINE PLOT :
sns.set()
data2.plot.line(y='Januari', lw=0.5, figsize=(5,4)) # SECARA DEFAULT SUMBU X JIKA TIDAK DIISI MAKA, INDEX AKAN MENJADI SUMBU X, lw=0.5 BBERFUNGSI UNTUK MENENTUKAN TIPIS ATAU TEBALNYA GRAFIK, figsize UNTUK MENENTUKAN PANNJANG & LEBAR UKURAN GRAFIK
plt.show()

# HEXBIN PLOT :
sns.set()
data2.plot.hexbin(x='Januari', y='Februari', gridsize=40) # gridsize UNTUK MENENTUKAN UKURAN GRAFIK 
plt.show()