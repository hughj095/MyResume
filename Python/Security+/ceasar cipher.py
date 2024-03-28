# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 12:27:03 2022

@author: HUGHJ095
"""

# Ceasar Cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l'
            ,'m','n','o','p','q','r','s','t'
            ,'u','v','w','x','y','z']

direction = input("encode or decode")
text = input("type word to encode/decode").lower()
shift = int(input("type shift number"))
cipher = ""
def encrypt(text,shift):
    cipher = ""
    text = list(text)
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            position = position + shift
            if position > 26:
                position = position - 26
        else: 
            position = position - shift
            if position < 1:
                position = position + 26
        new_letter = alphabet[position]
        cipher += new_letter
    print(f"result is {cipher}")
encrypt(text,shift)

    

# else:
#     text = list(text)
#     for letter in text:
#         for i in alphabet:
#             if letter == i:
#                 letter = i-shift
# print(f"result is {text}")
    

