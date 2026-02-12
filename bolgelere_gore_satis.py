import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

 # Veritabanına bağlan
conn = sqlite3.connect('eticaret.db')

 #SQL'den bölgelere göre satış verisini çek
sorgu = "SELECT Region, SUM(Sales) as Toplam_Satis FROM satislar GROUP BY Region"
grafik_df = pd.read_sql(sorgu, conn)

 # GÖRSELLEŞTİRME (SÜTUN GRAFİĞİ)
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='ToplamSatis', data=grafik_df, palette='viridis')
plt.title('Bolgelere Gore Toplam Satis Grafiği')
    
plt.savefig('Bolgelere_gore_satis_grafigi.png') 
plt.show()

conn.close()
