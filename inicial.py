import pygame,sys
from pygame.locals import*
from inimi import Alien
from baal import Bala
largura = 900
altura = 400
WHITE = (255, 255, 255)
pontos = 0
class naveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('image/aviaovermelho.png')
        
        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 60
        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20
        
        
    def movimentoDireita(self):
        self.rect.right += self.velocidade
        self.__moviment()
    
    def movimentoEsquerda(self):
        self.rect.left -= self.velocidade
        self.__moviment()
    
    def __moviment(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.left > 900:
                self.rect.left = 900
        
                
    def disparar(self,x,y):
        inimigo = Alien(y,x/4)
        minhaBala = Bala(x,y)
        self.listaDisparo.append(minhaBala)
    
    def colocar(self,superficie):
        superficie.blit(self.ImagemNave, self.rect)

def invasaoEspaco():
     pygame.init()
     tela = pygame.display.set_mode((largura,altura))
     pygame.display.set_caption("Invasão do Espaço")
     
     jogador = naveEspacial()
     ImagemFundo = pygame.image.load('image/thumb.jpg')
     jogando = True
     inimigo = Alien(altura,largura/4)
     balaproj = Bala(largura/2,altura-60)
     ponto = 0
     relogio = pygame.time.Clock()
     
     while True:
         relogio.tick(60)
         tempo = int(pygame.time.get_ticks()/1000)
         balaproj.trajetoria()
         inimigo.trajetoria()
         for evento in pygame.event.get():
             if evento.type == QUIT:
                 pygame.quit()
                 sys.exit()
             if evento.type == pygame.KEYDOWN:
                 if evento.key == K_LEFT:
                    jogador.movimentoEsquerda()
                    
                 elif evento.key == K_RIGHT:
                    jogador.movimentoDireita()
                    
                 elif evento.key == K_SPACE:
                     x,y = jogador.rect.center
                     jogador.disparar(x,y)
                     ponto += 2
                     inimigo.Tiro()
           
                     
         
         tela.blit(ImagemFundo,(0,0))
         #balaproj.colocar(tela)
         #Fundo scoreboard
         pygame.draw.rect(tela,WHITE,Rect([700,20],[190,40]),1)

         #Texto
         font = pygame.font.Font(None, 36)
         text = font.render("Pontos: " + str(ponto), 1, (200, 200, 200))
         textpos = text.get_rect()
         textpos.left = 705
         textpos.top = 30
         tela.blit(text, textpos)
         jogador.colocar(tela)
         inimigo.colocar(tela)
         inimigo.compartamento(tempo)
         if len(jogador.listaDisparo) > 0:
             for x in jogador.listaDisparo:
                 x.colocar(tela)
                 x.trajetoria()
                 if x.rect.top < -10:
                     jogador.listaDisparo.remove(x)
         pygame.display.update()
invasaoEspaco()