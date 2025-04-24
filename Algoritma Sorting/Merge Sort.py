def mergeSort(aList):
    print("Splitting ", aList)
    if len(aList) > 1:
        mid = len(aList) // 2
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        # Rekursif panggil mergeSort pada bagian kiri dan kanan
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0

        # Proses menggabungkan kembali daftar yang terpisah
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                aList[k] = leftHalf[i]
                i = i + 1
            else:
                aList[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        # Salin elemen yang tersisa dari leftHalf, jika ada
        while i < len(leftHalf):
            aList[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        # Salin elemen yang tersisa dari rightHalf, jika ada
        while j < len(rightHalf):
            aList[k] = rightHalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", aList)

# Input manual dari user
aList = []
jumlah = int(input("Masukkan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    angka = int(input(f"Masukkan Angka Ke-{i+1}: "))
    aList.append(angka)

print("\nSebelum Diurutkan:", aList)
mergeSort(aList)
print("\nSetelah Diurutkan:", aList)
