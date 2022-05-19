# Intro to Pygame

import pygame

pygame.init()

# Constants
BLACK   = (  0,  0,  0)
WHITE   = (255,255,255)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)

colour_list = [BLACK, WHITE]

WINDOW_TITLE = "Pygame Introduction"

def main():
    # Create a Window
    screen_size = (1000, 1000)
    screen = pygame.display.set_mode(screen_size)

    # Set the title of the window
    pygame.display.set_caption(WINDOW_TITLE)

    done = False

    clock = pygame.time.Clock()

    # MAIN PROGRAM LOOP
    while not done:
        #------event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # When the user clicks the red quit button
                done = True
            elif event.type == pygame.KEYDOWN:
                print("A key has been pressed down")
            elif event.type == pygame.KEYUP:
                print("A key has been let go of")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("A mouse button has been pressed")

        #------environment logic

        #------render the environment

        # Fill the screen with a background colour
        screen.fill(WHITE)

        # Draw a rectangle
        # rect -> [x, y, width, height]
        # pygame.draw.rect(screen, GREEN, [0,0, 400, 200])

        # Draw a range of lines
        # for delta_y in range (30, 230, 10):
           # pygame.draw.line(screen, BLUE, (0, 10 + delta_y), (100, 100))

        # Draw a line
        # pygame.draw.line(screen, BLACK, (0,0), screen_size)
        for number in  range 
            for number in range (0, 100, 1):
                if number % 2 == 0:
                    pygame.draw.rect(screen, colour_list[0], [0, 10 + 100 * number, 100, 100])
                elif number % 2 == 1:
                    pygame.draw.rect(screen, colour_list[1], [0, 10 + 100 * number, 100, 100])


        #------flip the display

        # Updates the screen  with what we've drawn
        pygame.display.flip()

        # Tick the clock
        clock.tick(75)


if __name__ == "__main__":
    main()