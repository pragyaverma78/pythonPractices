number = 58392
smallest = 9

while number > 0:

    digit = number % 10

    if digit < smallest:
        smallest = digit

    number = number // 10

print(smallest)