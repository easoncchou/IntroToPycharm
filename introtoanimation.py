import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "DVD Screensaver"

class Dvdlogo(pygame.sprite.Sprite):
    def __init__(self):
        # Call superclass constructor
        super().__init__()

        self.image = pygame.image.load("./assets/dvd_logo.png")
        self.image = pygame.transform.scale(
            self.image,
            (200, 115),
        )
        # Default (x,y) is (0,0)
        self.rect = self.image.get_rect()
        self.xvel = 2      # pixel per 1/60th second
        self.yvel = 2

    def update(self):
        """Change the x coordinate based on the xvel"""
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        # bounce the logo
        # if the ball hits the sides of the screen, reverse its x velocity
        if self.rect.x < 0 or self.rect.x > WIDTH - 200:
            self.xvel = (self.xvel * - 1)
        # if the logo hits the top or the bottom, reverse its y velocity
        if self.rect.y < 0 or self.rect.y > HEIGHT - 115:
            self.yvel = (self.yvel * -1)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()


    dvd_logo = Dvdlogo()
    # set coordinates of dvd_logo explicitly
    dvd_logo.rect.x = 100
    dvd_logo.rect.y = 100

    # Create an all_sprites_group object
    all_sprites_group = pygame.sprite.Group()

    # Add the Dvdlogo sprite to the all_sprites_group
    all_sprites_group.add(dvd_logo)


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # Update all sprites
        all_sprites_group.update()


        # ----- RENDER
        screen.fill(WHITE)

        all_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()