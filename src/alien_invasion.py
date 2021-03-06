import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # 初始化游戏并创建一个screen对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视鼠标和键盘事件
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船
        ship.update()

        # 更新子弹
        gf.update_bullets(aliens, bullets)

        # print(len(bullets)) 检验是否成功删除了消失的子弹

        # 更新飞船
        gf.update_aliens(ai_settings, aliens)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
