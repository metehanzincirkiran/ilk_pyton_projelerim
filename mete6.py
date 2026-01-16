takim_kaptani = "Metehan"
sayi_ortalamasi_hedefi = 30 >= 30
çiktiği_maç_sayisi = 12
toplam_attiği_sayi = 200
maç_başi_sayi_ortalamasi = toplam_attiği_sayi / çiktiği_maç_sayisi
print("\t-TAKİM KAPTANİ SEZON İSTATİSTİĞİ")
print(f"\t-Takim Kaptani: {takim_kaptani}\n\t-Maç Başi Sayi Hedefi: {sayi_ortalamasi_hedefi}\n\t-Çiktiği Maç Sayisi: {çiktiği_maç_sayisi}")
print(f"\t-Sezon Boyunca Attiği Toplam Sayi: {toplam_attiği_sayi}")
hedefe_ulaşti_mi = maç_başi_sayi_ortalamasi > sayi_ortalamasi_hedefi
print(f"\t-Sezon Sonu Hedefine Ulaşti Mi: {hedefe_ulaşti_mi}")
print(f"\t-Bu Hangi Sayi Tipi: {type(toplam_attiği_sayi)}")
print(f"\t-Toplam Attiği Sayi 200e Eşit Mi?:{toplam_attiği_sayi == 200}") 