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

i = 5

def f(arg=i):
    print(arg)

i = 6
f()