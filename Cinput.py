#exercise character input
#Trouble : membuat program sebuah input berupa nama dan usia..yang
#   akan dikirim 100 tahun kemudian

#Solve :
#1 Getting input
#gunakan syntax name_variabel=raw_input("Nama saya
#               age_variabel=input("Umur saya : ")
#                   print("Halo", name_variabel,"dan",age_variabel)

#2 Manipulasi String
#gunakan age = input("Enter your age: ")
#age = int(age)

#(or, if you want to be more compact with your code)

#age = int(input("Enter your age: "))

nama = input("Nama saya adalah: ")
usia = input("Umur saya adalah : ")
print("Hai",nama,usia,"akan bertambah 100 tahun kemudian")

usia1 = int(usia) + 100
print(usia1,"tahun", "akan muncul kemudian berupa")

#Solusi(harusnya bercerita pada usia 100 akan muncul pada tahun sekian)
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)