def fib(n):
    lst=[0,1]
    for i in range (n):
        lst.append(lst[-1]+lst[-2])
    return lst


result=fib(10)

print(result)