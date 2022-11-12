import pygame, sys
from pygame.locals import *
from .sidebox import SideBox

class UserInterface:
    def __init__(self, w: int, h: int):
        pygame.init()
        self.w = w
        self.h = h
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("CryptX: Crypto prices for the nerds!")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 120

        self.sidebox = SideBox(0,0,300,600)

    def run(self):
        while self.running:
            self.screen.fill((30,30,30))
            self.sidebox.draw(self.screen)
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.clock.tick(self.fps)
            pygame.display.update()