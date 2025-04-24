def bubbleSort(aList):
    n = len(aList)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                swapped = True
        if not swapped:
            break

# Input manual dari user
aList = []
jumlah = int(input("Masukkan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    angka = int(input(f"Masukkan Angka Ke-{i+1}: "))
    aList.append(angka)

print("\nSebelum Diurutkan:", aList)
bubbleSort(aList)
print("\nSetelah Diurutkan:", aList)
