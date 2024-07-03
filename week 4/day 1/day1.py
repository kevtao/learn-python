array = [5,3,9,2,7,1]


# test usin o(n)
def largest():
    currnum = array[0]
    for n in range(len(array)):
        if array[n] > currnum:
            currnum = array[n]
    print(currnum)
# largest()

# test using o(n)
def findSmallest(arr):
    small = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < small:
            small = arr[i]
            smallest_index = i
    return smallest_index

# creating o(n^2)
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        small = findSmallest(arr)
        newArr.append(arr.pop(small))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
