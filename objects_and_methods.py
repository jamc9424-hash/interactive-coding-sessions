#let's first recreate a variable or two

my_integer = 10
my_str = 'Hello world'
#you can always see the type of a variable using type()
type(my_integer)
type(my_str)

#what is stored inside the objects?

my_str.upper #upper is a METHOD that is attached to all of the objects of class string
#A method is like a function, it needs to be called.
#We put parenthese

my_str.upper() #HELLO WORLD
my_str.title()# Hello World
#why return a copy? DOESN"T change the original string

#other methiods
my_str.lower()
#what else is in there
my_str.endswith('!') #doesn't end with s ;
my_str.endswith('orld') #returne true
#methods are a way of pairing functions to specific types of objects

#some objects have other things than methods: properties
#propties are informaiton about the object that was created

my_integer.denominator #White wrenches are properties of the ocjects
my_integer.numerator
#properties are only meant to be read. They don't do anything. Just existr
#If something does not require any calculation to be given to you,
#and does not do anything, it is probably a property.
#but to be sure: look for the white wrench