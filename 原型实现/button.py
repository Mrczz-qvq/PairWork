import pygame.font

class startButton():
    
    def __init__(self, ai_settings, screen, msg, loc, size):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 140, 40
        self.text_color = (0, 0, 0)
        self.highlight_color = (220, 220, 220)
        self.font = pygame.font.SysFont('方正粗黑宋简体', size)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + 15
        self.rect.top = loc

        self.prep_msg(msg)
        self.prep_highlight_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.blit(self.msg_image, self.msg_image_rect) 
    
    def prep_highlight_msg(self, msg):
        self.highlight_msg = self.font.render(msg, True, self.highlight_color, None)
        self.highlight_msg_rect = self.highlight_msg.get_rect()
        self.highlight_msg_rect.center = self.rect.center

    def highlight_button(self):
        self.screen.blit(self.highlight_msg, self.highlight_msg_rect)

class loginButton():
    def __init__(self, msg, screen, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 100, 30
        self.button_color = (0, 191, 255)
        self.highlight_color = (30, 144, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('方正粗黑宋简体', 20)

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def highlight_button(self):
        self.screen.fill(self.highlight_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class gameButton():

    def __init__(self, ai_settings, screen, msg, x, y, size, weight, height):
        self.screen = screen

        self.x = x
        self.y = y
        self.text_color = (0, 0, 0)
        self.highlight_color = (220, 220, 220)
        self.font = pygame.font.SysFont('方正粗黑宋简体', size)
        self.rect = pygame.Rect(x, y, weight, height)

        self.prep_msg(msg)
        self.prep_highlight_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color)

    def draw_button(self):
        self.screen.blit(self.msg_image, self.rect) 
    
    def prep_highlight_msg(self, msg):
        self.highlight_msg = self.font.render(msg, True, self.highlight_color)

    def highlight_button(self):
        self.screen.blit(self.highlight_msg, self.rect)

class reminderButton():

    def __init__(self, ai_settings, screen, width, height, x, y):
        self.screen = screen
        
        self.button_color = (190, 190, 190)
        self.confirm = 1
        self.confirm_color = (255, 0, 0)

        self.rect = pygame.Rect(x, y, width, height)

    def draw_button(self):
        if self.confirm == 0:
            self.screen.fill(self.button_color, self.rect)
        else:
            self.screen.fill(self.confirm_color, self.rect)

    def confirm_button(self):
        self.confirm = 1

    def cancel_button(self):
        self.confirm = 0
    