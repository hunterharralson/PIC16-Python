#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:32:46 2020

@author: hunterharralson

Homework 4
Hunter Harralson
304-781-158

"""

import re 
import urllib # problem 3

''' 
PROBLEM 1 -----------------------------------------------------------
'''

# performs the same action as type()
def mytype(v):
    data = str(v)
    
    # float 
    if re.search(r'-?\d+\.\d*', data) is not None:
        return "float"
    # int
    elif re.search(r'^-?\d+[^\.]?', data) is not None:
        return "int"
    # list 
    elif re.search(r'^\[(?:-?\d*,*\s*)*\]$', data) is not None:
        return "list"
    # string 
    else:
        return "string"

# Testing:
print("Problem 1:")
print(mytype(12))
print(mytype(-12.0))
print(mytype("this is a string"))
print(mytype(""))
print(mytype([1,2,3]))
print(mytype([]))
 

#%%
 
'''
PROBLEM 2 -----------------------------------------------------------
'''

# returns a list of the names of all PDF files without extensions
def findpdfs(L):
    #[A-z]*[0-9]*(?=.pdf)
    pdfs = [re.findall(r'[A-z]+[0-9]*(?=.pdf)', i) for i in L]
    pdfs = [pdf for pdf in pdfs if pdf]
    return(pdfs)


# Testing: 
L = ["IMG2309.jpg", "lecture1.pdf", "homework.py", "homework2.pdf"]
print("\nProblem 2:")
print(findpdfs(L))


#%%


'''
PROBLEM 3 -----------------------------------------------------------
'''

# takes as input a URL and outputs any email addresses on the webpage
def findemail(url):
    page = urllib.request.urlopen(url).read().decode()
    raws = re.findall(r'(([A-z]*[0-9]*)+(@|((\[|\s)at(\]|\s))|((\[|\s)AT(\]|\s)))([A-z]+((\.)|((\[|\s)dot(\]|\s))|((\[|\s)DOT(\]|\s)))[A-z]*)(\.[A-z]+)*)', page)
    
    emails = [] # list to store the emails 
    
    # capture the outermost group only 
    for group in raws:
        emails.append(group[0])
    
    emails2 = []
    # replace tricky emails with @ symbol
    for email in emails:
        email = re.sub('\[at\]|\[AT\]|\sat\s|\sAT\s','@',email)
        email = re.sub('\[dot\]|\[DOT\]|\sdot\s|\sDOT\s','.',email)
        emails2.append(email)
    
    return set(emails2)

    
# Testing: 
url1 = "https://www.math.ucla.edu/~hangjie/contact/"
url2 = "https://www.math.ucla.edu/~hangjie/teaching/Winter2019PIC16/regexTest"
    
print("\nProblem 3:")
print(findemail(url1))
print(findemail(url2))


#%%

'''
PROBLEM 4 -----------------------------------------------------------
'''
from happiness_dictionary import happiness_dictionary

def happiness(text):
    text = text.lower()
    text = re.sub('[\.\?!]', '', text) # remove special chars
    
    word_list = text.split() # period at end of sent. may be a liability
    words_compiled = [re.compile('^' + i + '$') for i in word_list] # compile my searches
    
    word_dict = {key:value for key,value in happiness_dictionary.items() if any (re.match(regex,key) for regex in words_compiled)}
    
    num_words = len(word_dict)
    happy_score = sum(word_dict.values())
    
    return happy_score/num_words

s1 = "Mary had a little lamb."
s2 = "Mary had a little lamb. Mary had a little lamb!"
s3 = "A quick brown fox jumps over a lazy dog."

print("\nProblem 4:")
print(happiness(s1))
print(happiness(s2))
print(happiness(s3))


#%%