def fibonacci(number):
    i = 0
    first = 0
    second = 1
    fib_list = []
    for i in range(number):
        next = first
        fib_list.append(next)
        first = second
        second = next + second
    
    print(fib_list)