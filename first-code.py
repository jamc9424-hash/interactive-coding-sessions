print("Hello, World") # In our python file (also called a Python script).
print("Hello friends") # Final way of running Python code: Run a script in full

#What are the big variable types: String, Integer, Float, Boolean
this_string = "James" #This is a string, we ASSIGNED a value to a variable name

this_float = 3.14 #This is a float
this_int = 12 #This is an int
this_boolean = False #This is a boolean, case sensitive for False or True

#What can you do with variables?
#Only after the line is executed do the variables exist in python's memory
print(this_string)
print(this_float)

#What else can I print? 
print(this_string) #You can print a variable
print("Hello") #You can print a 'literal'
print(12) #You are directly printing an input, NOT a variable
print(12 + 5) #Printing an expression
#SKILL: Being able to 'trace the code'. Meaning reconstruct the steps of a code.
#Another example of an expression:
print(this_float + 5)

#what is print? A FUNCTION
#print() is a function. A function is a way of doing something in Python
#functions are 'called' using ().
#functions take a number of arguments (what goes inside the parentheses)
#some take zero, some take many

#how many arguments does print() take?
#it can take one:
print(this_float)
#it can take more!
print(this_float, this_int, this_string)
#print is printing all of its arguments on the same line

#let's do some calculations
print(2 + 3)
print(2*5)
print(2 + 3 * 5)
print((2 + 3) * 5) #Remember PEMDAS, Python follows it :D

print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3) #remember floating point errors :<)
#Operations with decimal numbers are by default, not mathematically 'exact'

#how can we avoid this?
#one way is to round

my_rounded_sum = round(0.1 + 0.2, 1)
print(my_rounded_sum)
print(my_rounded_sum == 0.3) #this is now true

#More logical comparisons
print(1 < 2)
print(1 > 2)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)

#you can also create more complex comparisons
print((1 < 2) and (3 > 2))
condition_1 = True
condition_2 = True
condition_3 = False
condition_4 = False
print(condition_1 and condition_2) #both true so true
print(condition_1 and condition_3) #false, when using 'and' in a sequence of conditions
#you have to have all conditions be true
print(condition_1 or condition_2) #true or true, TRUE
print(condition_1 or condition_3) #at least one of them is TRUE. OR requires at least one condition to be true
#Very important :}

print(False + False) #0
print(False + True)
print(True + True) #strange ....
print(True == 1) #true
print(False == 0) #true

print(False * 5)
print(True * 3 + 1) #simple stand-ins for 0 and 1

#let's continue the weirdness
greeting = "Hello " + "World"
print(greeting) #the meaning of + changes when you apply it
# to a string.
# + , when applied to strings, means concatenation. Bringing them
#into a single string

laugh = "ha " * 3
print(laugh) # * , is a repetition operator to concatenate the string a number
#of times

weird_laugh = "ha " * 3.14 #DOES NOT WORK

my_age = 21
my_intro = "I'm James and I am " + my_age
#returns a typerror (doesn't work:?
#when you want different type to work nicelky with each other
#gotta do some conversion firwst

#type conversions:
my_age_as_a_string = "21"
my_intro = "I'm James and I am " + my_age_as_a_string
print(my_intro)

#better way to do that is to convert types: str(), int(), float(), bool()

#how to use these fucktions:
print(str(42))
#is this really a string?
type(str(42))
#let's try others
str(3.14)
str(False)
str(0.1 + 0.2)
#we can convert pretty much evrything to a string

float('Hello!')
float('32')
float(False)
float('fifteen')

#For flooar is only somewtimes gonna wsork

int('hello')
int(True)
int(32)
int(3.14) #is it rounding or curring off demicals?
int(3.9)#cutting off :)

round(3.90)
#another great SKILL: Running experiments