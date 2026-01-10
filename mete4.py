müşteri = "Metehan"
müşteri2 = "Zincirkiran"
sonuç = müşteri + müşteri2
print("\t-Kullanici Karakter Sayisi 15 ile 20 arasinda olmak zorunda.")
print(f"\t-Müşteri İsmi Karakter Sayisi: {len(müşteri + müşteri2)}")
print("\t-Bu Kullanici adi uygun.")
print(f"\t-HOŞ GELDİNİZ {sonuç.upper()}")
print(f"\t-Kullanici Adi Me ile Me Başliyor?: {sonuç.startswith("Me")}")
print(f"\t-Kullanici Adi kiran ile Mİ Bitiyor?: {sonuç.endswith("kiran")}")