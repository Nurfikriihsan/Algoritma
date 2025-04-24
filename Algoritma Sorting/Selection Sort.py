def selectionSort(aList):
    for i in range(len(aList)):
        minIndex = i
        for j in range(i + 1, len(aList)):
            if aList[j] < aList[minIndex]:
                minIndex = j
        aList[i], aList[minIndex] = aList[minIndex], aList[i]

# Input manual dari user
aList = []
jumlah = int(input("Masukkan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    angka = int(input(f"Masukkan Angka Ke-{i+1}: "))
    aList.append(angka)

print("\nSebelum Diurutkan:", aList)
selectionSort(aList)
print("\nSetelah Diurutkan:", aList)
