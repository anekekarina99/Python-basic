#membuat list baru
#menggunakan append
# x = []
# x.append (3)
## example
#list1 = ['C++', 'Java', 'Python']
#list1.append('C#')
#print ("updated list : ", list1)


x = [1]
x.append (3)
print("updated list : ", x)

b = [1,3]
b.append ('Aneke')
b.append ('[5,6,7]')
print("updated list : ",b) 

#bisa menggunakan for
for x in b:
    print(x)

#bisa menggunakan if
for x in range (1,5,2):
    x = input(" ")
    if x >= 3:
            print("Aneke","[5,6,7]")

#solution
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# num = int(raw_input("Choose a number: "))

#  new_list = []

# for i in a:
#	if i < num:
#		new_list.append(i)

# print new_list