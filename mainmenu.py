import pygame
from utilities import Button

def main():

    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()

    x_screen_size = pygame.display.Info().current_w
    y_screen_size = pygame.display.Info().current_h
    
    screen = pygame.display.set_mode((x_screen_size, y_screen_size))
    #screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('The game')

    sound = pygame.mixer.Sound('assets/music.mp3')
    sound.play(-1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0)) 

    img = pygame.image.load("assets/game_icon.png").convert_alpha()
    icon = Button(x_screen_size * 0.5, y_screen_size * 0.2, img, y_screen_size / 500 )

    img = pygame.image.load("assets/play_button.png").convert_alpha()
    playb = Button(x_screen_size * 0.5, y_screen_size * 0.4, img, y_screen_size / 500 )

    img = pygame.image.load("assets/settings_button.png").convert_alpha()
    settingsb = Button(x_screen_size * 0.5, y_screen_size * 0.6, img, y_screen_size / 500 )

    img = pygame.image.load("assets/exit_button.png").convert_alpha()
    exitb = Button(x_screen_size * 0.5, y_screen_size * 0.8, img, y_screen_size / 500 )

    
    while True:

        icon.draw(screen)

        if playb.draw(screen):
            print("START")
        
        if settingsb.draw(screen):
            print("SETTINGS")
        
        if exitb.draw(screen):
            pygame.quit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        pygame.display.update()


main()