# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:04:21 2022

@author: HUGHJ095
"""
import random

choice = input("what do you choose? rock, paper, or scissors")
random = random.randint(1, 3)
error = False
if choice != "rock" and choice != "paper" and choice != "scissors":
    print("not a valid choice")
    error = True
if random == 1 and error == False:
    if choice == "rock":
        print("tie, rock")
    elif choice == "paper":
        print(f"you win, {choice} beats rock")
    else: print("you lose, rock beats scissors")
    
elif random == 2 and error == False:
    if choice == "paper":
        print("tie, paper")
    elif choice == "scissors":
        print("you win")
    else: print("you lose")

else:
    if error == False:
        if choice == "scissors":
            print("tie, scissors")
        elif choice == "rock":
            print("you win, rock beasts scissors")
        else: print("you lose, scissors beats paper")