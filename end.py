import pygame
import sys

class End:
    def __init__(self, game):
        self.game = game
        self.state = 'Restart'
        self.run_end = True
        self.mid_w, self.mid_h = self.game.width//2, self.game.height//2
        
        self.offset = -100
        self.restart_x, self.restart_y = self.mid_w, self.mid_h+30
        self.quit_x, self.quit_y = self.mid_w, self.mid_h+50
        
        self.game.menu.cursor_rect.midtop = (self.restart_x+self.offset, self.restart_y)
        
    def draw_end_screen(self):
        message = 'Congratulations!! You Won!!'
        while self.run_end:
            self.game.check_events()
            self.check_input()

            self.game.end_display.fill(self.game.bgcolor)
            self.draw_text(message, 24, self.mid_w, self.mid_h-100)
            self.draw_text('Restart', 20, self.restart_x, self.restart_y)
            self.draw_text('Quit', 20, self.quit_x, self.quit_y)

            self.draw_cursor()
            self.blit_screen()
            self.game.reset_keys()

    def move_cursor(self):
        if self.game.down:
            if self.state == 'Restart':
                self.game.menu.cursor_rect.midtop = (self.quit_x+self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.game.menu.cursor_rect.midtop = (self.restart_x+self.offset, self.restart_y)
                self.state = 'Restart'

        elif self.game.up:
            if self.state == 'Restart':
                self.game.menu.cursor_rect.midtop = (self.quit_x+self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.game.menu.cursor_rect.midtop = (self.restart_x+self.offset, self.restart_y)
                self.state = 'Restart'

    def check_input(self):
        self.move_cursor()
        if self.game.start:
            if self.state == 'Restart':
                self.game.playing = True
            elif self.state == 'Quit':
                pygame.quit()
                sys.exit()
            self.run_end = False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.game.fontname, size)
        msg = font.render(text, True, self.game.bordercolor)
        rect = msg.get_rect()

        rect.center = (x, y)
        self.game.end_display.blit(msg, rect)

    def draw_cursor(self):
        self.draw_text('*', 15, self.game.menu.cursor_rect.x, self.game.menu.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.end_display, (0,0))
        pygame.display.update()
        
            


'''
        font = pygame.font.Font(self.game.fontname, 24)
        
        self.end_display.fill(self.game.bgcolor)
            
        end_msg = font.render(message, True, self.game.textcolor)
        end_rect = end_msg.get_rect()
        end_rect.center = (self.mid_w, self.mid_h)
            
        self.end_display.blit(end_msg, end_rect)
        self.game.window.blit(self.end_display, (0,0))
        pygame.display.update()
'''        
        


