#<----------------- Without Function-------------->

number = 121

original = number
reverse = 0

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number = number // 10


if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# with function 

def is_palindrome(number):

    original = number
    reverse = 0

    while number > 0:

        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False


result = is_palindrome(121)

print(result)    