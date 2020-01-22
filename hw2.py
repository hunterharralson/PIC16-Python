'''
Hunter Harralson
304781158
PIC16 - Homework 2
'''

# Problem 1

# Function longestpath finds length of the longest path in a dictionary
def longestpath(d):
    '''
    INPUT - dictionary d
    OUTPUT - length of the longest path
    '''
    longest_path = 0
    
    for key in d:
        seen = [] 
        seen.append(key)
        value = d[key]
        current_path = 1
        
        while (value in d.keys() and value != d[value] and value not in seen):
            current_path+=1
            seen.append(value)
            value = d[value]
        
        longest_path = max(longest_path,current_path)
        
    return longest_path


# Testing 
d1 = {'a':'b', 'b':'c'}
print(longestpath(d1)) # 2

d2 = {'a':'b', 'b':'c', 'c':'d', 'e':'a', 'f':'a', 'd':'b'}
print(longestpath(d2)) # 5


# -----------------------------------------------------------------------------------------


# Problem 2 

from math import exp,sin,cos

# Function solve implements Newton's method for finding the root of a function
def solve(f,guess,tolerance):
    '''
    INPUT: 
        f - the function and its derivative
        guess - initial guess for the root of the function
        tolerance - very small number
    OUTPUT: 
        guess - the root of the function
    '''
    
    while abs(f(guess)[0]) > tolerance:
        guess = guess - f(guess)[0]/f(guess)[1]
    return guess
        
    
# Test Cases: 
solve(lambda x: [x**2-1, 2*x], 3, 0.0001) # 1.0000305180437934
solve(lambda x: [x**2-1, 2*x], -1, 0.0001) # -1
solve(lambda x: [exp(x)-1,exp(x)], 1, 0.0001) # 1.5641107898984284e-06
solve(lambda x: [sin(x), cos(x)], 0.5, 0.0001) # 3.311802132639069e-05