import os
import pygame

# Inisialisasi Pygame Mixer
pygame.mixer.init()

# Path relatif ke file suara
path_suara = os.path.join("suara", "saya.wav")

# Muat efek suara
suara_efek = pygame.mixer.Sound(path_suara)
