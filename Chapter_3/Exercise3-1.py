# write a function name right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter
# of the string is in column 70

def right_justify(s):
    print(' '* (70 - len(s)) + s)

right_justify('hi')
