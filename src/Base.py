import pygame
from Settings import *


'''

    Данный класс нужен для инициализации башен и взаимодействия с ними!
    Класс требуется в улучшениях

'''

class Base:
    def __init__(self, x, y, width, height):
        self.hp = STANDARD_BASE_HP

        self.x, self.y = x, y
        self.WIDTH, self.HEIGHT = width, height

        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)


class EnemyBase(Base):
    def __init__(self):
        super().__init__(WIDTH - 100, HEIGHT - 300, 100, 200)

    def attack_me(self, attack):
        if self.hp > 0:
            self.hp -= attack
        else:
            return DEFENDER_WIN
        return NONE


class DefenderBase(Base):
    def __init__(self):
        super().__init__(0, HEIGHT - 300, 100, 200)

    def attack_me(self, attack):
        if self.hp > 0:
            self.hp -= attack
        else:
            return ENEMY_WIN
        return NONE
