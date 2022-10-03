import pygame

class Link:
    def __init__(self, firstStation, secondStation) -> None:
        self.firstStation = firstStation 
        self.secondStation = secondStation

    def drawLink(self, window_surface):
        pygame.draw.line(window_surface, (71, 105, 48), (self.firstStation.X, self.firstStation.Y), (self.secondStation.X, self.secondStation.Y), 5)