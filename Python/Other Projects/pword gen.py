# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 12:28:55 2022

@author: HUGHJ095
"""
import random
#password generator
numltr = input("how many letters in your pword")
numnum = input("how many numbers in your pword")
numsym = input("how many symbols in your pword")
total=int(numltr)+int(numnum)+int(numsym)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 's', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','%','^','&','*','(',')']

randlet = random.randint(0,25)
randlet = letters[randlet]

randnum = random.randint(1,10)
randnum = numbers[randnum]

randsym = random.randint(0,8)
randsym = symbols[randsym]
pword = ""
for i in range(1,total):
    randlet = random.randint(0,25)
    randlet = letters[randlet]
    randnum = random.randint(0,9)
    randnum = numbers[randnum]
    randsym = random.randint(0,8)
    randsym = symbols[randsym]
    randord = random.randint(1,3)
    if randord == 1:
        pword = pword+randlet
    if randord == 2:
        pword = pword+str(randnum)
    if randord == 3:
        pword = pword+randsym
print(pword)