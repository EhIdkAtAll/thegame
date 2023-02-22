import pygame, json

def main():

    with open("config.json", "r") as f:
        config = json.load(f)

    #Music
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()

    x_screen_size = pygame.display.Info().current_w
    y_screen_size = pygame.display.Info().current_h

    screen = pygame.display.set_mode((x_screen_size, y_screen_size))
    display = pygame.display.set_mode((380,220))
    pygame.display.set_caption('The game')

    sound = pygame.mixer.Sound('assets/music.mp3')
    sound.play(-1)

    clock = pygame.time.Clock()

    #Launch the Main Menu
    while True:
        sound.set_volume(config["soundlevel"]/100)

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(70)


main()
