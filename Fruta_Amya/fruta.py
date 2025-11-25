import pygame
import random

class Fruta:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.color = (255, 0, 0)

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x, self.y), 20)


