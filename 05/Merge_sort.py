def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        colx, rowx = arr[:mid], arr[mid:]
        merge_sort(colx)
        merge_sort(rowx)

        coli, rowi, i = 0, 0, 0
        while coli < len(colx) and rowi < len(rowx):
            if colx[coli] < rowx[rowi]:
                arr[i] = colx[coli]
                coli += 1
            else:
                arr[i] = rowx[rowi]
                rowi += 1
            i += 1

        arr[i:] = colx[coli:] if coli != len(colx) else rowx[rowi:]


x = [5, 2, 8, 6, 10, 20, 50, 100]
merge_sort(x)
print(x)
