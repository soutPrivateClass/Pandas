import pandas as pd
import os

os.system('clear')

"""
MENGGABUNGKAN DATA FRAME SATU DENGAN YANG LAIN
"""

data1 = pd.DataFrame(
    {'A':['a0','a1','a2','a3','a4','a5'],
    'B':['b0','b1','b2','b3','b4','b5'],
    'C':['c0','c1','c2','c3','c4','c5'],
    'D':['d0','d1','d2','d3','d4','d5']},
    index = [0,1,2,3,4,5]
)
data2 = pd.DataFrame(
    {'A':['a6','a7','a8','a9','a10','a11'],
    'B':['b6','b7','b8','b9','b10','b11'],
    'C':['c6','c7','c8','c9','c10','c11'],
    'D':['d6','d7','d8','d9','d10','d11']},
    index = [6,7,8,9,10,11]
)
data3 = pd.DataFrame(
    {'A':['a12','a13','a14','a15','a16','a17'],
    'B':['b12','b13','b14','b15','b16','b17'],
    'C':['c12','c13','c14','c15','c16','c17'],
    'D':['d12','d13','d14','d15','d16','d17']},
    index = [12,13,14,15,16,17]
)

# CONCATENATION (PENGGABUNGAN 3 BUAH DATA DICT DIATAS) :

concateData = pd.concat([data1,data2,data3])
print(concateData)


# GROUPING / PENGELOMPOKKAN DATA
data4 = pd.DataFrame(
    {'Company' : ['BRI','BCA','MANDIRI', 'BRI', 'BCA'],
     'Name' : ['Joko', 'Amri', 'Masning', 'Hendra', 'Susilo'],
     'Age' : [22, 22, 23, 25, 23]}
)

print(data4)

# MENAMBAHKAN DATA BERDASARKAN KOLOM COMPANY :
sum = data4.groupby('Company').sum()
print(sum)

# MENJUMLAH BANYAKNYA DATA BERDASARKAN KOLOM COMPANY :
count = data4.groupby('Company').count()
print(count)

# NILAI TERENDAH BERDASARKAN KOLOM COMPANY :
min = data4.groupby('Company').min()
print(min)

# NILAI TERTINGGI BERDASARKAN KOLOM COMPANY :
max = data4.groupby('Company').max()    
print(max)

# NILAI RATA - RATA BERDASARKAN KOLOM COMPANY & AGE SEBAGAI PARAMETER (HANYA BISA UNTUK DATA NUMERIK) :
mean = data4.groupby('Company').Age.mean()    
print(mean)

# DESCRIBE ATAU KESIMPULAN DATA BERDASARKAN KOLOM COMPANY :
describe = data4.groupby('Company').describe().transpose() # transpose() UNTUK MENGUBAH STYLE ATAU GAYA VISUALISASI (TIDAK PAKAI JUGA  GAK MASALAH)
print(describe)

#  MERGE ADALAH SEBUAH FUNGSI UNTUK GROUPING DENGAN KONSEP IRISAN (INNER, OUTER, LEFT, & RIGHT)

# DIBAWAH INI ADALAH CONTOH UNTUK IMPLEMENTTASI INNER :
data5 = pd.DataFrame({
    'Key' : ['K0','K1','K2','K3'],
    'One'  : [1,2,3,4],
    'Two' : [6,7,8,9]
    })

data6 = pd.DataFrame({
    'Key' : ['K0','K1','K2','K3'],
    'Three'  : [1,2,3,4],
    'Four' : [6,7,8,9]
    })


# DIBAWAH INI ADALAH CONTOH UNTUK IMPLEMENTTASI LEFT & RIGHT :
data7 = pd.DataFrame({
    'Key0' : ['K0','K1','K2','K3','K4'],
    'Key1' : ['K0','K2','K3','K4','K6'],
    'Data 1' : ['Imran','Sodiq','Apri','Ika','Masning']
})

data8 = pd.DataFrame({
    'Key0' : ['K0','K1','K2','K3','K4'],
    'Key1' : ['K0','K2','K7','K4','K5'],
    'Data 2' : ['Anjas','Lily','Arman','Herman','Malik']
})

# INNER (IRISAN) MENGGABUNGKAN DUA BUAH DATA BERDASARKAN KEY DAN HANYA MENAMPILKAN DATA YANG MEMILIKI NILAI YANG SAMA
dataInner = pd.merge(data5,data6, how='inner', on='Key')
print(dataInner)

# LEFT MENGGABUNGKAN DUA BUAH DATA BERDASARKAN KEY DAN MENAMPILKAN DATA YANG MEMILIKI NILAI YANG SAMA DITAMBAH DENGAN DATA LEFT (DATA YANG PERTAMA)
dataLeft = pd.merge(data7,data8, how='left', on=['Key0','Key1'])
print(dataLeft)

# RIGHT MENGGABUNGKAN DUA BUAH DATA BERDASARKAN KEY DAN MENAMPILKAN DATA YANG MEMILIKI NILAI YANG SAMA DITAMBAH DENGAN DATA RIGHT (DATA YANG KEDUA)
dataRight = pd.merge(data7,data8, how='right', on=['Key0','Key1'])
print(dataRight)

# OUTER MENGGABUNGKAN DUA BUAH DATA BERDASARKAN KEY DAN MENAMPILKAN DATA YANG MEMILIKI NILAI YANG SAMA DITAMBAH DENGAN SEMUA DATA
dataOuter = pd.merge(data7,data8, how='outer', on=['Key0','Key1'])
print(dataOuter)

# JOIN FUNGSI
dataCompany1 = pd.DataFrame({
    'Company 1': ['BCA','BRI','MANDIRI'],
    'Company 2' : ['Oppo','Samsung','Xiaomi']},
    index = [1,2,3]
)

dataCompany2 = pd.DataFrame({
    'Company 3': ['Cimbniaga','BPD','BNI'],
    'Company 4' : ['Esia','Cross','Titan']},
    index = [1,2,4]
)

dataJoin = dataCompany1.join(dataCompany2, how='left')
print(dataJoin)

