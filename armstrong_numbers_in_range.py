start = 1
end = 500

for number in range(start, end + 1):

    temp = number
    digits = len(str(number))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == number:
        print(number)