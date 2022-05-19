import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"

class Snow(pygame.sprite.Sprite):
    def __init__(self, width: int):
        super().__init__()
        """
        :param width: width of snow in px
        """
        self.image = pygame.Surface([width, width])
        # fill that image with an actual shape
        pygame.draw.circle(
            self.image,
            WHITE,
            (width // 2, width // 2),  # draw in the middle
            width // 2
        )
        self.image.set_colorkey(BLACK)      # makes the black background of each snow sprite transparent

        self.rect = self.image.get_rect()

        self.yvel = 3

    def update(self):
        """Change the y-coord by yvel"""
        self.rect.y += self.yvel

        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH)
            self.rect.y = random.randrange(-50, -10)

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    num_snow = 100

    # Create a snow sprites group
    snow_sprites = pygame.sprite.Group()

    # Create num_snow snowflakes
    for i in range(num_snow):
        snow = Snow(10)

        # Decide randomly where to place snow
        snow.rect.center = random_coords()

        # Add the snow object to the new snow sprites group
        snow_sprites.add(snow)
        # snow_sprites_farther(snow)

        # Create smaller snow
        snow = Snow(random.choice([2, 5]))
        snow.rect.center = random_coords()
        snow.yvel = random.choice([1, 3])
        snow_sprites.add(snow)



    # TEST
    # snow.rect.center = (WIDTH // 2, HEIGHT // 2)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # ----- RENDER
        screen.fill(SKY_BLUE)

        # Draw all the sprite groups
        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def random_coords():
    x, y, = (
        random.randrange(0, WIDTH),
        random.randrange(0, HEIGHT)
    )
    return x, y


if __name__ == "__main__":
    main()