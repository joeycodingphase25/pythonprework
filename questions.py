    #Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(name1):                         # name = parameter
    return (f"hello_{name1.upper()}")

name = input("What is your name? ")

print(hello_name(name))                       # name is argument = the value that the parameter takes

#Question 2
 #Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():


def first_odds():
    for value in range(100):
        if value % 2 == 1:
            print(value)

first_odds()

# Question 3:

def max_num_in_list(a_list:list):
    a_list.sort()
    return a_list[-1]

print(max_num_in_list([1,2,3,5,6,7]))

# Question 4:
# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

#def leap_year_check():
   # year = input("Enter a Valid year ")
   # if year / 4 == int():
     #   return True      
   # else:
    #    return False
#leap_year_check()

#SOURCE: TheProgrammingPortal on YouTube
def leap_year_check(year):
    if year % 4 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False
year = int(input("Please type year here "))

if leap_year_check(year):
    print("That is a Leap Year, Bud")
else:
    print("Not a leap year, sorry bud.")

# Question 5


def new_consecutive(a_list):
    
    for i in range(len(a_list)-1):
        if a_list[i] != (a_list[i+1]-1):
            return False
    return True

if new_consecutive([1,2,3,4,5,6]):
    print("Congrats, this is a consecutive number list!")
else:
    print("these are not consecutive numbers!")




# def is_consecutive(a_list):    
#     if a_list == a_list.sort():
#         return True    
#     return False
# a_list = [1, 2, 3, 4, 5, 6]
# if is_consecutive(a_list):
#     print("Congrats, this is a consecutive number list!")
# else:
#     print("these are not consecutive numbers!")

