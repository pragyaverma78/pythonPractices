# without function
number= 8

factorial= 1

for i in range(1,number+1):
    factorial = factorial * i
    print ("factorial", factorial)
    
    
    
# <------------ with use function -------------->

def check_factorial_number(number):
    result=1
    for i in range (1,number+1):
        result = result*i
        
    return result 

answer = check_factorial_number (6) 
print(check_factorial_number,answer) 
     
  