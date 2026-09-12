import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# 1. PostgreSQL Veri Tabanına Bağlan
# Şifreni ve kullanıcı adını önceki betikteki gibi ayarladık
engine = create_engine('postgresql://ferhatbilge:3091@localhost:5432/db_duran_top')

# 2. SQL Sorgusu ile Veriyi Çek
query = """
SELECT takim, end_x, end_y 
FROM set_pieces 
WHERE vurus_tipi = 'Corner' AND sonuc = 'Basarili'
"""
df = pd.read_sql(query, engine)

# 3. Futbol Sahasını Çiz (StatsBomb boyutları: 120x80)
# Koyu yeşil bir çim rengi ve açık gri çizgiler kullanıyoruz
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(10, 7))
fig.set_facecolor('#22312b')

# 4. Verileri Sahaya Nokta Olarak Ekle
# Barcelona'nın kornerlerini kırmızı noktalarla çizelim
barca_df = df[df['takim'] == 'Barcelona']
pitch.scatter(barca_df.end_x, barca_df.end_y, ax=ax, c='red', edgecolors='black', s=150, zorder=2, label='Barcelona')

# Deportivo Alavés'in kornerlerini mavi noktalarla çizelim
alaves_df = df[df['takim'] == 'Deportivo Alavés']
if not alaves_df.empty:
    pitch.scatter(alaves_df.end_x, alaves_df.end_y, ax=ax, c='blue', edgecolors='black', s=150, zorder=2, label='Deportivo Alavés')

# 5. Başlık ve Gösterge (Legend) Ekle
plt.title("Başarılı Kornerlerin Düştüğü Noktalar (StatsBomb Verisi)", color='white', fontsize=16, pad=20)
ax.legend(loc='upper left', fontsize=12)

# 6. Grafiği Ekranda Göster
plt.show()
