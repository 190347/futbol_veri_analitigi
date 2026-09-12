import json
import pandas as pd

# İndirdiğimiz repodaki örnek bir Şampiyonlar Ligi maçı
with open('events/15946.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

set_pieces = []

# Sadece pas olaylarını dön ve duran topları filtrele
for event in events:
    if event.get('type', {}).get('name') == 'Pass':
        pass_type = event.get('pass', {}).get('type', {}).get('name')
        
        # Eğer pas tipi Korner veya Serbest Vuruş ise listeye ekle
        if pass_type in ['Corner', 'Free Kick']:
            set_pieces.append({
                'dakika': event.get('minute'),
                'takim': event.get('possession_team', {}).get('name'),
                'vurus_tipi': pass_type,
                'baslangic_x_y': event.get('location'), # Topun vurulduğu yer [x, y]
                'bitis_x_y': event.get('pass', {}).get('end_location'), # Topun düştüğü yer [x, y]
                'sonuc': event.get('pass', {}).get('outcome', {}).get('name', 'Basarili')
            })

# Veriyi Pandas ile bir tabloya çevir
df = pd.DataFrame(set_pieces)
print(df.head(10))
from sqlalchemy import create_engine
import pandas as pd # Eğer yukarıda ekli değilse ekle

# Koordinat listelerini x ve y olarak ayrı sütunlara bölme
df[['start_x', 'start_y']] = pd.DataFrame(df['baslangic_x_y'].tolist(), index=df.index)
df[['end_x', 'end_y']] = pd.DataFrame(df['bitis_x_y'].tolist(), index=df.index)

# Eski liste formatındaki sütunları silme
df = df.drop(columns=['baslangic_x_y', 'bitis_x_y'])

# PostgreSQL bağlantısını kurma
engine = create_engine('postgresql://ferhatbilge:3091@localhost:5432/db_duran_top')

# Veriyi SQL tablosu olarak yazdırma
df.to_sql('set_pieces', engine, if_exists='append', index=False)

print("Veriler başarıyla db_duran_top veri tabanına aktarıldı!")
