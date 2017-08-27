#!usr/bin/env python3

import random

dict = {}
dict['1'] = 'Have another go!'
dict['2'] = 'Go forward two spaces!' 
dict['3'] = 'Miss a turn!'
dict['4'] = 'Go back three spaces!'
dict['5'] = 'I would rather have _____ hair than _____ hair. (Choose between redand green)'
dict['6'] = 'Describe your best friend!'
dict['7'] = 'what superpower do you want? why?'
dict['8'] = 'would you rather have a cat or a dog?'
dict['9'] = 'Have another go!'
dict['10'] = 'would you rather have a dragon or a unicorn?'
dict['11'] = 'describe the plot of your favorite movie'
dict['12'] = 'Miss a turn!'
dict['13'] = 'I like _______ less than _______. (Choose between cake and ice cream)'
dict['14'] = 'I would rather go to _______ than _______. (Choose between Disneyland, Harry Potter World)'
dict['15'] = 'where do you want to go on vacation? why?'
dict['16'] = 'what do you like about Santiago?'
dict['17'] = 'I like _____ more than ______. (Choose between pizza and sushi)'
dict['18'] = 'Describe your pet'
dict['19'] = 'Tell me three of your favorite things!'
dict['20'] = 'what do you discuss in your favorite class?'
dict['21'] = 'Tell me three of your least favorite things!'
dict['22'] = 'Roll again!'

player1 = 0
player2 = 0
while player1 < 22 and player2 < 22:
    inp = (input('Player 1, ready to roll? (hit any key  when ready): ')
    dice = random.randint(1,7)
    print ('Player 1, roll:\nYou rolled the dice and got a ' + str(dice) + '.')
    player1 += dice
    print (dict[player1])
    inp = (input('Player 2, ready to roll? (hit any key  when ready): ')
    
#___player 2 rolls___
    dice2 = random.randint(1,7)
           print ('Player 2, roll:\nYou rolled the dice and got a ' + str(dice2) + '.')
    player2 += dice2
    print (dict[player2])
    inp = (input('Player 1, ready to roll? (hit any key  when ready): ')

    


#print ('\n\n\n\n\n\n\n\n' + dict['5'] + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
