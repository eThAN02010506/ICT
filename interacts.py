import pygame

# 检查升级区域是否被点击的函数
def check_upgrade_area_clicked(city_rect, upgrade_area, mouse_pos):
    if city_rect.collidepoint(mouse_pos) and upgrade_area.collidepoint(mouse_pos):
        return True
    return False