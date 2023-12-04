# **********************************************************************************************************************

#  Default Argument Values:

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')  
            # notice!!! ValueError will stop the run of the program.
        print(reminder)


# check the function with some examples: 

# example 1: the program will ask in the terminal 'Do you really want to quit?', 
# if the user answers 'no' it will exit the loop.
# if the user answers 'yes' it will exit the function and return True.
# if the user answers anything else (example- 'maybe'/'j'...) it will go over the loop again, 
# the number of times the program will run depends on the number we inserted to the 'retries' parameter.
ask_ok('Do you really want to quit?')

ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# **********************************************************************************************************************

# The default values are evaluated at the point of function definition in the defining scope
# the following call for the f function will print '5' instead of 6. 

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# Important warning: The default value is evaluated only once. 
# This makes a difference when the default is a mutable object such as a list, dictionary, 
# or instances of most classes. 
# For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# This will print: 
# [1]
# [1, 2]
# [1, 2, 3]
# If you don’t want the default to be shared between subsequent calls, 
# you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# **********************************************************************************************************************


# When a final formal parameter of the form **name is present, it receives a dictionary 
# (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. 
# This may be combined with a formal parameter of the form *name (described in the next subsection) 
# which receives a tuple containing the positional arguments beyond the formal parameter list. 
# (*name must occur before **name.) 
# For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# and of course it would print:

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.s
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


# **********************************************************************************************************************


# Special parameters
# By default, arguments may be passed to a Python function either by position or explicitly by keyword. 
# For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer 
# need only look at the function definition to determine if items are passed by position, by position or keyword, 
# or by keyword.

# A function definition may look like:

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

# where / and * are optional. 
# If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: 
# positional-only, positional-or-keyword, and keyword-only. 
# Keyword parameters are also referred to as named parameters.
