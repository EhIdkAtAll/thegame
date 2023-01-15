import pygame



class Menu():

    def __init__(self):
        pass










pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

# screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption('The game')


# Create The Backgound
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((000, 000, 000)) 

sound = pygame.mixer.Sound('music.mp3')
sound.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()