list = [5,71,26,16,35,3,5,1,4]

def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()
        left = []
        right = []
        for number in list:
            if number <= pivot:
                left.append(number)
            else:
                right.append(number)
        left = quickSort(left)
        right = quickSort(right)

        return left + [pivot] + right

print(quickSort(list))
        