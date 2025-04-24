def quickSort(aList):
    quickSortHelper(aList, 0, len(aList) - 1)

def quickSortHelper(aList, first, last):
    if first < last:
        splitPoint = partition(aList, first, last)
        quickSortHelper(aList, first, splitPoint - 1)
        quickSortHelper(aList, splitPoint + 1, last)

def partition(aList, first, last):
    pivotValue = aList[first]
    leftMark = first + 1
    rightMark = last

    done = False
    while not done:
        while leftMark <= rightMark and aList[leftMark] <= pivotValue:
            leftMark = leftMark + 1
        while aList[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark = rightMark - 1
        if rightMark < leftMark:
            done = True
        else:
            aList[leftMark], aList[rightMark] = aList[rightMark], aList[leftMark]

    aList[first], aList[rightMark] = aList[rightMark], aList[first]

    return rightMark

# Input manual dari user
aList = []
jumlah = int(input("Masukkan Jumlah Angka Yang Ingin Diurutkan: "))
for i in range(jumlah):
    angka = int(input(f"Masukkan Angka Ke-{i+1}: "))
    aList.append(angka)

print("\nSebelum Diurutkan:", aList)
quickSort(aList)
print("\nSetelah Diurutkan:", aList)
