import pygame
from juego import Juego
from menu import Menu

def main():
    pygame.init()
    
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fruta Manía")

    menu = Menu(pantalla)
    ejecutando = True

    while ejecutando:
        opcion = menu.mostrar()

        if opcion == "jugar":
            juego = Juego(pantalla)   # IMPORTANTE: pasar pantalla
            resultado = juego.iniciar()  # Puede devolver "menu" si lo deseas

        elif opcion == "records":
            menu.mostrar_records()

        elif opcion == "controles":
            menu.mostrar_controles()

        elif opcion == "salir":
            ejecutando = False

    pygame.quit()


if __name__ == "__main__":
    main()
