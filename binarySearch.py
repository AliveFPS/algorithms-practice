list = [5,1,7,3,8,2,552,3]


def binarySearch(list, element):
    list = sorted(list)
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == element:
            return element
        elif list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

print(binarySearch(list,8))



    