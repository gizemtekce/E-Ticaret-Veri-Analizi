import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


# Veritabanına bağlan
conn = sqlite3.connect('eticaret.db')

# SQL'den tarih ve satış verilerini çek
sorgu = "SELECT [Order Date], Sales FROM satislar"
df_trend = pd.read_sql(sorgu, conn)


# Tarih sütununu metinden  tarih'e çevir
df_trend['Order Date'] = pd.to_datetime(df_trend['Order Date'])

# Verileri aylara göre grupla
df_trend.set_index('Order Date', inplace=True)
aylik_satis = df_trend.resample('M').sum() # 'M' harfi aylık demektir.

# 3. GÖRSELLEŞTİRME (Çizgi Grafiği)
plt.figure(figsize=(12, 6))
sns.lineplot(x=aylik_satis.index, y='Sales', data=aylik_satis, marker='o', color='b', linewidth=2.5)


plt.title('Aylık Satış Çizgi Grafiği (2022-2025) ', fontsize=16, fontweight='bold')
plt.xlabel('Zaman (Aylar)', fontsize=12)
plt.ylabel('Toplam Satış Tutarı ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)


plt.savefig('Aylık_Satis_Grafigi.png')
plt.show()

conn.close()