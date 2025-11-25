import pygame
import sys

class Menu:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fuente_titulo = pygame.font.Font(None, 80)
        self.fuente_boton = pygame.font.Font(None, 50)
        self.fuente_pequeña = pygame.font.Font(None, 30)
        
        self.color_fondo = (34, 139, 34)  # Verde oscuro
        self.color_titulo = (255, 255, 100)  # Amarillo
        self.color_boton = (50, 205, 50)  # Verde lima
        self.color_boton_hover = (144, 238, 144)  # Verde claro
        self.color_texto = (255, 255, 255)  # Blanco
       
        self.boton_jugar = pygame.Rect(250, 200, 300, 70)
        self.boton_records = pygame.Rect(250, 290, 300, 70)
        self.boton_controles = pygame.Rect(250, 380, 300, 70)
        self.boton_salir = pygame.Rect(250, 470, 300, 70)
        
        self.botones = [
            (self.boton_jugar, "JUGAR"),
            (self.boton_records, "RECORDS"),
            (self.boton_controles, "CONTROLES"),
            (self.boton_salir, "SALIR")
        ]
        
        self.opcion_seleccionada = None
    
    def dibujar_boton(self, boton, texto, mouse_pos):
        """Dibuja un botón con efecto hover"""
   
        hover = boton.collidepoint(mouse_pos)
        
        
        color = self.color_boton_hover if hover else self.color_boton
        
        if hover:
            boton_expandido = boton.inflate(10, 10)
            pygame.draw.rect(self.pantalla, color, boton_expandido, border_radius=15)
            pygame.draw.rect(self.pantalla, self.color_texto, boton_expandido, 4, border_radius=15)
        else:
            pygame.draw.rect(self.pantalla, color, boton, border_radius=15)
            pygame.draw.rect(self.pantalla, self.color_texto, boton, 3, border_radius=15)
        
      
        texto_surface = self.fuente_boton.render(texto, True, self.color_texto if not hover else (0, 0, 0))
        texto_rect = texto_surface.get_rect(center=boton.center)
        self.pantalla.blit(texto_surface, texto_rect)
        
        return hover
    
    def mostrar(self):
        """Muestra el menú principal y maneja la interacción"""
        reloj = pygame.time.Clock()
        
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
          
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton_jugar.collidepoint(mouse_pos):
                        return "jugar"
                    elif self.boton_records.collidepoint(mouse_pos):
                        return "records"
                    elif self.boton_controles.collidepoint(mouse_pos):
                        return "controles"
                    elif self.boton_salir.collidepoint(mouse_pos):
                        return "salir"
            
            
            self.pantalla.fill(self.color_fondo)
            
            
            titulo = self.fuente_titulo.render("FRUTA MANIA", True, self.color_titulo)
            titulo_rect = titulo.get_rect(center=(400, 100))
            self.pantalla.blit(titulo, titulo_rect)
            
            
            subtitulo = self.fuente_pequeña.render("¡Recolecta frutas y evita obstáculos!", True, self.color_texto)
            subtitulo_rect = subtitulo.get_rect(center=(400, 150))
            self.pantalla.blit(subtitulo, subtitulo_rect)
            
            
            for boton, texto in self.botones:
                self.dibujar_boton(boton, texto, mouse_pos)
            
            
            version = self.fuente_pequeña.render("v2.0", True, (200, 200, 200))
            self.pantalla.blit(version, (10, 570))
            
            pygame.display.update()
            reloj.tick(30)
    
    def mostrar_controles(self):
        """Muestra la pantalla de controles"""
        reloj = pygame.time.Clock()
        boton_volver = pygame.Rect(300, 500, 200, 60)
        
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    return "menu"
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.collidepoint(mouse_pos):
                        return "menu"
            
            
            self.pantalla.fill(self.color_fondo)
            
            
            titulo = self.fuente_titulo.render("CONTROLES", True, self.color_titulo)
            titulo_rect = titulo.get_rect(center=(400, 80))
            self.pantalla.blit(titulo, titulo_rect)
            
           
            controles = [
                "MOVIMIENTO:",
                "  ↑ ↓ ← →  o  W A S D",
                "",
                "PAUSAR:",
                "  ESC",
                "",
                "POWER-UPS:",
                "  ⚡ Velocidad - Muévete más rápido",
                "  🛡️ Escudo - Protección temporal",
                "  ⏰ Tiempo Lento - Ralentiza enemigos",
                "  💎 Fruta Dorada - +5 puntos",
                "  💣 Bomba - Destruye obstáculos"
            ]
            
            y = 180
            for linea in controles:
                if linea.startswith(" "):
                    texto = self.fuente_pequeña.render(linea, True, (200, 200, 200))
                else:
                    texto = self.fuente_boton.render(linea, True, self.color_texto)
                texto_rect = texto.get_rect(center=(400, y))
                self.pantalla.blit(texto, texto_rect)
                y += 35 if linea else 20
            
          
            self.dibujar_boton(boton_volver, "VOLVER", mouse_pos)
            
            pygame.display.update()
            reloj.tick(30)
    
    def mostrar_records(self):
        """Muestra la tabla de récords"""
        reloj = pygame.time.Clock()
        boton_volver = pygame.Rect(300, 500, 200, 60)
        
        try:
            with open("records.txt", "r") as archivo:
                lineas = archivo.readlines()
                records = []
                for linea in lineas[:5]:  
                    records.append(linea.strip())
        except:
            records = ["No hay récords todavía", "", "¡Sé el primero en jugar!"]
        
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return "salir"
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    return "menu"
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.collidepoint(mouse_pos):
                        return "menu"
            
            self.pantalla.fill(self.color_fondo)
            
          
            titulo = self.fuente_titulo.render("RECORDS", True, self.color_titulo)
            titulo_rect = titulo.get_rect(center=(400, 80))
            self.pantalla.blit(titulo, titulo_rect)
            
            subtitulo = self.fuente_pequeña.render("Top 5 Mejores Puntajes", True, self.color_texto)
            subtitulo_rect = subtitulo.get_rect(center=(400, 140))
            self.pantalla.blit(subtitulo, subtitulo_rect)
            
            y = 200
            for i, record in enumerate(records):
                if record:
                    texto = self.fuente_boton.render(f"{i+1}. {record}", True, self.color_texto)
                    texto_rect = texto.get_rect(center=(400, y))
                    self.pantalla.blit(texto, texto_rect)
                    y += 60
            
            self.dibujar_boton(boton_volver, "VOLVER", mouse_pos)
            
            pygame.display.update()
            reloj.tick(30)
