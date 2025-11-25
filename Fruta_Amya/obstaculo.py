import pygame
import random
import math

class Obstaculo:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.velocidad = 2

        try:
            img = pygame.image.load("assets/obstaculos/obstaculo.png")
            self.imagen = pygame.transform.scale(img, (70, 70))
        except:
            self.imagen = pygame.Surface((70, 70))
            self.imagen.fill((200, 120, 50))

    def seguir_jugador(self, jugador_x, jugador_y):
        dx = jugador_x - self.x
        dy = jugador_y - self.y
        distancia = math.hypot(dx, dy)

        if distancia != 0:
            dx /= distancia
            dy /= distancia

        self.x += dx * self.velocidad
        self.y += dy * self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))
