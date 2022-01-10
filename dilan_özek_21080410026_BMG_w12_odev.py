#sinav_sonuc sözlük tablosu olusturma
sinav_sonuc = {'isimler':['ayse k.','ahmet m.','nuri c.','nawwar t.','suzan t.','ala b.'],
'cinsiyet':['k','e','e','e','k','k'],
'matematik':[60,40,97,45,56,95],
'türkce':[70,30,23,80,78,46]

}
print (sinav_sonuc ['isimler'])
print (sinav_sonuc['isimler'][3])

count_k=0
count_e=0

#sinav_sonuc isimli sözlüge kaydeden fonksiyon tanımlama.
def sinav_sonuc ():
    print ('isimler') 
    print ('cinsiyet')
    print ('matematik')
    print ('turkce') 

    sinav_sonuc()