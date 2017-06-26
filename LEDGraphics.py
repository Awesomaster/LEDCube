import pygame
import time
import run

start_time = time.time()
print('LEFT CLICK TO TURN ONE ON, RIGHT CLICK TO TURN IT OFF')
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
lightgreen = (100,255,100)

size = 50
margin = 5
n = 8

gridy = []
for layer in range(n):
    gridy.append([])
    for row in range(n):
        gridy[layer].append([])
        for column in range(n):
            gridy[layer][row].append(0)



# Initialize pygame
pygame.init()

# Set the size and size of the screen
window_width = n*size+(n+1)*size
window_height = (n+1)*size+(n+2)*size
window_size = [window_width, window_height]
screen = pygame.display.set_mode(window_size)

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

        while not done:
            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    reallyDone = True
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()

                    column = pos[0] // (size + margin)
                    row = pos[1] // (size + margin)

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

            screen.fill(black)

            for row in range(8):
                for column in range(8):
                    color = white
                    if i>1:
                        if gridy[i-2][row][column] == 1:
                            color = lightgreen

                    if grid[row][column] == 1:
                        color = green
                    pygame.draw.rect(screen,
                                     color,
                                     [(margin + size) * column + margin,
                                      (margin + size) * row + margin,
                                      size,
                                      size])

                pygame.draw.rect(screen,
                                 white,
                                 [margin,
                                  window_width,
                                  window_width-(2*margin),
                                  size])

                myfont = pygame.font.SysFont("monospace", 30)
                label = myfont.render("Layer: "+str(i), 1, (0,0,0))
                screen.blit(label, (margin, window_width+(2*margin)))

            clock.tick(60)
            pygame.display.flip()
        done = False
    reallyDone = True
    
run.send(gridy)
pygame.quit()
