import pygame
from station import Station
from link import Link

WIDTH = 800
HEIGHT = 800

# CONSTRUYENDO LOS OBJETOS
estaciones = {} 

estaciones['Zona Universitaria'] = Station(100, 400, (71, 105, 48))
estaciones['Palau Reial'] = Station(700, 400, (71, 105, 48))
estaciones['Maria Cristina'] = Station(200, 300, (71, 105, 48))

links = [Link(estaciones['Palau Reial'], estaciones['Maria Cristina']),Link(estaciones['Zona Universitaria'], estaciones['Palau Reial']), ]

# INICIALIZACIÓN DEL PYGAME
pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))

is_running = True


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    for i in estaciones:
        pygame.draw.circle(window_surface, estaciones[i].color, (estaciones[i].X, estaciones[i].Y), 30) 
    
    for j in links:
        j.drawLink(window_surface)

    links[0].setTrainFirst(window_surface)
    links[0].stepToSecond(window_surface)
    
    
    pygame.time.wait(100)

    background.fill(pygame.Color('#000000'))
    pygame.display.update()