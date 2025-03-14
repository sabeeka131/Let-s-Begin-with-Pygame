import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My first game screen')

background_color = (58, 58, 58)

background_image = pygame.transform.scale(
    pygame.image.load('bg.jpg').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)
cactus_image = pygame.transform.scale(
    pygame.image.load('c..png').convert_alpha(),
    (300, 300)
)
cactus_rect = cactus_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill(background_color)
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(cactus_image, cactus_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()