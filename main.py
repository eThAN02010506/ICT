import pygame
import sys
import enteringPage

def main_game_logic(player_name):
    pygame.init()

    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Info spread')

    background = pygame.image.load('/Users/ethanjiang/PycharmProjects/ICT roject/Graphics/下载 (1).jpeg').convert()
    background = pygame.transform.scale(background, (width, height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.blit(background, (0, 0))  # Draw the background

        # Display the player's name on the screen
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"Info Name: {player_name}", True, (255, 255, 255))
        window.blit(text_surface, (10, 10))  # Adjust the position if needed

        pygame.display.flip()

def start():
    clicked_start = enteringPage.show_entering_page()
    if clicked_start:
        player_name = enteringPage.ask_player_name()
        if player_name:
            main_game_logic(player_name)

if __name__ == "__main__":
    start()
