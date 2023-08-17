input_name = input("Adinizi giriniz: ")
print(input_name)

age_in_string = input("Yasinizi giriniz: ")
age = int(age_in_string)
print(age)

grade = 100.0
print(type(grade))

adi = input("Adinizi giriniz: ")
selamlama = "merhaba " + adi
print(selamlama)

a = int(input("bir sayı giriniz "))
b = int(input("başka bir sayı giriniz "))

print("girilen " + str(a) + " sayısı ile " + str(b) + " sayısının toplamı:", a+b)
print("girilen " + str(a) + " sayısı ile " + str(b) + " sayısının farkı:", a-b)
print("girilen " + str(a) + " sayısı ile " + str(b) + " sayısının çarpımı:", a*b)
print("girilen " + str(a) + " sayısı ile " + str(b) + " sayısının bölümü:", a/b)
print("girilen " + str(a) + " sayısı ile " + str(b) + " sayısının bölümünün tamsayısı:", a//b)
print("girilen " + str(a) + " sayısı ile " + str(2) + " sayısının üssü:", a**2)


