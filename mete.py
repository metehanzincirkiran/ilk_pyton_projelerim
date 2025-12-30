Şirket_Kasasi = 1000067
Ceo_Kazanci = 500057
Çalişan_Sayisi = 5675

Kalan_Para = Şirket_Kasasi - Ceo_Kazanci
Kişi_Başi_Gelir = Kalan_Para / Çalişan_Sayisi

print("\tŞİRKET GELİR DAĞİLİMİ")
print("-" * 40)
print(f"\n\tŞirket Kasasi : {Şirket_Kasasi}\n\t Ceo Kazanci: {Ceo_Kazanci}\n\t Çalişan Sayisi: {Çalişan_Sayisi}")
print(f"\n\t-Kalan Para: {Kalan_Para}")
print(f"\t-Kişi Başına Düşen Gelir: {Kişi_Başi_Gelir}")




print("=" * 50)

Oyuncu_Sayisi = 11
Maçta_Atilan_Sayi = 77
Maç_Süresi = 40

Kişi_Başi_Atilan_Sayi = Maçta_Atilan_Sayi / Oyuncu_Sayisi
Dakika_Başina_Atilan_Sayi = Maçta_Atilan_Sayi / Maç_Süresi

print("\tBASKETBOL TAKIM İSTATİSTİĞİ")
print("-" * 40)
print(f"\n\t-Oyuncu Sayisi: {Oyuncu_Sayisi}\n\t-Maçta Atilan Sayi: {Maçta_Atilan_Sayi}\n\t-Maç Süresi: {Maç_Süresi}")
print(f"\n\t-Dakika Başina Atilan Toplam Sayi: {Dakika_Başina_Atilan_Sayi}\n\t-Kişi Başina Atilan Sayi: {Kişi_Başi_Atilan_Sayi}")