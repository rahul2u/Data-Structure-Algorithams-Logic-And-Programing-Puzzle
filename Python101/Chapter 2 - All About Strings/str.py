# string create 4 ways single,double,tripel and str function


my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a
multi-line string. It covers more than
one line'''

print(my_string)
print(another_string)
print(a_long_string)


my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""

print(my_string)
print(otherString)
print(tripleString)


# It should be noted that a string is one of Python immutable types. What this means is that you
# cannot change a string’s content after creation. Let’s try to change one to see what happens:

string1 = 'abcd '
# string1[0] = 'b'

# string concatnation
print(dir(string1))
for i in dir(string1):
    print(i)

print(help(string1.capitalize))


# String Formatting
my_string = "I like %s" % "Python"
var = "cookies"
newString = "I like %s" % var
# Just note that
# when you insert more than one string, you have to enclose the strings that you’re going to insert
# with parentheses.
another_string = "I like %s and %s" % ("Python", var)
print(another_string)

int_float_err = "%i + %.2f" % (1, 2.00)

print(int_float_err)

print("%(lang)s is fun!" % {"lang":"Python"})

print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})


# format method

print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))
print("Python is as simple as {1}, {0}, {2}".format("a", "b", "c"))
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))



