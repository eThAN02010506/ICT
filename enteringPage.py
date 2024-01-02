import pygame
import sys

def show_entering_page():
    pygame.init()

    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Game Intro Page')

    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 200, 0)
    bright_green = (0, 255, 0)

    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    title_font = pygame.font.Font(None, 72)

    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def button(text, x, y, width, height, inactive_color, active_color):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pygame.draw.rect(window, active_color, (x, y, width, height))
            if click[0] == 1 and text == "Start":
                return True
        else:
            pygame.draw.rect(window, inactive_color, (x, y, width, height))

        text_surf, text_rect = text_objects(text, small_font, black)
        text_rect.center = ((x + (width / 2)), (y + (height / 2)))
        window.blit(text_surf, text_rect)

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(white)

        # Title: Info INC.
        title_surf, title_rect = text_objects("Info INC.", title_font, black)
        title_rect.center = ((window_size[0] / 2), (window_size[1] / 4))
        window.blit(title_surf, title_rect)

        # Buttons: Start and Quit
        clicked_start = button("Start", 150, 450, 100, 50, green, bright_green)
        if clicked_start:
            return True  # If "Start" is clicked, return True to main.py

        button("Quit", 550, 450, 100, 50, green, bright_green)  # Add logic for "Quit" if needed

        pygame.display.update()

    return False  # Return False if the loop exits without clicking "Start"

def ask_player_name():
    pygame.init()

    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Enter Your Name')

    white = (255, 255, 255)
    black = (0, 0, 0)

    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(250, 250, 300, 40)  # Adjusted position and size
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handling input box events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text  # Return entered text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill(white)

        # Render input box and text
        pygame.draw.rect(window, color, input_box, 2)
        text_surface = font.render(text, True, black)
        window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # Render text above the input box
        info_text = font.render("Insert the name of your info", True, black)
        text_rect = info_text.get_rect(center=(window_size[0] // 2, input_box.y - 30))  # Positioned above the input box
        window.blit(info_text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()
