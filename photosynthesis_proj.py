import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 300))
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
            def draw(self, screen):
                pygame.draw.circle(self.c_surface, self.c_color, self.c_pos, self.c_radius, self.c_width)
                screen.draw.text("Carbon Dioxide                +", (self.c_pos[0], self.c_pos[1] + 20) )
            
        #oxygen1 = Circle("blue", (350,250), 15, 0)
        #oxygen2 = Circle("blue", (350,250), 15, 0)

    class Glucose:
        def __init__():
            pass
            
carbon = Photosynthesis("sunlight", "H2O", "yellow", (100,150), 20, 0)
oxygen1 = Photosynthesis("sunlight", "H2O", "blue", (85,165), 10, 0)
oxygen2 = Photosynthesis("sunlight", "H2O", "blue", (115, 165), 10, 0)

oxygen3 = Photosynthesis("sunlight", "H2O", "blue", (165, 150), 20, 0)
hydrogen1 = Photosynthesis("sunlight", "H2O", "grey", (150, 135), 10, 0)
hydrogen2 = Photosynthesis("sunlight", "H2O", "grey", (180, 135), 10, 0)

oxygen4 = Photosynthesis("sunlight", "H2O", "blue", (360, 150), 20, 0)
oxygen5 = Photosynthesis("sunlight", "H2O", "blue", (375, 130), 20, 0)

carbon_circle1 = carbon.carbon_dioxide.circle
carbon_circle1.draw(screen)

oxygen_circle1 = oxygen1.carbon_dioxide.circle
oxygen_circle1.draw(screen)

oxygen_circle2 = oxygen2.carbon_dioxide.circle
oxygen_circle2.draw(screen)

oxygen_circle3 = oxygen3.carbon_dioxide.circle
oxygen_circle3.draw(screen)

hydrogen_circle1 = hydrogen1.carbon_dioxide.circle
hydrogen_circle1.draw(screen)

hydrogen_circle2 = hydrogen2.carbon_dioxide.circle
hydrogen_circle2.draw(screen)

oxygen_circle4 = oxygen4.carbon_dioxide.circle
oxygen_circle4.draw(screen)

oxygen_circle5 = oxygen5.carbon_dioxide.circle
oxygen_circle5.draw(screen)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
