import pygame
import cv2
import random
import numpy as np


# Display height and width 
window = (800,600)
screen = pygame.display.set_mode(window)
#Title
pygame.display.set_caption("Purple Rain")
# Background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((220, 220, 220))
pygame.display.flip()
background_position = [0,0]

# Declaring raindrops location
color = (128,0,128)
raindrops = []
for drop in range(200):
  x = random.randrange(0, window[0])
  y = random.randrange(0,window[1])
  length = random.randrange(4,15)
  speed = random.randrange(2,4)*0.25
  width = random.randrange(1,2)
  raindrops.append([x, y, length, speed, width])

time = pygame.time.Clock()


running = True
while running:
  #Exit
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
      running = False
  # overwrite the screen that the screen doesnt get filled up purple
  screen.blit(background, background_position)
  
  # Drawing the Raindrops
  for drop in raindrops:
    # Make the Drops move with gravity
    drop[1] += 0.25 + drop[3]
    # Draw the Drops (screen, color, start-pos, end-pos, width)
    pygame.draw.line(screen, color, (drop[0],drop[1]),(drop[0],drop[1]+drop[2]), drop[4])

    if drop[1] > window[1]:
      drop[0] = random.randrange(0,window[0])
      drop[1] = random.randrange(-50, 0)
      drop[2] = random.randrange(4,15)
      drop[3] = random.randrange(2,4)*0.25
      drop[4] = random.randrange(1,2)
  
  
  # update display    
  pygame.display.flip()
  time.tick(600)

pygame.quit()