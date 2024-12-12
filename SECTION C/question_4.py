# Question1 (i)
# a)  OOP is object oriantated Programm that takes in classes and objects including methods.

# OOP is significant in ways that it helps in performing day to day tasks.

# b) #A class is  an object constructor or blueprint for creating objects.
    # An object is comes from a class and takes properties of a class.

#question 4 (ii)

# programm that counts the occurace
def word_occurance():
    example = 'python exam'

    # using the split to separate the 2 words
    words = example.split()

    # using word count to find the specified number of words
    word_count = {}


    for word in words:
        word_count[word]=word_count.get(word,0)+1
        # print('Word occurances')
        
    for word, count in word_count.items():
        print(f'{word}:{count}')
        
word_occurance()

# question4 (iii)

# the function
def sum_of_numbers(a,b):
    
    # getting their sum
    sum = a+b
    
    # returning the result
    return(sum)
    
# calling the function with the values used for testing
sum_of_numbers(3,4)


# question4(iv)

class Car:
    
    # using init with attributes of the car class
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
        
    # instance for the car class and printing
details = Car('Toyota', 'V8', 'Black')
    
print(details.brand)
print(details.name)
print(details.color)


# question4 (v)
# Adding a method to the car class
class Car:
    # using the init 
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
        
    # adding a method to the car class
    def __init__(self,start_engine):
       self.start_engine = start_engine
    
    # the instance for the car and calling the method
start = Car('The engine of the car has started.')
print(start.start_engine)