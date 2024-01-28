#Write a program to print the first n numbers of a Fibonacci sequence
#i: number(int) o: number

def fib (n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


i = 1
n = input("Please type in a number: ")

while i <= int(n):
    print(fib(i))
    i+=1