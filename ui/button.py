import pygame

class Button:
    def __init__(self, text, w, h, pos, top_color=(62, 62, 66)):
        self.text = text
        self.top_rect = pygame.Rect(pos,(w,h)) 
        self.top_color = top_color
        self.font = pygame.font.SysFont('Nunito', 20)
        self.text_surf = self.font.render(text,True,(255,255,255))
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        self.bitcoin = pygame.transform.scale(pygame.image.load('/home/chanlan/dev/py/cryptx/res/bitcoin.png'), (50, 50))
        self.ethereum = pygame.transform.scale(pygame.image.load('/home/chanlan/dev/py/cryptx/res/ethereum.png'), (50, 50))
        self.solana = pygame.transform.scale(pygame.image.load('/home/chanlan/dev/py/cryptx/res/solana.png'), (50, 50))
        self.dogecoin = pygame.transform.scale(pygame.image.load('/home/chanlan/dev/py/cryptx/res/dogecoin.png'), (50, 50))

    def draw(self, win):
        pygame.draw.rect(win, self.top_color, self.top_rect)
        win.blit(self.bitcoin, (10, 125))
        win.blit(self.ethereum, (10, 250))
        win.blit(self.solana, (10, 375))
        win.blit(self.dogecoin, (10, 500))
        win.blit(self.text_surf, self.text_rect)
