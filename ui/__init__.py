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
        self.current_page = None

        self.sidebox = SideBox(0,0,300,600)
        
        #buttons
        self.buttons = [
            Button('Bitcoin', 300, 100, (0,100)),
            Button('Ethereum', 300, 100, (0,220)),
            Button('Solana', 300, 100, (0,350)),
            Button('Dogecoin', 300, 100, (0,475))
        ]

    def check_click(self):
        for button in self.buttons:
            mouse_pos = pygame.mouse.get_pos()
            if button.top_rect.collidepoint(mouse_pos):
                button.top_color = (0,122,204)
                if pygame.mouse.get_pressed()[0]:
                    if button.text == 'Bitcoin':
                        self.set_page(0)
                    if button.text == 'Ethereum':
                        self.set_page(1)
                    if button.text == 'Solana':
                        self.set_page(2)
                    if button.text == 'Dogecoin':
                        self.set_page(3)
            else:
                button.top_color = (62, 62, 66)

    def set_page(self, index):
        self.current_page = self.pages[index]

    def run(self):
        while self.running:
            self.check_click()
            print(self.current_page)
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((30,30,30))
            self.sidebox.draw(self.screen)
            for button in self.buttons:
                button.draw(self.screen)

            if self.current_page == self.pages[0]:
                pass
            elif self.current_page == self.pages[1]:
                pass
            elif self.current_page == self.pages[2]:
                pass
            elif self.current_page == self.pages[3]:
                pass
            else:
                pass

            self.clock.tick(self.fps)
            pygame.display.update()