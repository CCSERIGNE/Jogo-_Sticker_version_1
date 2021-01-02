import pygame ,sys

class Alien(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.Imagem1 = pygame.image.load('image/alien1.png')
        self.Imagem2 = pygame.image.load('image/alien2.png')
        self.Imagem3 = pygame.image.load('image/alien3.png')
        self.Imagem4 = pygame.image.load('image/alien4.png')
        self.Imagem5 = pygame.image.load('image/alien5.png')
        
        self.listaImagens = [self.Imagem1,self.Imagem2,self.Imagem3,self.Imagem4,self.Imagem5]
        self.posImagem = 0
        self.ImagemAlien = self.listaImagens[self.posImagem]
        
        self.rect = self.ImagemAlien.get_rect()
        self.listaDisparo = []
        self.velocidade = 2
        self.rect.top = posy
        self.rect.left = posx
        self.rect.right = posx
        
        self.top = self.rect.top
        self.left = self.rect.left
        self.right = self.rect.right
        self.configTempo = 1
        self.crash_sound = pygame.mixer.Sound('son/Tiros.wav')
        
    def Tiro(self):
        self.crash_sound.play()
        
    def trajetoria(self):
        print(self.posImagem)
        if self.rect.top <= 1: 
           self.rect.top =  self.top
           self.rect.left = self.left
           self.rect.right = self.right
        elif self.posImagem == 0:
            self.rect.top = self.rect.top-5
            self.rect.right = self.rect.right+5
        elif self.posImagem == 1:
            self.rect.top = self.rect.top-5
            self.rect.right = self.rect.right-5
        elif self.posImagem == 2:
            self.rect.top = self.rect.top-5
            self.rect.left = self.rect.left+5
        elif self.posImagem == 3:
            self.rect.top = self.rect.top-5
            self.rect.left = self.rect.left-5
        elif self.posImagem == 4:
            self.rect.top = self.rect.top-5
            self.rect.left = self.rect.left-5
            self.rect.right = self.rect.right+5
            
        
    def compartamento(self,tempo):
        if self.configTempo == tempo:
            self.posImagem += 1
            self.configTempo += 1
            if self.posImagem > len(self.listaImagens)-1:
                self.posImagem = 0
        
    def colocar(self,superficie):
        self.ImagemAlien = self.listaImagens[self.posImagem]
        superficie.blit(self.ImagemAlien, self.rect)
