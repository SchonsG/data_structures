
def find_smallest(arr):
    smallest_value = arr[0]
    smallest_index = 0

    for item in range(1, len(arr)):
        if arr[item] < smallest_value:
            smallest_value = arr[item]
            smallest_index = item

    print(smallest_value)
    return smallest_index


def selectionSort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


print(selectionSort([5, 3, 6, 2, 10]))

