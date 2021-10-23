from GameSprite import *
from config import *
from Bullet import *

class Player(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类方法,创建英雄精灵,同时指定敌机图片和速度
        super().__init__(PLAYER_IMAGE, 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("发射子弹...")

        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置精灵位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx

            # 将子弹精灵添加到子弹精灵组
            self.bullets.add(bullet)