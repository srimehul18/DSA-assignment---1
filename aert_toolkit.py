class StackADT:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)



def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)



naive_calls = 0
memo_calls = 0


def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)



def fib_memo(n, memo):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]



def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)
    tower_of_hanoi(n-1, auxiliary, source, destination)



def binary_search(arr, key, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)

    else:
        return binary_search(arr, key, mid+1, high)



stack = StackADT()



print("Part B- Factorial Tests")
print(f"0! = {factorial(0)}")
print(f"1! = {factorial(1)}")
print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

print('\n')

print("Part B- Fibonacci Tests")

for n in [5,10,20,30]:

    naive_calls = 0
    memo_calls = 0

    print(f"Fibonacci({n})")

    naive_result = fib_naive(n)
    print(f"Naive Result: {naive_result}")
    print(f"Naive Calls Counts: {naive_calls}")

    memo_result = fib_memo(n, {0:0,1:1})
    print(f"Memo Result: {memo_result}")
    print(f"Memo Calls Counts: {memo_calls}")

print('\n')

print("Part C- Tower of Hanoi (N=3)")

tower_of_hanoi(3, 'A', 'B', 'C')

print('\n')

print("Part D- Binary Search Tests")

arr = [1,3,5,7,9,11,13]

print(f"Search 7: {binary_search(arr,7,0,len(arr)-1)}")
print(f"Search 1: {binary_search(arr,1,0,len(arr)-1)}")
print(f"Search 13: {binary_search(arr,13,0,len(arr)-1)}")
print(f"Search 2: {binary_search(arr,2,0,len(arr)-1)}")

print(f"Search in empty list: {binary_search([],5,0,-1)}")