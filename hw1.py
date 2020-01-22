# Hunter Harralson
# 304-781-158
# Homework 1

# Problem 1
def largerIndex(c):
    '''
    INPUT: list c
    OUTPUT: list k 
    '''
    
    index = 0 
    k = [0]*(len(c))
    
    for i in c:
        if i > index:
            k[index] = 1
        elif i == index:
            k[index] = 0
        elif i < index:
            k[index] = -1
        index = index + 1
    return k
            
# Test the function:
l1 = [1,2,0,4,2,1,40,-5]
l2 = [0,3,2,1,32,3,4,0]
print("List 1: ", largerIndex(l1))
print("List 2: ", largerIndex(l2))

# ----------------------------------------------------------------------------

# Problem 2 
def squareUpTo(n):
    '''
    INPUT: int n - the largest number to be squared
    OUTPUT: list squares - the values less than or equal to n, squared 
    '''
    
    squares = []
    squares = [i*i for i in range(n) if i*i <= n]
    return squares

# Test the function:
print(squareUpTo(10))
print(squareUpTo(100))


# ----------------------------------------------------------------------------


# Problem 3
import random as rand

'''
Function fliplin3 uses fair coins to generate a biased coin
with success probability of 1/3
'''
def flip1in3():
    '''
    Output - true 1/3 of the time or false 2/3 of the time
    '''
    coin1 = rand.randint(0,1)
    coin2 = rand.randint(0,1)
    
    # if both heads, reflip
    if coin1 == 1 and coin2 == 1:
        return flip1in3()
    # if both tails, return true (1/3)
    elif coin1 == 0 and coin2 == 0: 
        return True
    # if one heads and one tail, return false (2/3)
    else: 
        return False

    
print(flip1in3())

# Testing the function:     
true_count = 0
false_count = 0

for i in range(0,101):
    if flip1in3() == True:
        true_count = true_count + 1
    else:
        false_count = false_count + 1

print("True: ", true_count)
print("False: ", false_count)


# ----------------------------------------------------------------------------


# Problem 4
def duplicates(c): 
    '''
    INPUT - list c containing integers
    OUTPUT - list k containing the duplicate values of list c
    '''
    k = []
    [k.append(i) for i in c if c.count(i)>1 and i not in k]
    
    return k

# Test the function:
l3 = [1,2,5,3,6,2,4,5]
duplicates(l3)

l4 = [1,3,5,5,1,4,3]
duplicates(l4)
