from GameSprite import *
from config import *


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        # 调用父类方法实现精灵创建
        super().__init__(BG_IMAGE)
        # 判断是否是交替图像, 如果是, 需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 调用父类的update方法
        super().update()

        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
