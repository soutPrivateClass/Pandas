import pandas as pd
import os

os.system('clear')


data = pd.read_csv('kapal_titanic.csv')

# CARA MANUAL READ ATAU MEMBACA DATA SECARA KESELURUHAN 
pd.options.display.max_rows = 891
pd.options.display.min_rows = 891
print(data)

# FUGSI .info DIBAWAH INI UNTUK MENGETAHUI SUMMARY ATAU RINGKASAN GENERAL DATA
infoGeneral = data.info()
print(infoGeneral)

# FUGSI .describe DIBAWAH INI UNTUK MENGETAHUI SUMMARY ATAU RINGKASAN MATEMATIS DATA
infoMatematis = data.describe()
print(infoMatematis)


# FUGSI .describe DIBAWAH INI UNTUK MENGETAHUI SUMMARY ATAU RINGKASAN NON NUMERIK DATA
infoNonNumerik = data.describe(include='O')
print(infoNonNumerik)