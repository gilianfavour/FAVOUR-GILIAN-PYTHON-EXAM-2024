# question 1 (i)

def circle_area(radius):
    
    # The formula for getting a circle
    pie = 3.14
    area = pie * radius**2
    
    # returning the area
    return area
    
circle_area(4)


# question 1 (ii)

# The list of the numbers given
def sum_of_odd_numbers():
    numbers = [4,7,2,9,12,15]
    total = 0

    # Using a for loop 
    for number in numbers:
        
        if number %2 == 1:
            print(number)
            
        else:
            pass

        # using the loop
    for number in numbers:
            total += number
    print(f' The sum of odd numbers is {total}')
sum_of_odd_numbers()
    
# question 1 (iii)

# defining the function
def two_numbers():
    # prompting the user to input the numbers
    first_number = int(input('Please insert the first number: '))
    second_number = int(input('Please insert the first number: '))

    # finding the sum
    sum = first_number + second_number
    print(f' The sum of {first_number} and {second_number} is :{sum}')
    
    # finding difference
    difference = first_number - second_number
    print(f'The difference between {first_number} and {second_number} is: {difference}')
    
    # finding product
    product = first_number * second_number
    print(f' The product of {first_number} and {second_number} number is: {product}')
    
    # finding the quotient
    quotient = first_number ** second_number
    print(f' The quotient of {first_number} and {second_number} is: {quotient}')
    
# calling the function
two_numbers()



# question 1 (iv)

# listing the dictionary
student_info = {
    'name':'Alice',
    'age' : 20,
    'grade' : 'A'
}

# updating the age to 26
student_info['age'] = 26
print(f'The updated age in the dictionary is: {student_info}')

# adding a new key value 
student_info['city'] ='Kampala'
print(f' A new key value added into the dictinary brings an output of: {student_info}')