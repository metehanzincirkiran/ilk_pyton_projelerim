kitaplar = [1,6,4,5,7,9,6,5,4,] # [] bu iki parentez arasına koyarakta liste yapılabilir. Fakat çok virgül ve ""içerdiği için hata iihtimali artar.
kitaplarin_renkleri = "Mavi Sari Kirmizi Bordo Yeşil".split() # .split() methoduyla direkt değişkenin içine "" içine yazdıgımız şeyler listeye dönüşür.(stringler içim!!)
print(f"-Kitaplarin Sira Numaralari: {kitaplar}\n-Kitaplarin Renkleri: {kitaplarin_renkleri}")
print(len(kitaplarin_renkleri))#len fonskiyonuyla kaç tane kitap rengi olduğunu öğrendik .
print(kitaplarin_renkleri[0])#İlk kitap rengini öğrendik.
print(kitaplarin_renkleri[::2])#İkişer ikişer listedeki verileri saymasını istedik
kitaplarin_renkleri.append("Turuncu")#.append() methodunu kullanarak listenin sonuna bir renk daha ekledik.
print(kitaplarin_renkleri)
kitaplarin_renkleri.insert(2,"Kahve Rengi")#.insert() methodunu kullanarak istediğimiz indexe bir renk ekledik.
print(kitaplarin_renkleri)
print(len(kitaplarin_renkleri))#Tekrardan listedeki renk sayısını len fonksiyonunu kullanarak öğrendik
kitaplarin_renkleri.remove("Turuncu")#.remove() methodunu kullanarak listenin içindeki belirttiğimiz bir veriyi sildik.
print(kitaplarin_renkleri)
kitaplarin_renkleri.remove("Kahve Rengi")#.remove()Kullanarak yine tekrardan belirttiğimiz bir rengi sildik
print(kitaplarin_renkleri)
kitaplarin_renkleri.append("Lacivert")#.append() methodunu kullanarak tekrardan listenin sonuna bir renk daha ekledik.
print(kitaplarin_renkleri)
kitaplarin_renkleri.insert(0,"Lacivert")#.insert() methodunu kullanarak belirttiğimiz bir yere belirtiğimiz bir rengi ekledil.
print(kitaplarin_renkleri)
kitaplarin_renkleri2 = ["Pembe","Turkuaz"]#yeni bir değişken açtik.
kitaplarin_renkleri.extend(kitaplarin_renkleri2)#.extend() methodunu kullanarak ilk değişkenimizin sonuna ikinci değişkenimizdeki verileri liste şeklinde aktardık.
print(kitaplarin_renkleri)
silinen_renk = kitaplarin_renkleri.pop(1)#.pop() methodu 
print(f"Silinen Renk: {silinen_renk}") #burda .pop() methodunu kullanarak listesinden bir renk sildiğimiz değişkeni f'string yöntemiyle sildiğimiz rengi belirttik.
kitaplarin_renkleri.reverse() #.reverse()bu tersine çevir demek. 
print(kitaplarin_renkleri)#.reverse()kullanarak değişkenimizi tersine çevirdik.
kitaplar.reverse()#sayılardan oluşan listemizi terse çevirdik burda yine .reverse() metodunu kullanarak.
print(kitaplar)
kitaplarin_renkleri.sort()#.sort() stringleri alfabetik olarak sıralar . Egerki bir sayıysada büyükten küçüğe sıralar.
print(kitaplarin_renkleri)#.sort() burada alfabetik olarak sıraladı çünkü stringlerden oluşan bir liste.
kitaplar.sort()#Burada .sort() büyükten küçüge sıraladı çünkü değişken listesi sayılardan oluşuyor.
print(kitaplar)
kitaplar.sort(reverse=True)#.sort(reverse=True) methodunu kullanarak tersten bu seferde büyükten küçüğe sıralattık.
print(kitaplar)
