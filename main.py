a=5
b=15
liste=[1,3,5,7,9]


print("List içerisinde in operatörünün kullanımı : \n")
print("Liste : ",liste)
print("Listede a değişkenine karşılık gelen bir değer var mı ? " ,a in liste) #a=5 ve 5 değeri listenin içerisinde bulunmaktadır
print("Listede b değişkenine karşılık gelen bir değer var mı ? ",b in liste) #b=15 ve 15 değeri listenin içerisinde bulunmamaktadır.

print("\nStringler içerisinde in operatörü kullanımı : \n")
isim="Mehmet"
x="e"
y="a"
print("isim : ",isim)
print("isim adlı string değişkende e'ye karşılık gelen bir değer var mı ? " ,x in isim) #x="e" ve e değeri Mehmet içerisinde bulunmaktadır .
print("isim adlı string değişkende a'ye karşılık gelen bir değer var mı ? " ,y in isim) # y="a" ve a değeri Mehmet içerisinde bulunmamaktadır .