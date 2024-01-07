from sqlalchemy import create_engine # MODULE INI BERFUNGSI UNTUK MEMORY SQL 
import pandas as pd
import os

os.system("clear")


"""
CARA MEMBACA DATA PADA SUMBER DATA EXCEL, HTML, DAN SQL DENGAN LIBRARY PANDAS
"""


# IMPOR MENGGUNAKAN FUNGSI ATAU METHOD .read_

# 1. IMPOR DATA DENGAN FORRMAT CSV 
data = pd.read_csv('kapal_titanic.csv')
print(data)

# IMPOR 5 DATA TERATAS MENGGUNAKAN FUNGSI ATAU METHOD .head()
limaDataTeratas = data.head()
print(limaDataTeratas)

# IMPOR 5 DATA TERAKHIR MENGGUNAKAN FUNGSI ATAU METHOD .tail()
limaDataTerakhir = data.tail()
print(limaDataTerakhir)

# 2. IMPOR DATA DENGAN FORMAT HTML
dataHtml = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(dataHtml[0]) # MEMBACA INDEX KE - 0 PADA DATA DISAMPIPNG KARENA FUNGSI PADA PANDAS MENG IMPOR DALAM BETUK LIST DAN AGAR SUPAYA RAPI 


# EKSPOR DATA KEDALAM EKSTENSI FORMAT FILE YANG BERBEDA DENGAN MENGGUNAKAN FUNGSI ATAU METHOD .to

# 1. EKSPOR KEDALAM FORMAT CSV :
data.to_csv('DataCsv.csv', index=False) # index = false, BERFUNGSI AGAR FORMAT INDEXING TIDAK MENJADI BARIS
data1 = pd.read_csv('DataCsv.csv')
print(data1)

# 2. EKSPOR KEDALAM FORMAT EXCEL :
data.to_excel('DataExcel.xlsx', index=False, sheet_name='Sheet_1') # SHEET NAME BERFUNGSI UNTUK MEMBERI NAMA PADA KETERANGAN SHEET 
data2 = pd.read_excel('DataExcel.xlsx')
print(data2)

# 3. EKSPOR KEDALAM FORMAT SQL ATAU UNTUK DATABSE 
mesin = create_engine('sqlite:///:memory:')
data.to_sql('DataSql', con=mesin)
data3 = pd.read_sql('DataSql', con=mesin)
print(data3)


