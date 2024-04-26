#Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
result = []

for num in range(100, 401):
    digits = [int(digit) for digit in str(num)]
    if all(digit % 2 == 0 for digit in digits):
        result.append(str(num))

print(",".join(result))
