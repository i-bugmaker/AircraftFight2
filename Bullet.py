from GameSprite import *
from config import *

class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__(BULLET_IMAGE, -2)

    def update(self):

        # 调用父类方法, 让子弹垂直移动
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")