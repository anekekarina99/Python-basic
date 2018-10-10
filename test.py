i=0
while True:
    print(i)
    if i==10 :
        break
    i+=1

#buat prima sumber internet
def prime(x) : #Membuat function bernama prime dan var x sebagai angka yg akan di input.
    prim = True #Membuat var bernama prim
    if x > = 2 :  #Jika x yang diinput lebih besar dari 2, maka :
        for i in range(2, x) #looping dengan nilai i adalah angka 2 sampai nilai (x-1) yang diinput.
            if x % i == 0 : #Jika x yang diinput dibagi i sama dengan 0(tidak ada sisa), maka :
                prim = False #nilai var prim adalah False
    else : #Jika x yang diinput selain x >= 2 berati nilai x < 2, maka :
        prim = False #Nilai var prim adalah False (karena x < 2 bukanlah nilai prima)
    return prim #Mengembalikan nilai var prim asalnya yaitu True.