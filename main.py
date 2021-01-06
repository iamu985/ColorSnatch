import pygame
from game import Game

g = Game()
while g.running:
    g.menu.display_menu()
    g.game_loop()
