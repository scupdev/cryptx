import pygame, sys
from pygame.locals import *
from .sidebox import SideBox
from .button import Button

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
        self.pages = ["BITCOIN", "ETHEREUM", "SOLANA", "DOGECOIN"]
        self.current_page = self.pages[0]

        self.sidebox = SideBox(0,0,300,600)
        
        #buttons
        self.button_1 = Button('Bitcoin', 300, 100, (0,100))
        self.button_2 = Button('Ethereum', 300, 100, (0,220))
        self.button_3 = Button('Solana', 300, 100, (0,350))
        self.button_4 = Button('Dogecoin', 300, 100, (0,475))

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((30,30,30))
            self.sidebox.draw(self.screen)
            self.button_1.draw(self.screen)
            self.button_2.draw(self.screen)
            self.button_3.draw(self.screen)
            self.button_4.draw(self.screen)

            if self.current_page == self.pages[0]:
                pass
            elif self.current_page == self.pages[1]:
                pass
            elif self.current_page == self.pages[2]:
                pass
            elif self.current_page == self.page[3]:
                pass
            else:
                pass

            self.clock.tick(self.fps)
            pygame.display.update()