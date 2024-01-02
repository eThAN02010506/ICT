import pygame
import sys
import enteringPage
from city_data import city_population, city_spread_rates
from algorithm import calculate_affected_population
from city_functions import calculate_city_affected_population

def main_game_logic(player_name):
    pygame.init()

    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Info spread')

    background = pygame.image.load('Graphics/下载 (1).jpeg').convert()  # 修改为背景图的路径
    background = pygame.transform.scale(background, (width, height))

    elapsed_time = 0
    upgrade_point = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elapsed_time += 1
        upgrade_point, total_population = calculate_city_affected_population(elapsed_time, upgrade_point)

        total_affected_population = 0
        for city in city_population:
            spread_rate = city_spread_rates[city]
            affected_population, _ = calculate_affected_population(city_population[city], spread_rate, elapsed_time, 0)
            total_affected_population += affected_population

        window.blit(background, (0, 0))  # 显示背景图

        font = pygame.font.Font(None, 24)
        text_total_population = font.render(f"Total Population: {total_population}", True, (255, 255, 255))
        text_total_affected = font.render(f"Total Affected Population: {total_affected_population:.0f}", True, (255, 255, 255))

        text_total_population_rect = text_total_population.get_rect()
        text_total_population_rect.topright = (width - 10, 10)
        window.blit(text_total_population, text_total_population_rect)

        text_total_affected_rect = text_total_affected.get_rect()
        text_total_affected_rect.topright = (width - 10, 40)
        window.blit(text_total_affected, text_total_affected_rect)

        # 其他游戏逻辑...

        pygame.display.flip()

def start():
    clicked_start = enteringPage.show_entering_page()
    if clicked_start:
        player_name = enteringPage.ask_player_name()
        if player_name:
            main_game_logic(player_name)

if __name__ == "__main__":
    start()
