# ---------------- Without Function ---------------->
number = 1234

total = 0

while number > 0:

    digit = number % 10

    total = total + digit

    number = number // 10

print("Sum:", total)


#--------------- With Function ------------

def sum_of_digits(number):

    total = 0

    while number > 0:

        digit = number % 10
        total = total + digit
        number = number // 10

    return total


result = sum_of_digits(1234)

print("Sum:", result)