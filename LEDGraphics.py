import pygame
import time

start_time = time.time()
print('LEFT CLICK TO TURN ONE ON, RIGHT CLICK TO TURN IT OFF')
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHTGREEN = (100,255,100)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 50
HEIGHT = 50
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
gridy = []
for layer in range(8):
    gridy.append([])
    for row in range(8):
        gridy[layer].append([])
        for column in range(8):
            gridy[layer][row].append(0)
 

 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [445, 500]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("LED Cube")
 
# Loop until the user clicks the close button.
done = False
reallyDone = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
while not reallyDone:
    for i in range(8):
        grid = gridy[i]
        i+=1
        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:  # If user clicked close
                    reallyDone = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (WIDTH + MARGIN)
                    row = pos[1] // (HEIGHT + MARGIN)
                    # Set that location to one
                    if event.button == 1:
                        if row >= 8:
                            done = True
                        else:
                            grid[row][column] = 1
                    elif event.button == 3:
                        if row >= 8:
                            done = True
                        else:
                            grid[row][column] = 0
                            print(grid[row][column])
                    print("Click ", pos, "Grid coordinates: ", row, column)
         
            screen.fill(BLACK)
         
            for row in range(8):
                for column in range(8):
                    color = WHITE
                    if i>1:
                        if gridy[i-2][row][column] == 1:
                            color = LIGHTGREEN
                            
                    if grid[row][column] == 1:
                        color = GREEN
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                pygame.draw.rect(screen, WHITE, [5, 445, 435, 50])
                myfont = pygame.font.SysFont("monospace", 30)

                label = myfont.render("Layer: "+str(i), 1, (0,0,0))
                screen.blit(label, (5, 455))
            clock.tick(60)
            pygame.display.flip()
        done = False
        print(grid)
    reallyDone = True
print(gridy)
pygame.quit()
