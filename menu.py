import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.width//2, self.game.height//2
        self.run_menu = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y, self.game.bordercolor)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        #reset key
        

class MainMenu(Menu):
    def __init__ (self, game):
        super().__init__(game)
        self.state = 'Start'
        self.startx, self.starty = self.mid_w, self.mid_h+30
        self.optionx, self.optiony = self.mid_w, self.mid_h+50
        self.cursor_rect.midtop = (self.startx+self.offset, self.starty)
        self.c = (221, 60, 20)
        self.o = (60, 221, 20)
    def display_menu(self):
        while self.run_menu:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.bgcolor)

            self.game.draw_text('Rules', 20, self.mid_w, self.mid_h-200, self.c)
            self.game.draw_text('The colors of the box changes', 12, self.mid_w, self.mid_h-180, self.c)
            self.game.draw_text('Each time you click on a box', 12, self.mid_w, self.mid_h-165, self.c)
            self.game.draw_text('Objective', 12, self.mid_w, self.mid_h-130, self.o)
            self.game.draw_text('All 9 boxes should have the same color to win', 12, self.mid_w, self.mid_h-115, self.o)
            self.game.draw_text('Main Menu', 20, self.mid_w, self.mid_h-20, self.game.bordercolor)
            self.game.draw_text('Start', 20, self.startx, self.starty, self.game.bordercolor)
            self.game.draw_text('Options', 20, self.optionx, self.optiony, self.game.bordercolor)
            self.game.draw_text('Creator: Frank B Gomes', 9, self.mid_w, self.mid_h+100, self.game.bordercolor)
            self.game.draw_text('Music: Frank B Gomes', 9, self.mid_w, self.mid_h+120, self.game.bordercolor)
            self.game.draw_text('Created using PyGame', 9, self.mid_w, self.mid_h+140, self.game.bordercolor)
            self.game.draw_text('Gomenasai! Options is work in progress', 9, self.mid_w, self.mid_h+200, (221, 60, 20))
            self.draw_cursor()
            self.blit_screen()
            self.game.reset_keys()

    def move_cursor(self):
        if self.game.down:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionx+self.offset, self.optiony)
                self.state = 'Option'
            elif self.state == 'Option':
                self.cursor_rect.midtop = (self.startx+self.offset, self.starty)
                self.state = 'Start'

        elif self.game.up:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionx+self.offset, self.optiony)
                self.state = 'Option'
            elif self.state == 'Option':
                self.cursor_rect.midtop = (self.startx+self.offset, self.starty)
                self.state = 'Start'
            

    def check_input(self):
        self.move_cursor()
        if self.game.start:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                pass

            self.run_menu = False
                
            
        
            
