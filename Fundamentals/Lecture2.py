# Concept of Print Function

#Method 1 f-string
# %%
name = 'chandan'
age = 22
salary = 600000
print(f'Hello My name is {name} and my age is {age} and salary is {salary}')

#Method 2 .format method(dotformat)
print('Hello My name is {} and my age is {} and salary is {}'.format(name,age,salary))

# %%
lst1 = [] #List can be empty
lst2 = [1,2,3,56.45,"Hi","World",True,False,[10,20,30],(100,200,300),{1,2,3},{"India":1000},None]
       # int, float, string,     bool,       list,      tuple,        set,    dictionary,   none

#Control Flow ------Conditional Statements
#If Condition
#Ask a user to enter name
name = input("Enter you name :")
if name== "chandan":
    print(f'Your name is {name}')

#%%
#Ask a user to print Head or tail if head print win otherwise print lose

Coin_side = input("Enter coin side:")
if Coin_side.lower() =="head":
    print("You win the game")
else:
    print("You lose the game")
    
# %%
#head -you win,tail - I win, other invalid entry ----will work but wrong logic

Coin_side = input("Enter coin side:")
if Coin_side.lower() == "head":
    print("You win the game")
if Coin_side.lower() == "tail":
    print("I win the game")
else :
    print("Enter correct coin side :")

# %%
#if-elif-else

Coin_side = input("Enter coin side:")
if Coin_side.lower() == "head":
    print("You win the game")
elif Coin_side.lower() == "tail":
    print("I win the game")
else :
    print("Enter correct coin side :")

# %%
#Concept of Indexing and Slicing

str = "Welcome to the world of python programming"
str1 = "Hello World"
print(str1[6])  #space is also count as index
print(str[-5])
print(str[6:-2])
print(str[-5:-2])
print(str[::2])

# %%
'''
Write a program to check whether the entered word is a palindrome or not

Logic:
1.Ask user to enter a String
2.Reverse the String
3.Compare the Original String with the new String
4.If true the Palindrome otherwise not a palindrome

'''

string = input("Enter a string:")
string1 = string[::-1] #str1[start:stop:step] : --> -1 means reverse the string
if string == string1:
    print(f"{string} is a palindrome")
else :
    print(f"{string} is  not a palindrome")

# %%
'''
Write a program to check the report status of student
90+ excellent
80+ good
70+ moderate
60+ pass
'''
score = int(input("Enter you Score :"))
if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 70:
    print("Moderate")
elif score >= 80:
    print("PASS - Can do better")
else :
    print("Fail")
# %%
