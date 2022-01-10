#sinav_sonuc isimli liste olusturma.
sinav_sonuc = {'isimler':['ayse k.','ahmet m.','nuri c.','nawwar t.','suzan t.','ala b.'],
'cinsiyet':['k','e','e','e','k','k'],
'matematik':[60,40,97,45,56,95],
'türkce':[70,30,23,80,78,46]
}
# klavyeden girilen bilgileri sinav_sonuc  listesine ekleyen fonksiyon.

def ogrenci_bilgileri_guncelleme(isim,cinsiyeti,matematiknot,türkçe):
   sinav_sonuc['isimler'].append(isim)
   sinav_sonuc['cinsiyet'].append(cinsiyeti)
   sinav_sonuc['matematik'].append(matematiknot)
   sinav_sonuc['türkce'].append(türkçe)


# 2 yeni kayıt girmesini ekranaq yazdıralım
isim_1=input('1.Öğrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_1=input("Öğrencinin cinsiyeti erkek ise e Kız ise k harfini giriniz.")
matematik_1=input("Öğrencinin matematik dersinden aldığı notu giriniz:")
Türkçe_1=input("Öğrencinin Türkçe dersinden aldığı notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_1,cinsiyet_1,matematik_1,Türkçe_1)


isim_2=input('2. Öğrencinin ismini"isim soyismin_ilk_harfi." olarak giriniz:')
cinsiyet_2=input("Öğrencinin cinsiyeti erkek ise e Kız ise k harfini giriniz.")
matematik_2=input("Öğrencinin matematik dersinden aldığı notu giriniz:")
Türkçe_2=input("Öğrencinin Türkçe dersinden aldığı notu giriniz:")

ogrenci_bilgileri_guncelleme(isim_2,cinsiyet_2,matematik_2,Türkçe_2)


# güncellenmiş yeni kayıtları tabloya (sinav_sonuc listesini) ekrana yazdırma.
print(sinav_sonuc)

#listeyi daha düzenli yazdıralım.

print("İsimler:",sinav_sonuc['isimler'])
print("Cinsiyetleri (e olanlar erkek, kız olanlar k harfiyle gösterilmiştir.):",sinav_sonuc['cinsiyet'])
print("Matematik derslerinden alınan notlar:",sinav_sonuc['matematik'])
print("Türkçe dersinden alınan notlar:",sinav_sonuc['türkce'])
print("Not:cinsiyet ve notlar, isim listesine göre sırasıyla yazılmıştır.")