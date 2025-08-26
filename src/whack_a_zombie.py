import pygame

"""
Config setting to run
"""
class Config:
    def __init__(self, width, height):
        self.width = width
        self.height = height

"""
Execute the game
"""
class Whack_A_Zombie:
    def __init__(self, cfg):
        self.cfg = cfg
    def run(self):
        pygame.init()
        SURFACE = pygame.display.set_mode(self.cfg.width, self.cfg.heigth)