array1 = [3,8,12,20,32,48]
array2 =[5,7,9,25,29]


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)

def merge(array1, array2):
    output = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            output.append(array1[i])
            i += 1
        else:
            output.append(array2[j])
            j += 1

    output += array1[i:]
    output += array2[j:]

    return output

print(mergeSort(array1))
