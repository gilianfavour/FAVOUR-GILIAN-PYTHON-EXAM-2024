# question 2 (i)

def student_details():
# # Entering the details from the keyboard

    student_name = input('Please input your name: ')
    student_number = input('Please input your student number: ')
    programming = int(input('Please enter the marks scored in Proramming: '))
    data_sceine = int(input('Please enter the marks scored in Data Science: '))
    computer_applications = int(input('Please enter the marks scored in Computer Applications: '))
    
    
    # calculating the average mark
    average_mark = (programming+data_sceine+computer_applications)/3
    print( f'The average mark is {average_mark}' )
    
student_details()

#question2 (ii)

# Asking the user to input the values
miles_driven = float(input('Input the number of Miles Driven:'))
gallons_of_gas_used = float(input('Input the number of gallons used: '))

# # formula for the miles per gallon
# MPG = miles_per_gallon
MPG = miles_driven/gallons_of_gas_used

#printing the result
print(MPG)


# question2 (iii)

# Printing all number from 1 to 100 that are not divisible by 2
def number_not_divisible_by_2():
    for number in range(1,100):
        if number %2 != 0:
            print(number)
            
        else:
            pass
        
number_not_divisible_by_2()