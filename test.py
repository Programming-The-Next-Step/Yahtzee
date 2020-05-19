# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:43:54 2020

@author: danar
"""
https://gamedevacademy.org/a-comprehensive-introduction-to-pygame/
# Needed to use any and all python resources.
import pygame
import sys
 
# Defines common colors
background_one = (0, 0, 0)  # black
background_two = (255, 255, 255)  # white
# red: (255, 0, 0)
# purple: (255, 0, 255)
# light salmon: (255, 160, 122)
 
# Initializes all pygame functionality.
pygame.init()
 
# Set the size of the window, variables can be used for positioning
# within program.
window_width = 700
window_height = 400
 
# Creates the window and puts a Surface into "screen".
screen = pygame.display.set_mode((window_width, window_height))
 
# Sets title of window, not needed for the game to run but
# unless you want to try telling everyone your game is called
# "Game Title", make sure to set the caption :)
pygame.display.set_caption("Game Title Here")
 
# Used for timing within the program.
clock = pygame.time.Clock()
 
# Used for timed events.
milli_timer = 0
white_flash_time = 1000  # Milliseconds between the screen being filled white
black_flash_time = 500   # Milliseconds between the screen being filled black
 
# Main loop of the program.
while True:
    # Event processing here, stuff the users does.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # When user presses a key.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
            elif event.key == pygame.K_DOWN:
                print("DOWN")
 
    # Add the amount of milliseconds passed
    # from the last frame.
    milli_timer += clock.get_time()
 
    # Every 1000 milliseconds, fill it with white
    if milli_timer > white_flash_time:
        screen.fill(background_two)
        milli_timer = 0  # Reset timer
    # Every 500 milliseconds, fill it with black.
    elif milli_timer > black_flash_time:
        screen.fill(background_one)
 
    # Display all images drawn.
    # This removes flickering images and makes it easier for the processor.
    pygame.display.flip()
 
    # Defines the frame rate. The number is number of frames per second.
    clock.tick(20)