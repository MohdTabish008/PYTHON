#!/usr/bin/env python
import random
def get_guess():
    return list(input('Enter 3 Digit Code'))
#Generate Random Code
def code_generator():
    digits = [str(num) for num in range(10)]
    #shuffling the digits
    random.shuffle(digits)
    #grab first three digits
    return digits[:3]

#Generate The Clues
def generate_clues(code,user_guess):
    if user_guess == code:
        return 'Attaboy! Code Cracked'
    clues = []    
    for index,num in enumerate(user_guess):
        if num == code[index]:
            clues.append('Match')
        elif (num in code):
            clues.append('Close')
    if clues == []:
        return ['Try Hard']
    else:
        return clues
            
#Run Game Logic
print('Welcome Spy,Guess the Code')
secret_code = code_generator()
clue_report = []
while clue_report != 'Attaboy! Code Cracked':
    guess = get_guess()
    clue_report = generate_clues(secret_code,guess)
    print('result of 1st num  ,  result of 2nd num  , result of 3rd num')
    print(*clue_report)
    

