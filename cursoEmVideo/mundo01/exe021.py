'''
Faça um programa em python que abra e reprodusa um arquivo mp3
'''

import pygame;
pygame.init();
pygame.mixer.music.load('d:\Works\python\cursoEmVideo\mundo01\pitch-up.mp3')
pygame.mixer.music.play()
pygame.event.wait()