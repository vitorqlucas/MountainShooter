#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        # Movimento contínuo para efeito de parallax
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:  # Reinicia a posição quando sai da tela
            self.rect.left = WIN_WIDTH
