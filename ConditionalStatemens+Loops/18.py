#Write a Python program to get the Fibonacci series between 0 and 50.
a, b = 0, 1
fib_series = []

while a <= 50:
    fib_series.append(a)
    a, b = b, a + b

print("Fibonacci series between 0 and 50:")
print(fib_series)
