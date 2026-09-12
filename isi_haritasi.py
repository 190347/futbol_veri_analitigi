import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from mplsoccer import Pitch
import seaborn as sns

# 1. PostgreSQL Veri Tabanına Bağlan
engine = create_engine('postgresql://ferhatbilge:3091@localhost:5432/db_duran_top')

# 2. SQL Sorgusu (Daha fazla veri çekmek için tüm takımların kornerlerini alıyoruz)
query = """
SELECT end_x, end_y 
FROM set_pieces 
WHERE vurus_tipi = 'Corner'
"""
df = pd.read_sql(query, engine)

# 3. Futbol Sahasını Çiz
# Isı haritasının parlaması için koyu temayı koruyoruz
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(12, 8))
fig.set_facecolor('#22312b')

# 4. Barcelona verileri kaldırıldı

# 5. Isı Haritasını (KDE Plot) Oluştur
# kdeplot ile yoğunluk hesaplanır. 'cmap' ile renk paleti (örn: magma, inferno, Reds) belirlenir.
sns.kdeplot(
    x=df.end_x, 
    y=df.end_y, 
    fill=True, 
    cmap='magma', 
    alpha=0.7, 
    levels=15, 
    ax=ax,
    thresh=0.01
)

# 6. Başlık Ekle
plt.title("Genel Korner Isı Haritası (Tüm Takımlar)", color='white', fontsize=18, pad=20)

# 7. Grafiği Göster
plt.show()
