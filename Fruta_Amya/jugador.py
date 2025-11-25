import pygame

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 5

        try:
            imagen_original = pygame.image.load("assets/jugador/jugador.png")
            self.imagen = pygame.transform.scale(imagen_original, (60, 60))
        except:
            # Imagen alternativa
            self.imagen = pygame.Surface((60, 60))
            self.imagen.fill((0, 0, 255))

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    def obtener_pos(self):
        return self.x, self.y
