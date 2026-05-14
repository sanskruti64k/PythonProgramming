"""
Ask the user enter the two number and do the addition of the two numbers

Logic:
1. I will ask the user to enter the number
2. Two number will be assigned to the variable
3. var = v1 + v2
4. print new assigned variable i.e var

Execution:
1.input() : will take user input as string and return it back to caller function(main) as a string value
2.Assign two variables with input()
variable1 = int(input()); here we are converting the user input into integer number int()) so that we
3.Assign variable; ans = variable1 + variable 2
4.Print output"""

a = int(input("Enter the first number : "))
b = int(input("Enter the first number : "))
ans = a+b
print(ans)
print(type(ans))

# %%

Name = input("enter your name:")
print(Name)
print(type(Name))

'''
Note: 
1.Python is Case sensitive
2.()--> function --- in-built function
3.assignment with UNDERSCORE ( _ ) is valid variable 
4.dash (-) invalid

- Variable should always Start with alphabet

- STRING must always be in quotes

- Multiple assignment of variable with differnt datatypes

- Boolean is always in camel casing 
it will not accept in all small and all caps
'''
# Data types of Python Programming
'''
1. integer
2. float
3. string
4. boolean
5. list
6.tuple
7. sets
8. dictionary

'''
a = 100
c_ = 12
print (a,c_)

pi = 3.14
name = 'India'
print(type(name))
India,Pak,USA = 100,200.45,'usa'
print(type(USA))

a = True
b = False
print(a and b)
print(a or a)