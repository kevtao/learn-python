array = [5, 3, 9, 2, 7, 1]


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


# print(selectionSort([5, 3, 6, 2, 10]))


# breadth width search

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
 return name[-1] == 'e'
from collections import deque
search_queue = deque()
search_queue += graph["you"]
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
