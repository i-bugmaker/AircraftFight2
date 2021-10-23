from config import *
from AircraftFightGame import *
from Player import *
from BackGround import *
from Enemy import *
import pygame


class AircraftFightGame(object):
    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法,精灵和精灵组的创建
        self.__creat_sprites()

        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(PLAYER_FIRE_EVENT, 500)

    def __creat_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄精灵和英雄精灵组
        self.player = Player()
        self.player_group = pygame.sprite.Group(self.player)

    def start_game(self):
        print("游戏开始")
        while True:
            # 设置刷新帧率
            self.clock.tick(FPS)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                AircraftFightGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场>>>")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == PLAYER_FIRE_EVENT:
                self.player.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
        # 持续移动
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("向右移动")
            self.player.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.player.speed = -2
        else:
            self.player.speed = 0

    def __check_collide(self):

        # 子弹摧毁敌机
        pygame.sprite.groupcollide(
            self.player.bullets, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(
            self.player, self.enemy_group, True)

        # 判断列表是否有内容
        if len(enemies) > 0:

            #     # 英雄牺牲
            self.player.kill()
        #     # 结束游戏
            AircraftFightGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.player_group.update()
        self.player_group.draw(self.screen)
        self.player.bullets.update()
        self.player.bullets.draw(self.screen)

    @staticmethod
    def __game_over(self):
        print("游戏结束")
        pygame.quit()
        exit()
