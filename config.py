import pygame

# 屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 玩家模型
PLAYER_IMAGE = "images/hero1.png"

# 敌机模型
ENEMY_IMAGE = "images/enemy-1.gif"

# 子弹模型
BULLET_IMAGE = "images/bullet-3.gif"

# 背景图片
BG_IMAGE = "images/background.png"

# 

# 刷新的帧率
FPS = 60

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件
PLAYER_FIRE_EVENT = pygame.USEREVENT + 1
