#exercise = odd or even
#Trouble : membuat program jika kelipatan 4 maka cetak pesan yang sesuai
#                          jika untuk dua nomor:
#       satu nomor untuk memeriksa (sebut saja num) dan satu nomor untuk dibagi dengan (periksa). 
#       Jika cek membagi secara merata menjadi num, katakan itu kepada pengguna. Jika tidak, cetak pesan yang sesuai.

for x in range (0,11):
    if x % 4 == 0:
        print ("Multiplication 4")
    elif x % 2 == 1:
        print("Odd")
    else:
        print("Even")