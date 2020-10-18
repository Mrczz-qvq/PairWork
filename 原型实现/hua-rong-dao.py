# encoding:utf-8
import sys
import pygame
from settings import Settings
import game_functions as gf
from button import startButton
from button import loginButton
from button import gameButton
from button import reminderButton
from game_stats import GameStats
from inputBox_test import TextBox
from map import Map
from board import Scoreboard
from board import Timeboard
from board import Showboard
import json
import random

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Hua-Rong-Dao")
    stats = GameStats(ai_settings)
    
    filename1 = './Information/userInformation.json'
    with open(filename1) as f_obj:
        stats.user_info = json.load(f_obj)
    filename2 = './Information/game_record.json'
    with open(filename2) as f_obj:
        stats.game_record = json.load(f_obj)

    pygame.mixer.init()
    pygame.mixer.music.load('./Background/BGmusic.mp3')
    pygame.mixer.music.play(-1, 0.0)

    playButton = startButton(ai_settings, screen, "进入游戏", 344, 15)
    regButton = startButton(ai_settings, screen, "注册", 410, 15)
    setButton = startButton(ai_settings, screen, "系统设置", 478, 15)
    exitButton = startButton(ai_settings, screen, "退出", 546, 15)

    enterButton = startButton(ai_settings, screen, "开始游戏", 175, 20)
    rankButton = startButton(ai_settings, screen, "排行榜", 325, 20)
    backButton = startButton(ai_settings, screen, "返回", 482, 20)

    stopButton = gameButton(ai_settings, screen, "暂停", 480, 50, 20, 40, 25)
    returnButton = gameButton(ai_settings, screen, "返回", 620, 208, 30, 60, 35)
    resetButton = gameButton(ai_settings, screen, "设置", 620, 350, 30, 60, 35)
    closeButton = gameButton(ai_settings, screen, "退出", 620, 495, 30, 60, 35)
    replayButton = gameButton(ai_settings, screen, "重玩", 325, 458, 30, 60, 35)
    menuButton = gameButton(ai_settings, screen, "返回", 620, 458, 30, 60, 35)
    rkButton = gameButton(ai_settings, screen, "返回", 757, 480, 20, 40, 25)
    srButton = gameButton(ai_settings, screen, "返回", 765, 465, 20, 40, 25)

    username_box_log = TextBox(200, 30, screen_rect.centerx-80, screen_rect.centery-50)
    password_box_log = TextBox(200, 30, screen_rect.centerx-80, screen_rect.centery)

    username_box_reg = TextBox(200, 30, screen_rect.centerx-80, screen_rect.centery-50)
    password_box_reg = TextBox(200, 30, screen_rect.centerx-80, screen_rect.centery)

    return_button = loginButton("返回", screen, screen_rect.centerx-130, screen_rect.centery+60)
    confirm_button = loginButton("确定", screen, screen_rect.centerx+30, screen_rect.centery+60)
    register_button = loginButton("注册", screen, screen_rect.centerx+30, screen_rect.centery+60)

    musicBoard = Showboard(ai_settings, screen, stats, '背景音乐', 300, 330, 40, (255, 0, 0))
    soundBoard = Showboard(ai_settings, screen, stats, '游戏音效', 600, 330, 40, (255, 0, 0))

    musicButton = reminderButton(ai_settings, screen, 40, 40, 400, 310)
    soundButton = reminderButton(ai_settings, screen, 40, 40, 700, 310)

    while True:
        gf.check_events_start(stats, playButton, setButton, regButton, exitButton)
        if stats.page == 'Start':
            gf.update_startScreen(ai_settings, screen, playButton, setButton, regButton, exitButton)
       
        elif stats.page == 'Login':
            while stats.page == 'Login':
                gf.update_loginScreen(stats, ai_settings, screen, username_box_log, password_box_log, return_button, confirm_button)
                pygame.display.flip()

        elif stats.page == 'Enter':
            while stats.page == 'Enter':
                gf.update_enterScreen(stats, ai_settings, screen, enterButton, rankButton, backButton)
                pygame.display.flip()

        elif stats.page == 'Game':
            image_map = Map()
            image_map.randMap()
            index = random.randint(0, len(ai_settings.pintu_list)-1)
            ai_settings.pintu = pygame.image.load("./Game_Image/" + ai_settings.pintu_list[index])
            stats.step = 0
            stats.time = 0
            stats.count = 0
            stats.game_active = True

            sb = Scoreboard(ai_settings, screen, stats)
            tb = Timeboard(ai_settings, screen, stats)
            while stats.page == 'Game':
                while stats.game_active and stats.page == 'Game':
                    gf.update_gameScreen(stats, ai_settings, screen, image_map, sb, tb, stopButton)
                    pygame.display.flip()
                while not stats.game_active and stats.page == 'Game' and not stats.game_set:
                    gf.update_stopScreen(stats, ai_settings, screen, returnButton, resetButton, closeButton)
                    pygame.display.flip()
                while stats.game_set and stats.page == 'Game':
                    screen.blit(ai_settings.bg_set, (0, 0))
                    musicBoard.show_msg()
                    soundBoard.show_msg()
                    musicButton.draw_button()
                    soundButton.draw_button()
                    srButton.draw_button()

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if srButton.rect.collidepoint(mouse_x, mouse_y):
                        srButton.highlight_button()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            if rkButton.rect.collidepoint(mouse_x, mouse_y):
                                    stats.game_set = False
                            elif musicButton.rect.collidepoint(mouse_x, mouse_y):
                                if musicButton.confirm == 0:
                                    musicButton.confirm_button()
                                    pygame.mixer.music.play(-1, 0.0)
                                else: 
                                    musicButton.cancel_button()
                                    pygame.mixer.music.stop()
                            elif soundButton.rect.collidepoint(mouse_x, mouse_y):
                                if soundButton.confirm == 0:
                                    soundButton.confirm_button()
                                else:
                                    soundButton.cancel_button()
                
                    pygame.display.flip()

        elif stats.page == 'Victory':
            pygame.time.delay(500)
            time = Showboard(ai_settings, screen, stats, str(stats.time)+'s', 500, 350, 25, (0, 0, 0))
            step = Showboard(ai_settings, screen, stats, str(stats.step), 500, 395, 25, (0, 0, 0))
            while stats.page == 'Victory':
                gf.update_victoryScreen(stats, ai_settings, screen, replayButton, menuButton, time, step)
                pygame.display.flip()

        elif stats.page == 'Set':
            while stats.page == 'Set':
                screen.blit(ai_settings.bg_set, (0, 0))
                musicBoard.show_msg()
                soundBoard.show_msg()
                musicButton.draw_button()
                soundButton.draw_button()
                srButton.draw_button()

                mouse_x, mouse_y = pygame.mouse.get_pos()
                if srButton.rect.collidepoint(mouse_x, mouse_y):
                    srButton.highlight_button()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if rkButton.rect.collidepoint(mouse_x, mouse_y):
                            if stats.game_active:
                                stats.page = 'Start'
                            else:
                                stats.page = 'Game'
                        elif musicButton.rect.collidepoint(mouse_x, mouse_y):
                            if musicButton.confirm == 0:
                                musicButton.confirm_button()
                                pygame.mixer.music.play(-1, 0.0)
                            else: 
                                musicButton.cancel_button()
                                pygame.mixer.music.stop()
                        elif soundButton.rect.collidepoint(mouse_x, mouse_y):
                            if soundButton.confirm == 0:
                                soundButton.confirm_button()
                            else:
                                soundButton.cancel_button()
                
                pygame.display.flip()

        elif stats.page == 'Rank':
            while stats.page == 'Rank':
                rankBoard1 = Showboard(ai_settings, screen, stats, str((stats.game_record[stats.player])[0]) + '步   ' + 
                str((stats.game_record[stats.player])[1]) + 's', 620, 240, 35, (255, 0, 0))
                rank = []
                for key, value in stats.game_record.items():
                    if value[0] == 0:
                        continue
                    dict = {}
                    dict['name'] = key
                    dict['step'] = value[0]
                    dict['time'] = value[1]
                    rank.append(dict)
                rank_order = sorted(rank, key = lambda i: (i['step'], i['time'])) 
                
                rankBoard2 = Showboard(ai_settings, screen, stats, (rank_order[0])['name'], 460, 330, 30, (0, 0, 0))
                rankBoard3 = Showboard(ai_settings, screen, stats, (rank_order[1])['name'], 460, 380, 30, (0, 0, 0))
                rankBoard4 = Showboard(ai_settings, screen, stats, (rank_order[2])['name'], 460, 430, 30, (0, 0, 0))
                rankBoard5 = Showboard(ai_settings, screen, stats, str((rank_order[0])['step']), 595, 330, 30, (0, 0, 0))
                rankBoard6 = Showboard(ai_settings, screen, stats, str((rank_order[1])['step']), 595, 380, 30, (0, 0, 0))
                rankBoard7 = Showboard(ai_settings, screen, stats, str((rank_order[2])['step']), 595, 430, 30, (0, 0, 0))
                rankBoard8 = Showboard(ai_settings, screen, stats, str((rank_order[0])['time']), 740, 330, 30, (0, 0, 0))
                rankBoard9 = Showboard(ai_settings, screen, stats, str((rank_order[1])['time']), 740, 380, 30, (0, 0, 0))
                rankBoard10 = Showboard(ai_settings, screen, stats, str((rank_order[1])['time']), 740, 430, 30, (0, 0, 0))
                rankBoard11 = Showboard(ai_settings, screen, stats, '1', 320, 330, 30, (0, 0, 0))
                rankBoard12 = Showboard(ai_settings, screen, stats, '2', 320, 380, 30, (0, 0, 0))
                rankBoard13 = Showboard(ai_settings, screen, stats, '3', 320, 430, 30, (0, 0, 0))

                rankBoard_list = [rankBoard1, rankBoard2, rankBoard3, rankBoard4, rankBoard5, rankBoard6, rankBoard7,
                rankBoard8, rankBoard9, rankBoard10, rankBoard11, rankBoard12, rankBoard13]


                gf.update_rankScreen(stats, ai_settings, screen, rkButton, rankBoard_list)
                pygame.display.flip()

        elif stats.page == 'Register':
            while stats.page == 'Register':
                gf.update_regScreen(stats, ai_settings, screen, username_box_reg, password_box_reg, return_button, register_button)
                pygame.display.flip()

        pygame.display.flip()

run_game()
