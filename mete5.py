sayi1 = 12
sayi2 = 22 / 2
Sonuç = sayi1 * sayi2
sonuç2 = sayi1 ** sayi2
print(sayi1)
print(sayi2)
print(sayi1 * sayi2)
print(f"İki değişkenin çarpiminin sonuci: {Sonuç}")
print(f"Üs alma işleminin sonuci: {sonuç2}")



#PYTHON MATEMATİKSEL OPERATÖRLER
#Toplama = +
#Çikarma = -
#Çarpma = *
#(Üs)Kuvet alma = **
#Bölme = / (Bu float böler her zaman sonuç tam olsa bile sonuna .0 getirir.)
#Tamsayı Bölme = // (Bu iteger böler her zaman, say irgülliyse bile virgülü görmez.)
#Mutlak Değer = abs
#Yuvarlama = round 
#Not: çıktıda sayının sonunda . varsa bu bir float'tir mesela 10.0 veya 12.12 gibi
#ama çıktıda direkt noktasız bir sayı varsa mesela 1 veya 10 gibi bu integer'dir.

mat1 = 22 / 7 # / bu float demektir. 
mat2 = 22 // 7 # // bu intteger demektir.
print(mat1)
print(mat2)

print(round(mat2))
print(3 * (6 + 4))

#Karlilaştırma Operatörleri
#Eşit midir: == ÖRN: print(10==10) çıktıda TRUE yazar.
#Eşit değil midir: != ÖRN: print(5 != 4) çıktıda TRUE yazar.
#Büyüktür: > ÖRN: print(4 > 3) Çıktıda TRUE yazar.
#Küçüktür: < ÖRN: print(4 < 5) Çıktıda TRUE yazar.
#Büyük eşit mi: >= ÖRN: print(5 >= 5) Çıktıda TRUE yazar.
#Küçük eşit mi: <= ÖRN: print(6 <= 10) Çıktıda TRUE yazar.

ar = "100"
ar2 = 100
ar3 = int(ar)
print(ar3 == ar2)

ba = 35
be = "62"
bc = int(be)
print(ba < bc)

sayi3 = int(66.9) # İntegerlarda tam sayılık ksıımlara bakılır.
print(sayi3)
sayi4 = float(78.84)
print(sayi4)
sayi5 = round(26135.98)
print(sayi5)