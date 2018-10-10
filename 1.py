a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

N = [1,3]

for x in a:
    if x < num:
        N.append([5,6,7])

print("updated list : ",N)