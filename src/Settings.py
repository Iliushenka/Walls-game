import pygame
pygame.init()

"""

    Данный файл отвечает за настройку игры в целом
    Не рекомендуется изменять данный файл, так как могут появиться баги
    Данный файл обязательно импортировать

    Здесь находятся константы, они обозначаются заглавными буквами

"""

WIDTH, HEIGHT = 1000, 600
FPS = 60
SPEED_MONEY = 200
COST_DEFENDER = 20

STANDARD_BASE_HP = 10

'''
    Константы для игры
'''
NONE = "None"
ENEMY = "Enemy"
DEFENDER = "Defender"
MENU = "Menu"
GAME = "Game"
DEATH = "Death"
ENEMY_WIN = "Enemy win"
DEFENDER_WIN = "Defender win"

'''
    Функции кнопок
'''
B_NONE = None
B_CLOSE = "CLOSE"
B_START_GAME = "START GAME"
B_BUY_DEFENDER = "BUY DEFENDER"

'''
    Шрифты константы
'''
FONT_GAME = pygame.font.Font("../fonts/bit.ttf", 50)
FONT_PRESS_ESC = pygame.font.Font("../fonts/bit.ttf", 20)

'''
    Текстовые константы
'''
TEXT_PAUSE = FONT_GAME.render("PAUSE", True, (255, 255, 255))
TEXT_PRESS_ESC = FONT_PRESS_ESC.render("Press esc", True, (255, 255, 255))
TEXT_START_GAME = FONT_PRESS_ESC.render("Start game", True, (255, 255, 255))