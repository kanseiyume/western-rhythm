import pygame
from pygame.locals import *
import random
import time
import sys
import os
import math

pygame.init()

# Define colors
colors = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "green": (0, 255, 0),
    "teal": (0, 128, 128),
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "gray": (128, 128, 128)

}

# Western Rhythm - man gets isekai'd into a desert world with gambling everywhere taking the forms of rhythm game battles

class Game:
    def __init__(self):
        # Set up the screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Western Rhythm")
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.SysFont("Arial", 20)
        self.font_large = pygame.font.SysFont("Arial", 30)
        self.font_huge = pygame.font.SysFont("Arial", 50)
    
    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(self.fps)
            self.events()
            self.update()
            self.draw()