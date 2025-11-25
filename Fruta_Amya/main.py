import pygame
from juego import Juego
from menu import Menu

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fruta Manía ")
    
    menu = Menu(pantalla)
    
    while True:
        opcion = menu.mostrar()
        
        if opcion == "jugar":
            juego = Juego()
            juego.iniciar()
        
        elif opcion == "records":
            resultado = menu.mostrar_records()
            if resultado == "salir":
                break
        
        elif opcion == "controles":
            resultado = menu.mostrar_controles()
            if resultado == "salir":
                break
        
        elif opcion == "salir":
            break
    
    pygame.quit()
