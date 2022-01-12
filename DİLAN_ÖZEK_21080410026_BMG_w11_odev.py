
#isim Listesini tanımla 
mans=[]


#kisi isimlerini ekrana yazdırma 
x=input("isim giriniz:")
mans.append(x)
y=input("isim giriniz:")
mans.append(y)
z=input("isim giriniz:")
mans.append(z)
print("Liste:")
print(mans)

#Liste uzunlugunu hesaplama 
print("Liste uzunlugu:")
uzunluk= len(mans)
print(uzunluk)

#Listede 2. kisinin ismini ekrana yazdıralım
print("Listedeki 2. kisi:")
print(mans[1])


#Listedeki son ismi  çıkarma ve ekrana yazdırma
mans.pop()
print("Listedeki son kisi cıkarıldı,Yeni Liste:")
print(mans)
