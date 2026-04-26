tuple = ("kalem","silgi","acacak","kalemlik")
print(type(tuple))#type fonksiyonunu kullanarak değişkenimizin türünü öğrendik
print(len(tuple))#len fonksiyonunu kullanarak tuplemizde kaç tane elemean ldugunu öğrendik
print(tuple)
for eşyalar in tuple:
    print(eşyalar)#demet oluşturmayi öğrendik peki bu demetin listelerden farki nedir ? cevap aslında basit listeler dğeiştirilebilir fakat demetler değiştirilemez,sonradan eleman eklenmez veya çıkartilamaz.
    
set1= {"kalem","silgi","acacak","kalemlik"}#burada {} kullandıgımız için bilgisayar bunun set(küme) oldugunu anladi
print(type(set1))#type fonksiyonu ile değişkenimiizin küme oldugunu öğrendik
print(len(set1))#len fonksiyonunu kullanarak kümemizin içindeki eleman sayisini bulduk
print(set1)#kümemizi terminale yazdirdik
for malzemeler in set1:#for döngüsünde kümemizi döndürdük fakat dikkatinizi çekerim her çalıştırdığımda kümemizin içindeki elemanların yerleri değişiyor.İşte kümenin özelliğide budur. elemanlarinin sirasi yoktur ve 1 eleman sadec 1 kez yazilir
    print(malzemeler)#kümeler yani setler sırasız bir değişkendir.İçindeki elemanlarin bir sirasi olmaz.
küme = {"araba","madalyon","kupa"}#Tekrardan {} ile bir set(küme) oluşturduk
küme.add("anahtarlik")#kümeye yeni bir eleman eklemek için add metodunu kullandik.
print(küme)#setimizin yeni halini terminale yazdirdik
küme.remove("kupa")#setimizden(kümemizden) "kupa" elemanini çikardik 
print(küme)#tekrardan yazdirdik 
set1 = {"kalem","silgi","acacak","kalemlik"}
set2 = {"kalem","silgi","acacak","kalemlik","miknatis","cam"}
print(set1.intersection(set2))#.intersection: iki kümede de olanlar yani set1 ve set2 kümelerinin ortak elemanlari,kesişimi
print(set1.union(set2))#.union: iki kümede de olan elemanlarin birleşimi
print(set2.difference(set1))#.difference: kümelerin farklarini gösterir.
print(f"Miknatis elemani set2 kümesinin elemani mi?: {"miknatis" in set2}")
print(f"Miknatis elemani set1 kümesinin elemani mi?: {"miknatis" in set1}")
print(f"Miknatis elemani 2 kümenin birleşiminde var mi?: {"miknatis" in set1.union(set2)}")
değişken = set({"kalem,silgi,acacak,kalemlik"})
print(değişken)
