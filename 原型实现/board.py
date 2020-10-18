import pygame.font

class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.step)
        self.score_image = self.font.render(score_str, True, self.text_color)

    def show_score(self):
        self.screen.blit(self.score_image, (780, 245))

class Timeboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_time()

    def prep_time(self):
        time_str = str(self.stats.time) + 's'
        self.time_image = self.font.render(time_str, True, self.text_color)

    def show_time(self):
        self.screen.blit(self.time_image, (780, 390))

class Showboard():
    def __init__(self, ai_settings, screen, stats, msg, x, y, size, color):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats

        self.text = msg
        self.text_color = color
        self.font = pygame.font.SysFont('方正粗黑宋简体', size)
        self.rect = screen.get_rect()
        self.x = x
        self.y = y

        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.text, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.x, self.y)

    def show_msg(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)