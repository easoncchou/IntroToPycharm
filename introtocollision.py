import pygame
import random
import time

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "intro to collision"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/squirtle_sprite.png")
        # Resize
        self.image = pygame.transform.scale(
            self.image,
            (75, 75),
        )


        # Rect
        self.rect = self.image.get_rect()

        self.last_collided = 0

    def update(self):
        """Follow the mouse"""

        self.rect.center = pygame.mouse.get_pos()

        if pygame.time.get_ticks() - self.last_collided > 500:
            self.image = pygame.image.load("./assets/squirtle_sprite.png")
            self.image = pygame.transform.scale(
                self.image,
                (75, 75),
            )




    def collidefx(self):
        self.image = pygame.image.load("./assets/explosion_sprite.png")
        self.image = pygame.transform.scale(
            self.image,
            (100, 100),
        )

        self.last_collided = pygame.time.get_ticks()


class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/ultra_ball.png")
        # Resize
        self.image = pygame.transform.scale(
            self.image,
            (50, 50)
        )
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = random_coords()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Call superclass constructor
        super().__init__()

        self.image = pygame.image.load("./assets/gengar_sprite.png")
        self.image = pygame.transform.scale(
            self.image,
            (75, 75),
        )

        self.rect = self.image.get_rect()
        self.rect.center = random_coords()
        self.xvel = 2      # pixel per 1/60th second
        self.yvel = 2

    def update(self):
        """Change the x coordinate based on the xvel"""
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        # bounce the logo
        # if the ball hits the sides of the screen, reverse its x velocity
        if self.rect.x < 0:
            self.rect.x = 0
            self.xvel *= -1
        if self.rect.x > WIDTH - 75:
            self.rect.x = WIDTH - 75
            self.xvel *= -1
        # if the logo hits the top or the bottom, reverse its y velocity
        if self.rect.y < 0:
            self.rect.y = 0
            self.yvel *= -1
        if self.rect.y > HEIGHT - 75:
            self.rect.y = HEIGHT - 75
            self.yvel *= -1



def random_coords() -> list:
    """Returns a random x, y coordinate"""
    return random.randrange(0, WIDTH), random.randrange(0, HEIGHT)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    num_treasure = 7
    num_enemy = 4
    score = 0
    coin_sound = pygame.mixer.Sound("./assets/coinsound.ogg")
    lives = num_enemy

    # Create sprite groups
    all_sprites_group = pygame.sprite.Group()
    treasure_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()


    # Create sprites to fill groups

    # Create treasure sprites
    for i in range(num_treasure):
        treasure = Treasure()

        # Add it to Both lists
        all_sprites_group.add(treasure)
        treasure_sprites_group.add(treasure)

    player = Player()
    all_sprites_group.add(player)

    # Create enemy sprites to fill groups
    for i in range(num_enemy):
        enemy = Enemy()

        # Add it to both lists
        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        # Deal with player colliding with treasure sprites
        # PLAYER collides with any sprite from TREASURE_SPRITE_GROUP
        collided_treasure = pygame.sprite.spritecollide(player, treasure_sprites_group, dokill=True)

        collided_enemy = pygame.sprite.spritecollide(player, enemy_sprites_group, dokill=True)


        if len(collided_treasure) > 0:
            # some collision has happened
            # TODO: Play sound when collected
            coin_sound.play()
            score += 1

            # Replace the treasure
            treasure = Treasure()
            all_sprites_group.add(treasure)
            treasure_sprites_group.add(treasure)

        if len(collided_enemy) > 0:
            # some collision has happened
            lives -= 1
            player.collidefx()

        # Iterate through all collided treasure
        for treasure in collided_treasure:
            print(f"treasure x: {treasure.rect.x}")
            print(f"treasure y: {treasure.rect.y}")
            print(f"score is {score}")

        # Iterate through all collided enemy
        for enemy in collided_enemy:
            print(f"enemy x: {treasure.rect.x}")
            print(f"enemy y: {treasure.rect.y}")
            print(f"you have {lives} left")

        # ----- RENDER
        screen.fill(WHITE)
        all_sprites_group.draw(screen)


        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()