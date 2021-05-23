import random
import sys
import pygame
import pygame.locals import *

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.pygame.display.set_mode((SCREENWIDTH),(SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {} 
GAME_SOUNDS = {}
PLAYER = '/gallery/sprites/bird.jpg'
BACKGROUND = '/gallery/sprites/5background.jpg'
PIPE = '/gallery/sprites/pipe.JPG'

if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy game by navneet')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('/gallery/sprites/0.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/1.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/2.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/3.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/4.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/5.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/6.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/7.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/8.jpg').convert_alpha(),
        pygame.image.load('/gallery/sprites/9.jpg').convert_alpha(),
    )

    GAME_SPRITES['base'] = pygame.image.load('/gallery/sprites/base.jpg').convert_alpha()   
    GAME_SPRITES['base'] = pygame.image.load('/gallery/sprites/pipe.jpg').convert_alpha()
    
    GAME_SPRITES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert.alpha(), 180),
    pygame.image.load(PIPE).convert.alpha()
    )