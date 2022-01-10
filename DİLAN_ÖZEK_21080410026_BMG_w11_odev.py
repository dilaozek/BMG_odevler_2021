
#isim Listesini tanımla 
kisiler=[]


#kisi isimlerini ekrana yazdırma 
x=input("isim giriniz:")
kisiler.append(x)
y=input("isim giriniz:")
kisiler.append(y)
z=input("isim giriniz:")
kisiler.append(z)
print("Liste:")
print(kisiler)

#Liste uzunlugunu hesaplama 
print("Liste uzunlugu:")
uzunluk= len(kisiler)
print(uzunluk)

#Listede 2. kisinin ismini ekrana yazdıralım
print("Listedeki 2. kisi:")
print(kisiler[1])


#Listedeki son ismi  çıkarma ve ekrana yazdırma
kisiler.pop()
print("Listedeki son kisi cıkarıldı,Yeni Liste:")
print(kisiler)