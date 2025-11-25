import pygame
import random

class Fruta:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)

        try:
            img = pygame.image.load("assets/frutas/fruta.png")
            self.imagen = pygame.transform.scale(img, (40, 40))
        except:
            self.imagen = pygame.Surface((40, 40))
            self.imagen.fill((255, 0, 0))

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def obtener_pos(self):
        return self.x, self.y
