import pygame
import os   

bg_start_filename = './Background/start.png'
bg_set_filename = './Background/set.png'
bg_reg_filename = './Background/reg.jpg'
bg_log_filename = './Background/log.jpg'
bg_enter_filename = './Background/enter.png'
bg_game_filename = './Background/game.png'
Image_dir = r"./Game_Image"
bg_stop_filename = './Background/stop.png'
bg_victory_filename = './Background/victory.png'
bg_rank_filename = './Background/rank.png'

class Settings():
    def __init__(self):
        self.screen_width = 994
        self.screen_height = 653
        self.bg_start = pygame.image.load(bg_start_filename)
        self.bg_set = pygame.image.load(bg_set_filename)
        self.bg_reg = pygame.image.load(bg_reg_filename)
        self.bg_log = pygame.image.load(bg_log_filename)
        self.bg_enter = pygame.image.load(bg_enter_filename)
        self.bg_game = pygame.image.load(bg_game_filename)
        self.pintu_list = []
        self.pintu = pygame.image.load("./Game_Image/1.jpg")
        self.bg_stop = pygame.image.load(bg_stop_filename)
        self.bg_victory = pygame.image.load(bg_victory_filename)
        self.bg_rank = pygame.image.load(bg_rank_filename)

        for files in os.walk(Image_dir): 
            self.pintu_list = files[2]