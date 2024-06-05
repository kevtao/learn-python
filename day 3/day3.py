def triangle_top(n):
    for index in range(0, n):
        white = f'{" "* (n - index - 1)}'
        print(f'{white}{"a" * (2 * index + 1)}{white}')

# triangle_top(5)

def triangle_down(n):
    for index in range(0,n):
        white = f'{" " * (index)}'
        print(f'{white}{"a" * (2 * (n - index)  - 1)}{white}')

# triangle_down(5)

def triangle_right(n):
    if n % 2 != 1:
        print("this function expects a odd number")
        return

    memoryImage = []
    for index in range(n):
        if index <= (n - 1) // 2:
            row = ' ' * ((n - index - (n - 1) // 2) - 1) + 'a' * (index + 1)
        else:
            row = ' ' * ((index - (n-2) // 2) - 1) + 'a' * (n - index)
        memoryImage.append(row)

    print('\n'.join(memoryImage))


# triangle_right(5)

def triangle_left(n):
    if n % 2 != 1:
        print("this function expects a odd number")
        return
    
    memoryImage = []
    for index in range(n):
        if index <= (n - 1) // 2:
            row = 'a' * (index + 1) + ' ' * ((n - index - (n - 1) // 2) - 1)
        else:
            row = 'a' * (n - index) + ' ' * ((index - (n-2) // 2) - 1)
        memoryImage.append(row)

    print('\n'.join(memoryImage))


# triangle_left(5)


def fib1(n):
    if n == 0 or n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)
#print(fib1(10))


def fib2(n):
    a, b = 0, 1
    for _ in range (n):
        a, b = b, a + b
    return a 
n = 10
print(fib2(n))