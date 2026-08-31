# --------------------- Without Function -------------

number = 123456

count = 0

while number > 0:

    number = number // 10

    count = count + 1

print("Digits:", count)


# <------- with funtion ---------->

def count_digits(number):

    count = 0

    while number > 0:

        number = number // 10
        count = count + 1

    return count


result = count_digits(123456)

print("Digits:", result)