import pygame
pygame.init()
pygame.mixer.music.load('MP3EU.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Aperte enter para parar')
pygame.quit()