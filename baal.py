import pygame,sys


class Bala(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load('image/baladorado.png')
        
        self.rect = self.ImagemBala.get_rect()
        self.velocidadeBala = 10
        self.rect.top = posy
        self.rect.left = posx
        
    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala
        
    def colocar(self,superficie):
        superficie.blit(self.ImagemBala, self.rect)