import sys
import pygame
from map import Map
import json

def check_events_start(stats, playButton, setButton, regButton, exitButton):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_startButton(stats, playButton, setButton, regButton, exitButton, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(stats, event)

def check_events_login(text_box):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            text_box.key_down(event)

def check_startButton(stats, playButton, setButton, regButton, exitButton, mouse_x, mouse_y):
    if stats.page=='Start' and playButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Login'
    elif stats.page=='Start' and setButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Set'
    elif stats.page=='Start' and regButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Register'
    elif stats.page=='Start' and exitButton.rect.collidepoint(mouse_x, mouse_y):
        sys.exit()

def update_startScreen(ai_settings, screen, playButton, setButton, regButton, exitButton):
    screen.blit(ai_settings.bg_start, (0,0))
    playButton.draw_button()
    setButton.draw_button()
    regButton.draw_button()
    exitButton.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if playButton.rect.collidepoint(mouse_x, mouse_y):
        playButton.highlight_button()
    elif setButton.rect.collidepoint(mouse_x, mouse_y):
        setButton.highlight_button()
    elif regButton.rect.collidepoint(mouse_x, mouse_y):
        regButton.highlight_button()
    elif exitButton.rect.collidepoint(mouse_x, mouse_y):
         exitButton.highlight_button()

def update_enterScreen(stats, ai_settings, screen, enterButton, rankButton, backButton):
    screen.blit(ai_settings.bg_enter, (0,0))
    enterButton.draw_button()
    rankButton.draw_button()
    backButton.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if enterButton.rect.collidepoint(mouse_x, mouse_y):
        enterButton.highlight_button()
    if rankButton.rect.collidepoint(mouse_x, mouse_y):
        rankButton.highlight_button()
    if backButton.rect.collidepoint(mouse_x, mouse_y):
        backButton.highlight_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_enterButton(stats, enterButton, rankButton, backButton, mouse_x, mouse_y)

def check_enterButton(stats, enterButton, rankButton, backButton, mouse_x, mouse_y):
    if enterButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Game'
    if backButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Start'
    if rankButton.rect.collidepoint(mouse_x, mouse_y):
        stats.page = 'Rank'


def update_loginScreen(stats, ai_settings, screen, username_box, password_box, return_button, confirm_button):
    screen.blit(ai_settings.bg_log, (0,0))
    screen_rect = screen.get_rect()
    draw_box(screen)
    return_button.draw_button()
    confirm_button.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if return_button.rect.collidepoint(mouse_x, mouse_y):
        return_button.highlight_button()
    if confirm_button.rect.collidepoint(mouse_x, mouse_y):
        confirm_button.highlight_button()   

    username_box_rect = pygame.Rect(screen_rect.centerx-80, screen_rect.centery-50, 200, 30)
    password_box_rect = pygame.Rect(screen_rect.centerx-80, screen_rect.centery, 200, 30)

    if stats.username_input:
        pygame.draw.rect(screen, (220, 220, 220), username_box_rect, 0)
    else:
        pygame.draw.rect(screen, (255, 255, 255), username_box_rect, 0)      

    if stats.password_input:    
        pygame.draw.rect(screen, (220, 220, 220), password_box_rect, 0)
    else:
        pygame.draw.rect(screen, (255, 255, 255), password_box_rect, 0)        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if username_box_rect.collidepoint(mouse_x, mouse_y):
                stats.username_input = True
                stats.password_input = False
            if password_box_rect.collidepoint(mouse_x, mouse_y):
                stats.password_input = True
                stats.username_input = False
            if return_button.rect.collidepoint(mouse_x, mouse_y):
                stats.page = 'Start'
                username_box.clear()
                password_box.clear()
                stats.username_input = False
                stats.password_input = False               
            if confirm_button.rect.collidepoint(mouse_x, mouse_y):
                username = username_box.get_text()
                password = password_box.get_text()
                if (username in stats.user_info) and (stats.user_info[username] == password):
                    stats.player = username
                    stats.page = 'Enter'
                    username_box.clear()
                    password_box.clear()
                    stats.username_input = False
                    stats.password_input = False 
                else:
                    password_box.clear()
        elif event.type == pygame.KEYDOWN:
            if stats.username_input:
                username_box.key_down(event)
            if stats.password_input:
                password_box.key_down(event)

    pygame.time.delay(33)
    username_box.draw(screen)
    password_box.draw(screen)

def update_regScreen(stats, ai_settings, screen, username_box, password_box, return_button, register_button):
    screen.blit(ai_settings.bg_log, (0,0))
    screen_rect = screen.get_rect()
    draw_box(screen)
    return_button.draw_button()
    register_button.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if return_button.rect.collidepoint(mouse_x, mouse_y):
        return_button.highlight_button()
    if register_button.rect.collidepoint(mouse_x, mouse_y):
        register_button.highlight_button()   

    username_box_rect = pygame.Rect(screen_rect.centerx-80, screen_rect.centery-50, 200, 30)
    password_box_rect = pygame.Rect(screen_rect.centerx-80, screen_rect.centery, 200, 30)

    if stats.username_input:
        pygame.draw.rect(screen, (220, 220, 220), username_box_rect, 0)
    else:
        pygame.draw.rect(screen, (255, 255, 255), username_box_rect, 0)      

    if stats.password_input:    
        pygame.draw.rect(screen, (220, 220, 220), password_box_rect, 0)
    else:
        pygame.draw.rect(screen, (255, 255, 255), password_box_rect, 0)        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if username_box_rect.collidepoint(mouse_x, mouse_y):
                stats.username_input = True
                stats.password_input = False
            if password_box_rect.collidepoint(mouse_x, mouse_y):
                stats.password_input = True
                stats.username_input = False
            if return_button.rect.collidepoint(mouse_x, mouse_y):
                stats.page = 'Start'
                username_box.clear()
                password_box.clear()
                stats.username_input = False
                stats.password_input = False  
            if register_button.rect.collidepoint(mouse_x, mouse_y):
                username = username_box.get_text()
                password = password_box.get_text()
                stats.user_info[username] = password
                stats.game_record[username] = [0, 0]
                username_box.clear()
                password_box.clear()
                stats.username_input = False
                stats.password_input = False 
                filename1  =  './ Information/ userInformation.json'
                with open(filename1, 'w') as f_obj:
                    json.dump(stats.user_info, f_obj)
                filename2  =  './ Information/ game_record.json'
                with open(filename2, 'w') as f_obj:
                    json.dump(stats.game_record, f_obj)

        elif event.type == pygame.KEYDOWN:
            if stats.username_input:
                username_box.key_down(event)
            if stats.password_input:
                password_box.key_down(event)

    pygame.time.delay(33)
    username_box.draw(screen)
    password_box.draw(screen)

def update_gameScreen(stats, ai_settings, screen, image_map, sb, tb, stopButton):
    screen.blit(ai_settings.bg_game, (0, 0))
    stopButton.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if stopButton.rect.collidepoint(mouse_x, mouse_y):
        stopButton.highlight_button()

    pygame.time.delay(25)
    stats.count += 25
    if stats.count == 1000:
        stats.count = 0
        stats.time += 1
        tb.prep_time()

    sb.show_score()
    tb.show_time()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            mouse_x, mouse_y = pygame.mouse.get_pos()    
            if pygame.mouse.get_pressed() == (1, 0, 0):     
                mx, my = pygame.mouse.get_pos()     
                if stopButton.rect.collidepoint(mx, my):
                    stats.game_active = False
                mx -= 130
                my -= 240
                if mx<300 and my <300:      
                    x=int(mx/100)       
                    y=int(my/100)
                    if image_map.click(x,y):
                        stats.step += 1
                        sb.prep_score()
                    if image_map.imgMap==image_map.winMap:  
                        min_step = (stats.game_record[stats.player])[0]
                        min_time = (stats.game_record[stats.player])[1]
                        if stats.step < min_step or (stats.step==min_step and stats.time<min_time) or (min_step==0 and min_time==0):
                            new_record = [stats.step, stats.time]
                            stats.game_record[stats.player] = new_record
                            filename = './Information/game_record.json'
                            with open(filename, 'w') as f_obj:
                                json.dump(stats.game_record, f_obj)
                        stats.page = 'Victory'

    for y in range(3):
        for x in range(3):
            i = image_map.imgMap[y][x]
            if i == 8:    
                continue
            dx = (i % 3) * 100      
            dy = (int(i / 3)) * 100
            screen.blit(ai_settings.pintu, (130 + x * 100, 240 + y * 100), (dx, dy, 100, 100))

def update_victoryScreen(stats, ai_settings, screen, replayButton, menuButton, time, step):
    screen.blit(ai_settings.bg_victory, (0, 0))
    replayButton.draw_button()
    menuButton.draw_button()
    time.show_msg()
    step.show_msg()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if replayButton.rect.collidepoint(mouse_x, mouse_y):
        replayButton.highlight_button()
    elif menuButton.rect.collidepoint(mouse_x, mouse_y):
        menuButton.highlight_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if replayButton.rect.collidepoint(mouse_x, mouse_y):
                stats.page = 'Game'
            elif menuButton.rect.collidepoint(mouse_x, mouse_y):
                stats.page = 'Start'

def update_stopScreen(stats, ai_settings, screen, returnButton, resetButton, closeButton):
    screen.blit(ai_settings.bg_stop, (0, 0))
    returnButton.draw_button()
    resetButton.draw_button()
    closeButton.draw_button()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if returnButton.rect.collidepoint(mouse_x, mouse_y):
        returnButton.highlight_button()
    elif resetButton.rect.collidepoint(mouse_x, mouse_y):
        resetButton.highlight_button()
    elif closeButton.rect.collidepoint(mouse_x, mouse_y):
        closeButton.highlight_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if returnButton.rect.collidepoint(mouse_x, mouse_y):
                stats.game_active = True
            elif resetButton.rect.collidepoint(mouse_x, mouse_y):
                stats.game_set = True
            elif closeButton.rect.collidepoint(mouse_x, mouse_y):
                exit()

def update_rankScreen(stats, ai_settings, screen, rkButton, rankBoard_list):
    screen.blit(ai_settings.bg_rank, (0, 0))
    for rankBoard in rankBoard_list:
        rankBoard.show_msg()
    rkButton.draw_button()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if rkButton.rect.collidepoint(mouse_x, mouse_y):
        rkButton.highlight_button()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rkButton.rect.collidepoint(mouse_x, mouse_y):
                stats.page = 'Enter'

def check_keydown_events(stats, event):
    if event.key == pygame.K_q:
        stats.page = 'Start'

def draw_box(screen):
    screen_rect = screen.get_rect()
    pygame.draw.rect(screen, (0, 0, 0), (screen_rect.centerx-200, screen_rect.centery-100, 400, 250), 1)
    font = pygame.font.SysFont('方正粗黑宋简体', 20)
    username_msg = font.render("账号", True, (0,0,0))
    password_msg = font.render("密码", True, (0,0,0))
    screen.blit(username_msg, (screen_rect.centerx-125, screen_rect.centery-50, 400, 250))
    screen.blit(password_msg, (screen_rect.centerx-125, screen_rect.centery, 400, 250))
