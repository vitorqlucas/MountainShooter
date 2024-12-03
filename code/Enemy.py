#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade inicial no eixo Y

    def move(self):
        # Movimento horizontal (da direita para a esquerda)
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Comportamento especial para Enemy3
        if self.name == "Enemy3":
            # Movimento vertical (subindo e descendo)
            self.rect.centery += self.vertical_speed

            # Checa borda inferior
            if self.rect.bottom >= WIN_HEIGHT:
                self.vertical_speed = -ENTITY_SPEED[self.name]  # Inverte para subir

            # Checa borda superior
            elif self.rect.top <= 0:
                self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Desce com o dobro da velocidade

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Retorna um tiro exclusivo para cada inimigo
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
