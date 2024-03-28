# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:42:14 2022

@author: HUGHJ095
"""

# who has more instagram followers among family
from game_data import data
import random
score = 0
go = 1
while go == 1:
    def format_data(account):
        account_name = account['name']
        account_prof = account['profession']
        account_home = account['hometown']
        return f"{account_name}, from {account_home}, is a {account_prof}"
    
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
    
    print('welcome to the guess how many followers game')
    print(f"Compare A: {format_data(account_a)}.")
    print('vs')
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type A or B").lower()
    
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    
    def check_answer(guess, a_follower_count, b_follower_count):
        if a_follower_count > b_follower_count:
            return guess == "a"
        else: 
            return guess == "b"
    
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    if is_correct:
        print("you're right")
        score = score + 1
    else:
        print("sorry that's wrong")
        score = 0
        go = 0
    print (score)    














