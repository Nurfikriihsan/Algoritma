def insertionSort(aList):
    for index in range(1, len(aList)):
        currentValue = aList[index]
        position = index

        # Geser elemen-elemen yang lebih besar ke kanan
        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1

        # Masukkan currentValue ke posisi yang tepat
        aList[position] = currentValue


# Input manual dari user
aList = []
jumlah = int(input("Masukkan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    angka = int(input(f"Masukkan Angka Ke-{i+1}: "))
    aList.append(angka)

print("\nSebelum Diurutkan:", aList)
insertionSort(aList)
print("\nSetelah Diurutkan:", aList)
