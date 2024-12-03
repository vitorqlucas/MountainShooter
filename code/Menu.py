#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70), align='center')
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120), align='center')

            # Renderize o nome e o RU no canto superior esquerdo
            self.menu_text(15, "Alunos:", C_WHITE, (4, 4), align='left')
            self.menu_text(15, "Juliana Trindade Vicentim - RU: 4348733", C_WHITE, (4, 16), align='left')
            self.menu_text(15, "Poliana Gabriele Brandani da Silva - RU: 4381444", C_WHITE, (4, 28), align='left')
            self.menu_text(15, "Vitor Quintanilha Lucas - RU: 4497445", C_WHITE, (4, 40), align='left')

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i), align='center')
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i), align='center')
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, align: str = 'center'):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        if align == 'center':
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        elif align == 'left':
            text_rect: Rect = text_surf.get_rect(topleft=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
