import pygame, sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (139, 69, 19)

screen = pygame.display.set_mode((800, 300))
pygame.display.set_caption("photosynthesis")
screen.fill("white")
font = pygame.font.Font(None, 30)

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
            
            def text(self, txt, x ,y):
                text_surface = font.render(txt, True, (0, 0, 0))  
                text_rect = text_surface.get_rect(center=(x,y))  # Positioning
                self.c_surface.blit(text_surface, text_rect)
            
        #oxygen1 = Circle("blue", (350,250), 15, 0)
        #oxygen2 = Circle("blue", (350,250), 15, 0)

    class Glucose:
        def __init__():
            pass

    class GlucoseDiagram:
        def __init__(self, surface, position):
            self.surface = surface
            self.position = position  # center x, y
            self.atoms = []

            # Rough visual layout (simplified hexagon ring of glucose)
            offset_x, offset_y = self.position
            r = 15  #radius
            self.atoms = [
                {"element": "C", "pos": (offset_x, offset_y), "color": BROWN},
                {"element": "C", "pos": (offset_x + 40, offset_y - 30), "color": BROWN},
                {"element": "C", "pos": (offset_x + 80, offset_y), "color": BROWN},
                {"element": "C", "pos": (offset_x + 80, offset_y + 40), "color": BROWN},
                {"element": "C", "pos": (offset_x + 40, offset_y + 70), "color": BROWN},
                {"element": "C", "pos": (offset_x, offset_y + 40), "color": BROWN},
                {"element": "O", "pos": (offset_x - 30, offset_y + 20), "color": BLUE},
                {"element": "H", "pos": (offset_x + 20, offset_y - 50), "color": GRAY},
                {"element": "H", "pos": (offset_x + 100, offset_y - 10), "color": GRAY},
                {"element": "H", "pos": (offset_x + 100, offset_y + 50), "color": GRAY},
                {"element": "H", "pos": (offset_x + 20, offset_y + 90), "color": GRAY},
                {"element": "H", "pos": (offset_x - 20, offset_y + 70), "color": GRAY},
            ]

            self.radius = r

        def draw(self):
            for atom in self.atoms:
                pygame.draw.circle(self.surface, atom["color"], atom["pos"], self.radius)
                label = font.render(atom["element"], True, BLACK)
                text_rect = label.get_rect(center=atom["pos"])
                self.surface.blit(label, text_rect)

           
carbon = Photosynthesis("sunlight", "H2O", "yellow", (100,150), 20, 0)
oxygen1 = Photosynthesis("sunlight", "H2O", "blue", (85,165), 10, 0)
oxygen2 = Photosynthesis("sunlight", "H2O", "blue", (115, 165), 10, 0)

oxygen3 = Photosynthesis("sunlight", "H2O", "blue", (215, 150), 20, 0)
hydrogen1 = Photosynthesis("sunlight", "H2O", "grey", (200, 135), 10, 0)
hydrogen2 = Photosynthesis("sunlight", "H2O", "grey", (230, 135), 10, 0)

oxygen4 = Photosynthesis("sunlight", "H2O", "blue", (430, 150), 20, 0)
oxygen5 = Photosynthesis("sunlight", "H2O", "blue", (425, 130), 20, 0)

carbon_circle1 = carbon.carbon_dioxide.circle
carbon_circle1.draw(screen)
carbon_circle1.text("Carbon Dioxide", carbon_circle1.c_pos[0] - 15, carbon_circle1.c_pos[1] + 50)

oxygen_circle1 = oxygen1.carbon_dioxide.circle
oxygen_circle1.draw(screen)

oxygen_circle2 = oxygen2.carbon_dioxide.circle
oxygen_circle2.draw(screen)

oxygen_circle3 = oxygen3.carbon_dioxide.circle
oxygen_circle3.draw(screen)
oxygen_circle3.text("Water", oxygen_circle3.c_pos[0], oxygen_circle3.c_pos[1] + 50)

hydrogen_circle1 = hydrogen1.carbon_dioxide.circle
hydrogen_circle1.draw(screen)

hydrogen_circle2 = hydrogen2.carbon_dioxide.circle
hydrogen_circle2.draw(screen)

oxygen_circle4 = oxygen4.carbon_dioxide.circle
oxygen_circle4.draw(screen)
oxygen_circle4.text("Oxygen", oxygen_circle4.c_pos[0], oxygen_circle4.c_pos[1] + 50)

oxygen_circle5 = oxygen5.carbon_dioxide.circle
oxygen_circle5.draw(screen)

glucose_diagram = Photosynthesis.GlucoseDiagram(screen, (600, 150))
glucose_diagram.draw()
font3 = pygame.font.SysFont("callibri", 25)
text3 = font3.render("Glucose", True, "black")
screen.blit(text3, (600, 260))

font4 = pygame.font.SysFont("callibri", 50)
text4 = font4.render("+", True, "black")
screen.blit(text4, (150, 135))

font5 = pygame.font.SysFont("callibri", 50)
text5 = font5.render("-->", True, "black")
screen.blit(text5, (300, 135))

font6 = pygame.font.SysFont("callibri", 50)
text6 = font6.render("+", True, "black")
screen.blit(text6, (500, 135))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
