import sys
import random
from enum import Enum

class RPS(Enum): 
    ROCK = 1
    PAPER = 2 
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

print('')
player_choice = int(input('Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n'))

if player_choice < 1 or player_choice > 3: 
    sys.exit('you must enter 1, 2 or 3')

computer_choice = int(random.choice('123'))

print('')
print('You chose ' + str(RPS(player_choice)).replace("RPS.", '') + '.')# replace
print('python chose ' + str(RPS(computer_choice))[4:]+ '.') # slice
print('')

if player_choice == 1 and computer_choice == 3: 
    print('🎉You Win!')
elif player_choice == 2 and computer_choice == 1: 
    print('🎉You Win!')
elif player_choice == 3 and computer_choice == 2: 
    print('🎉You Win!')
elif player_choice == 1 and computer_choice == 2: 
    print('😭You Lose!')
elif player_choice == 2 and computer_choice == 3: 
    print('😭You Lose!')
elif player_choice == 3 and computer_choice == 1: 
    print('😭You Lose!')
else: 
    print('😳Tie!')