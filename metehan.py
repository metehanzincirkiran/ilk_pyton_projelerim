Ay_Sonu_Şiret_Kazanci = 50000
Ceo_Kazanci = 40000
Çalişan_Sayisi = 5

Kalan_Para = Ay_Sonu_Şiret_Kazanci - Ceo_Kazanci
Kişi_Başina_Düşen_Para = Kalan_Para / Çalişan_Sayisi

print(f"TOPLAM PARANİN DAĞİTİMİ")
print(f"^" * 40)
print(f"Toplam Şirket Kazanci : {Ay_Sonu_Şiret_Kazanci}: Dolar")
print(f"Toplam Ceo Kazanci : {Ceo_Kazanci}: Dolar")
print(f"Toplam Çalişan Sayisi : {Çalişan_Sayisi}: Kişi")
print(f"^" * 40)

print(f"Sonuç : {Çalişan_Sayisi} kişinin her birine {Kişi_Başina_Düşen_Para}")
