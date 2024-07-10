from collections import deque
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
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

# search("you")


graph = {}
graph["you"] = {"alice", "bob", "claire"}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
    print(f"go to {node}")
