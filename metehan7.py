print("\t-UYGULAMA KURALLARİ")
print("\t1-Kullanici adi 8 karakter olmalidir.")
print("\t2-Şifre, kullanici adi karakter sayisiyle eşit olmalidir.")
print("\t3-Kulanici adi büyük harf ile başlamalidir.Unutulursa uygulama otomatik olarak büyütür.")
print("-" * 80)
Kullanici = "muhammet"
Şifre = "12345678"
print("\t-Kullanici: muhammet")
print("\t-Şifre: 12345678")
print(f"\t-Kullanici Karakter Sayisi: {len(Kullanici)}: Karakterter Sayisi Uygun.") 
print(f"\t-Baş Harf Büyütme: {Kullanici.capitalize()}: Uygun.")
print(f"\t-Şifre Karakter Sayisi: {len(Şifre)}: Şifre Kullanici İsmiyle Uyuşuyor,Uygun.")
print("\t-Robot Olmadiğinizi Doğrulamak Amaciyla Şifreniz ile Oluşturulmuş Soruyu Yanitlayiniz.")
Şifre_Denetim = 1+2+3+4+5+6+7+8
print(f"\t-Şifreniz olan {int(Şifre)}'deki sayilarin toplami {Şifre_Denetim} mi?")
print("*" * 80)
print("\t-Muhammet Hoş Geldiniz <3")
