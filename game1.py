#!usr/bin/env python3
#https://www.youtube.com/watch?v=iLL2V1es52I&index=2&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

import pygame
from gameDictionary import dict
from boardgame import move
pygame.init() #got to have. initializes

#Red, green, blue
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((800,600)) #canvas, dimensions: parameter must be tuple, i.e. be in parens, i guess
pygame.display.set_caption('LanguageRace')
pygame.display.update()

#_____________MainLoop_____________
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#'no parens cause this is an object'. ok, then what is it W/ parens?
            gameExit = True # =/= game loss

    #fill is applied to surface object
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400,300,10,10])#location, color, coordinates(top left, width, height)
    gameDisplay.fill(red,rect = [200,200,50,50])
#0,0 is from the top left corner. so it's 100 pixels down


    pygame.display.update()

    a = move(0,1)
    print (a)




pygame.quit() #unitializess
quit() #exits python

#learn ganon, falco, falcon? 
#jenny jaffe, 555
#erin, tweet AFE
#practice 2v1
#it's like...my childhood imagination had a purity that mine doesn't now. now mine feels restricted by guilt over what I've done, WHICH ISN'T EVEN BAD

#https://www.youtube.com/watch?v=pp2opCTPa0k&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=7
