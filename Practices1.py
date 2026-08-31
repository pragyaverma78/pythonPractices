

students = [45, 78, 23, 91, 67]

prices = [500, 1200, 350, 999, 750]

marks = [88, 76, 95, 64, 89]

def find_numbers(numbers):
    
    greatest =  numbers[0]
    
    for number in numbers:
        if number > greatest:
            greatest = number
    
    return greatest

print(find_numbers(students))        
            
#    <---------------------smallest number ---------------------> 
        
students = [45, 78, 23, 91, 67]

prices = [500, 1200, 350, 999, 750]

marks = [88, 76, 95, 64, 89]

def find_numbers(numbers):
    
    greatest =  numbers[0]
    
    for number in numbers:
        if number < greatest:
            greatest = number
    
    return greatest

print(find_numbers(prices))  
 

# <-----------------------second largest number ------------------------->     
            