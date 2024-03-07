print("\n<< Prima dan Komposit >>")
print("-"*15)

min = int(input("Masukkan angka minimum: "))
max = int(input("Masukkan angka maksimum: "))

prima = []
komposit = {}

for i in range(min, max + 1):
    if i > 1:
        prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                komposit[i] = None  
                break
        if prime:
            prima.append(i)



print(f"Bilangan Prima:{prima}")


print(f"Bilangan Komposit:{komposit.keys()}")
