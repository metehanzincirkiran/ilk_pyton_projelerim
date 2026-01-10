
print("\n" * 50)
# Burada temelimizi sağlamlaştıracak bir çalişmaya geçeceğiz.

kod = "Selam" 
print(kod.upper())
print(kod) #Aslinda değişkenimiz ayni burada .upper()'in mantıgını anlıyoruz her şeyi büyütmeye yarıyor.
kod = kod.upper() #Burada .upper() metodunu kod değişkenine atadığimizden dolayi artık fonksiyon içine her kod yazdıgımızda tüm harfleri büyük yazcak.
print(kod)
print(kod.lower()) #Burada .lower() Metodu değişkendeki tüm harfleri küçültmemizi sağlar.
kod = kod.lower() #.lower() Metodunu kkod değişkenine ekledim böylece print içine her kod yazdıgımda küçük harfe çevircek.
print(kod)
print(kod.capitalize())#.capitalize() Methodu değişkenin baş harfini büyük yazmamızı sağlar.
kod = kod.capitalize() #.capitalize() Methodunu kod değişkenine ekledim böylece print içine yazdıgım her kod da ilk harfini büyük yapacak.
print(kod)

#Burada biraz daha derine iniyoruz.
print("\n"* 30)

not1 = "Metehan"
not2 = "Zincirkiran"
print(not1.startswith("Mete")) #.startswith() metodu kodun başında girdiğin karakter varsa true der yoksa false der.
print(not2.startswith("Zincir"))
bir_kullanici_ismi = not1 + not2
print(bir_kullanici_ismi.startswith("MetehanZincirkiran"))

print(bir_kullanici_ismi.endswith("an")) # .endswith() methodu başına girdiğin karakterin sonunda mevcutsa true der sonunda mevcut değilse false der.
print(bir_kullanici_ismi.endswith("Zincirkiran"))
print(bir_kullanici_ismi.endswith("kiran"))

print(len(bir_kullanici_ismi)) # len fonksiyonu değişkenin kaç karakterden oluştugunu sayar.
print(len(not1))
print(len(not2))
print(not1.upper()) # .upper metodu değişkendeki tüm karakterleri büyük yaptı.
print(not1.lower()) # .lower metodu değişkendeki bütük karakterleri küçük yaptı.
print(not1.capitalize()) # .capitalize() metodu Değişkenin baş harfini büyütür.
print(not1.startswith("Mete")) # .startswith() metodu değişkenin başındaki harfleri sorgular "" içine yazmamızın sebebi ise bilgisayar işlem yapmıyor bize sadece olanı söylüyor.
print(not1.endswith("han")) # .endswith metodu değişkenin son harflerine bakar harf bulunuyorsa true bulunmuyorsa false ama sonunda
print(len(not1 + not2)) # Bu eski bir yöntemacemi işi.
print(f"{len(bir_kullanici_ismi)}") # Burada f-string kolaylıgından yararlanarak oluşturuyoruz. Modern yöntemdir uzun uzun toplama çıkarmayla ugrastırmaz.
