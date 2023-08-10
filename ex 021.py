#Type a code using python that opens and plays the audio of an mp3 file

import pygame

pygame.init()
pygame.mixer.music.load('ex 021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
