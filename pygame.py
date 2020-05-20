# Needed to use any and all python resources.
import pygame
import pygame_menu  #pip install pygame-menu
from os import path
from win32api import GetSystemMetrics 
import yahtzee        

# Defines common colors
background_one = (255, 255, 255)  # white
background_two = (0, 0, 0)  # black
FPS = 30 # frames per second

# Set the size of the window, variables can be used for positioning
# within program.
window_width = GetSystemMetrics((0))
window_height = GetSystemMetrics((1))


#create function to present text
font_name = pygame.font.match_font('arial') 
def text_draw(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, background_two)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


class Instruction(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = instr_img
        self.rect = self.image.get_rect()

# Initializes all pygame functionality.
pygame.init()
# Creates the window and puts a Surface into "screen".
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

pygame.display.set_caption('Yahtzee!')

#load in graphics
#find a way to make a img_dir that works for every user
instr_img = pygame.image.load(r'C:\Users\danar\GitHub\Yahtzee\Images\Instructions.PNG').convert()
instr_img_rect = instr_img.get_rect()

all_sprites = pygame.sprite.Group()
instruction = Instruction()
all_sprites.add(instruction)
# game loop
running = True
while running:
    clock.tick(FPS)
    # process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # update
    all_sprites.update()
    
    # render/draw
    screen.fill(background_one)
    all_sprites.draw(screen)
    pygame.display.flip() # always last
    
pygame.quit()