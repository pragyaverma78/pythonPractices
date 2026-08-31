number = 1234

reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number = number // 10

print("Reverse:", reverse)





# <-----------with use function----------------->


def reverse_number(number):

    reverse = 0

    while number > 0:

        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    return reverse


result = reverse_number(1254)

print("Reverse:", result)