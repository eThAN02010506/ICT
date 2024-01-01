import pygame
import sys

# 初始化 Pygame
pygame.init()

# 定义窗口大小
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Info spread')  # 更改为你的游戏名称

# 加载背景图像
background = pygame.image.load('background.jpg').convert()  # 加载背景图像
background = pygame.transform.scale(background, (width, height))  # 调整图像大小以适应窗口

# 游戏主循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制背景图像
    window.blit(background, (0, 0))  # 在窗口上绘制背景图像

    # 在这里添加其他绘制和更新游戏元素的代码

    # 更新屏幕显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
