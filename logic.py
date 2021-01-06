import pygame
import random

class GameLogic:
    def __init__(self, game):
        self.game = game
        self.rows, self.cols = 3, 3
        self.red = (219, 95, 95)
        self.green = (78, 201, 74)
        self.blue = (174, 198, 252)
        
        self.color_choice = [self.red, self.green, self.blue]
        self.map = {
            (0,0) : [(0,0), (0,1), (1,0)],
            (0,2) : [(0,2), (0,1), (1,2)],
            (2,0) : [(2,0), (1,0), (2,1)],
            (2,2) : [(2,2), (2,1), (1,2)],
            (1,1) : [(1,1), (0,1), (1,2), (1,0), (2,1)],
            (1,0) : [(1,0), (0,0), (1,1), (2,0)],
            (0,1) : [(0,1), (0,0), (1,1), (0,2)],
            (1,2) : [(1,2), (0,2), (1,1), (2,2)],
            (2,1) : [(2,1), (2,0), (1,1), (2,2)],
            }

        self.winconditions = [[[self.red,self.red,self.red],[self.red,self.red,self.red],[self.red,self.red,self.red]],
                              [[self.green,self.green,self.green],[self.green,self.green,self.green],[self.green,self.green,self.green]],
                              [[self.blue,self.blue,self.blue],[self.blue,self.blue,self.blue],[self.blue,self.blue,self.blue]],
                              ]
        
        
    def generate_colormap(self):
        generated = []
        for i in range(self.rows):
            temp = []
            generated.append(temp)
            for j in range(self.cols):
                temp.append(random.choice(self.color_choice))
        return generated

    def mapp(self, i, j):
        return i*self.game.scale, j*self.game.scale

    def conf_rowcol(self, mousevalue):
        return mousevalue[0]//self.game.scale, mousevalue[1]//self.game.scale

    def calculateColor(self, row, col, colormap):
        colorValue = colormap[row][col]
        colorIndex = self.color_choice.index(colorValue)
        count = colorIndex + 1
        if count > len(self.color_choice)-1:
            count = 0
        return self.color_choice[count]
        

    
                
