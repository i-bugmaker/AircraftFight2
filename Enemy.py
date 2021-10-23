from GameSprite import *
from config import *
import random

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 调用父类方法,创建敌机精灵,同时指定敌机图片
        super().__init__(ENEMY_IMAGE)
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 调用父类方法, 保持垂直方向飞行
        super().update()

        # 判断是否非处屏幕, 如果是, 需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕,删除...")

            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)