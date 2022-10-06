import pygame

class Link:
    def __init__(self, firstStation, secondStation, trainX=0, trainY=0) -> None:
        self.firstStation = firstStation 
        self.secondStation = secondStation
        self.trainX = trainX
        self.trainY = trainY

    def drawLink(self, window_surface):
        pygame.draw.line(window_surface, (71, 105, 48), (self.firstStation.X, self.firstStation.Y), (self.secondStation.X, self.secondStation.Y), 5)

    def setTrainFirst(self, window_surface):
        pygame.draw.circle(window_surface, (196, 255, 249), (self.firstStation.X, self.firstStation.Y), 10)
        trainX = self.firstStation.X
        trainY = self.firstStation.Y

    def setTrainSecond(self, window_surface):
        pygame.draw.circle(window_surface, (196, 255, 249), (self.secondStation.X , self.secondStation.Y), 10)
        trainX = self.secondStation.X
        trainY = self.secondStation.Y

    def stepToSecond(self, window_surface):
        self.trainX = self.trainX + ((self.secondStation.X - self.firstStation.X)/50)
        self.trainY = self.trainY + ((self.secondStation.Y - self.secondStation.Y)/50)
        pygame.draw.circle(window_surface, (196, 255, 249), (self.trainX, self.trainY), 10)