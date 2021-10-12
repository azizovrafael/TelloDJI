# 1) pip3 install pygame - klavya inputlari oxumaq ucun
#
import pygame

def init():
 pygame.init()
 win = pygame.display.set_mode((400,400))

def get_key(name):
 ans = False
 for i in pygame.event.get(): pass
 keyInput = pygame.key.get_pressed()
 myKey = getattr(pygame, 'K_{}'.format(name))
 if keyInput[myKey]:
     ans = True
 pygame.display.update()

 return ans

# # virtualenv


#def sss():
#    pass
#
#
#if __name__ == "__main__":
#    sss()
