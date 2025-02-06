import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("photosynthesis")
screen.fill("white")

class Photosynthesis:
    def __init__(self, sunlight, water, color, pos, radius, width):
        self.sunlight = sunlight
        self.carbon_dioxide = self.Carbon_Dioxide(color, pos, radius, width)
        self.water = water
    def process(self):
        if self.sunlight > 0 and self.carbon_dioxide > 0 and self.water > 0:
            glucose = self.carbon_dioxide + self.water
            oxygen = self.carbon_dioxide // 2
            return glucose, oxygen
        else: 
            return "not enough resources for photosynthesis" 
        
    class Carbon_Dioxide:
        def __init__(self, color, pos, radius, width):
            self.oxygen1 = "oxygen1"
            self.oxygen2 = "oxygen2"
            self.carbon = "carbon"
            self.circle = self.Circle(color, pos, radius, width)
        
        class Circle:
            def __init__(self, color, pos, radius, width):
                self.c_color = color
                self.c_pos = pos
                self.c_radius = radius
                self.c_width = width
                self.c_surface = screen
            def draw(self):
                pygame.draw.circle(self.c_surface, self.c_color, self.c_pos, self.c_radius, self.c_width)
            
        #oxygen1 = Circle("blue", (350,250), 15, 0)
        #oxygen2 = Circle("blue", (350,250), 15, 0)
            
carbon = Photosynthesis("sunlight", "H2O", "yellow", (300,300), 20, 0)

carbon_circle1 = carbon.carbon_dioxide.circle
carbon_circle1.draw()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()