import constants as const
from enum import Enum
from spritesheet import SpriteSheet
import pygame


class CharacterStates(Enum):
    still = 1
    jumping = 2
    moving_l = 3
    moving_r = 4
    punching_l = 5
    punching_r = 6
    kicking_l = 7
    kicking_r = 8


class Character:

    def __init__(self, sprite: str, x: int, y: int):
        if sprite == "SpriteSheet('images/chicken.png')":
            self.sprite = SpriteSheet('images/chicken.png')
            self.stand = self.sprite.get_sprite(5, 5, 60, 60)
            self.kick = self.sprite.get_sprite(5, 65, 60, 60)
            self.cross_walk = self.sprite.get_sprite(65, 5, 60, 60)
            self.jump = self.sprite.get_sprite(65, 65, 60, 60)
            self.punch = self.sprite.get_sprite(125, 5, 60, 60)
        elif sprite == SpriteSheet('images/cow.png'):
            self.sprite = SpriteSheet('images/cow.png')
            self.stand = self.sprite.get_sprite(5, 5, 60, 60)
            self.kick = self.sprite.get_sprite(5, 65, 60, 60)
            self.cross_walk = self.sprite.get_sprite(65, 5, 60, 60)
            self.jump = self.sprite.get_sprite(65, 65, 60, 60)
            self.punch = self.sprite.get_sprite(125, 5, 60, 60)

        self.x = x
        self.y = y
        self.current = self.stand
        self.last = pygame.time.get_ticks()
        self.buffer = 300

    def jumpAnimal(self):
        if self.current != self.jump:
            self.y -= const.SCALE * 4
            self.current = self.jump

    def moveAnimal(self, direction: str):
        if direction == "left":
            self.x -= const.SCALE / 2
            self.current = self.cross_walk
            self.x -= const.SCALE / 2
            self.current = self.stand

        elif direction == "right":
            self.x += const.SCALE / 2
            self.current = self.cross_walk
            self.x += const.SCALE / 2
            self.current = self.stand

    def punchAnimal(self, direction: str):
        if self.current != CharacterStates.jumping:
            if direction == "left":
                # self.x -= const.SCALE / 2
                self.current = self.punch
                # self.x += const.SCALE / 2
                # self.current = self.stand
            elif direction == "right":
                # self.x += const.SCALE / 2
                self.current = self.punch
                # self.x -= const.SCALE / 2
                # self.current = self.stand

    def kickAnimal(self, direction: str):
        if self.current != CharacterStates.jumping:
            if direction == "left":
                self.x -= const.SCALE / 2
                self.current = self.kick
                now = pygame.time.get_ticks()
                if now - self.last >= self.buffer:
                    self.last = now
                    # self.x += const.SCALE / 2
                    self.current = self.stand
            elif direction == "right":
                self.x += const.SCALE / 2
                self.current = self.kick
                now = pygame.time.get_ticks()
                if now - self.last >= self.buffer:
                    self.last = now
                    # self.x -= const.SCALE / 2
                    self.current = self.stand

    def gravity(self):
        now = pygame.time.get_ticks()
        if self.y < const.DISPLAY_H - (15 * const.SCALE) and now - self.last >= self.buffer:
            self.y += const.SCALE
        if self.y == const.DISPLAY_H - (15 * const.SCALE):
            self.last = now

    def getCurrState(self) -> pygame.Surface:
        return self.current

    def setCurrState(self, action: CharacterStates):
        self.current = action
