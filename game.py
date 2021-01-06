import pygame
from pygame import mixer
from menu import MainMenu
from logic import GameLogic
from end import End

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 600
        self.size = (self.width, self.height)
        self.scale = self.width // 3
        self.fps = 100

        self.display = pygame.Surface(self.size)
        self.end_display = pygame.Surface(self.size)
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption('ColorSnatch')
        self.clock = pygame.time.Clock()

        self.bgcolor = (40, 70, 70)
        self.bordercolor = (221, 221, 221)
        self.textcolor = (70, 40, 70)

        self.running, self.playing = True, False
        self.down, self.up, self.start, self.back = False, False, False, False
        self.mactive = False
        
        self.menu = MainMenu(self)
        self.logic = GameLogic(self)
        self.end = End(self)
        
        self.fontname = '8-BIT WONDER.ttf'

        #sounds
        mixer.music.load('sounds/background.mp3')
        mixer.music.play(-1)
        
    def game_loop(self):
        colormap = self.logic.generate_colormap()

##        colormap = [
##            [self.logic.red,self.logic.red,self.logic.red],
##            [self.logic.red,self.logic.red,self.logic.red],
##            [self.logic.red,self.logic.red,self.logic.red],
##            ]
        

        while self.playing:
            self.check_events()
            self.display.fill(self.bgcolor)
            
            
            #GRID
            self.draw_grid(colormap)
            if self.mactive:
                mousevalue = pygame.mouse.get_pos()
                rows, cols = self.logic.conf_rowcol(mousevalue)

                affected_neighbours = self.logic.map[(rows, cols)]
                for neighbours in affected_neighbours:
                    color_to_swap = self.logic.calculateColor(neighbours[0], neighbours[1], colormap)
                    colormap[neighbours[0]][neighbours[1]] = color_to_swap
            if colormap in self.logic.winconditions:
                self.end.draw_end_screen()
                self.window.blit(self.end_display, (0,0))
                    
                    
            
            pygame.display.update()
            self.window.blit(self.display, (0,0))
            self.clock.tick(self.fps)

            self.reset_keys()
        pygame.quit()

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.menu.run_menu = False
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q:
                    self.running, self.playing = False, False
                if ev.key == pygame.K_DOWN:
                    self.down = True
                if ev.key == pygame.K_UP:
                    self.up = True
                if ev.key == pygame.K_RETURN:
                    self.start = True
                if ev.key == pygame.K_BACKSPACE:
                    self.back = True
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                self.mactive = True
                    
    def reset_keys(self):
        self.down, self.up, self.start, self.back = False, False, False, False
        self.mactive = False
        
    def draw_text(self, text, size, x, y, textcolor):
        font = pygame.font.Font(self.fontname, size)
        text_surface = font.render(text, True, textcolor)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_grid(self, colormap):
        for i in range(self.logic.rows):
            for j in range(self.logic.cols):
                a, b = self.logic.mapp(i, j)
                border = pygame.Rect(a, b, self.scale, self.scale)
                cell = pygame.Rect(a, b, self.scale, self.scale)
                pygame.draw.rect(self.display, self.bordercolor, border, 15)
                pygame.draw.rect(self.display, colormap[i][j], cell)
                
                
        


