import os
import pygame

# init
pygame.init()
clock = pygame.time.Clock()

# settings
WIDTH, HEIGHT = 1920, 1080

# load song
song = pygame.mixer.Sound("song.wav")

# load frames
print("loading frames...")
frames = []
for name in sorted(os.listdir("frames"), key=lambda x: int(os.path.splitext(x)[0])):
    frames.append(pygame.transform.scale(pygame.image.load(os.path.join("frames", name)), (WIDTH, HEIGHT)))
print("frames loaded")

# setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bad apple")

# play music
song.play()

# main loop
for f in frames:
    # show image on screen
    screen.blit(f, (0, 0))
    pygame.display.flip()
    
    # fps
    clock.tick(29.97)
