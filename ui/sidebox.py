import pygame

class SideBox:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y 
        self.h = h
        self.w = w
        self.color = (45, 45, 48)
        self.rect = (x,y,w,h)
        self.font = pygame.font.SysFont('Nunito', 25)
        self.text = self.font.render("Cryptx : Today", True, (0, 122, 204))

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect,0,0,0,20,0,20)
        win.blit(self.text, (50,20))