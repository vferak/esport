import pygame
import numpy as np
import pygame.gfxdraw
import time

from graveyard.grave_object import Grave_object
from graveyard.tile_block import Tile_block


class MyObject(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, type, objectWidth, objectHeight):
        pygame.sprite.Sprite.__init__(self)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.type = type
        self.objectWidth = objectWidth
        self.objectHeight = objectHeight
        self.direction = 0

        self.animationIdle = self.getAnimationIdle()
        self.animationWalking = self.getAnimationWalking()
        self.animationAttacking = self.getAnimationAttacking()

        self.images = self.animationIdle
        self.rect = self.images[0].get_rect()

        self.marginX = (self.rect.width - self.objectWidth) / 2
        self.marginY = (self.rect.height - self.objectHeight) / 2

        self.index = 0
        self.speed = 5

        self.inAir = False
        self.gravityMultiplier = 1.06
        self.gravity = 5
        self.maxGravity = 40
        self.currentGravity = self.gravity

        self.jumpCount = 17
        self.jumpSpeed = 13
        self.currentJump = 0

        self.boxObjectType = 'crate'

    def getAnimationIdle(self):
        return []

    def getAnimationWalking(self):
        return []
    
    def getAnimationAttacking(self):
        return []

    def getAnimationImages(self, name, frames, zerofill=3, format='.png'):
        images = []
        for i in range(0, frames):
            img = pygame.image.load(name + str(i).zfill(zerofill) + format)
            images.append(img)

        return images
    
    def getAnimationImage(self, name, format='.png'):
        images = []
        img = pygame.image.load(name + format)
        images.append(img)

        return images

    def update(self, playground, game_display):
        self.__checkCollisions(playground)
        self.index = 0 if self.index >= len(self.images) - 1 else self.index + 1
        game_display.blit(self.images[self.index], (self.rect.x, self.rect.y))

    def changeDirection(self):
        self.direction = 1 if self.direction == -1 else -1

    def moveLeft(self):
        self.speed = 5
        self.__moveOnX(-self.speed)

    def moveRight(self):
        self.speed = 5
        self.__moveOnX(+self.speed)

    def idle(self):
        self.images = self.animationIdle
        self.__applyGravity()
        
    def die(self):
        self.images = self.animationDying
        
    def attack(self):
        self.images = self.animationAttacking

    def __moveOnX(self, speed):
        self.images = self.animationWalking
        self.rect.x += speed
        self.__applyGravity()

    def jump(self):
        if not self.inAir:
            self.images = self.animationWalking
            self.inAir = True
            self.currentJump = 1
            self.__applyGravity()

    def __applyGravity(self):
        self.inAir = True
        if self.currentJump != 0:
            self.rect.y -= self.jumpSpeed
            self.currentJump += 1
        else:
            self.rect.y += self.currentGravity
        if self.currentJump == self.jumpCount:
            self.currentJump = 0
            self.currentGravity = self.gravity
        if self.currentGravity < self.maxGravity:
            self.currentGravity *= self.gravityMultiplier

    def __checkCollisions(self, playground):
        self.__checkObjectCollisions(playground)
        self.__checkBorderCollisions()

    def __checkBorderCollisions(self):
        if self.rect.x + self.marginX < 0:
            self.rect.x = 0 - self.marginX
        elif self.rect.x + self.rect.width - self.marginX > self.screenWidth:
            self.rect.x = self.screenWidth - self.rect.width + self.marginX

    def __checkObjectCollisions(self, playground):
        xCorrection = 20
        yCorrection = 40
        feetY = self.rect.height + self.rect.y - self.marginY
        leftX = self.rect.x + self.marginX + xCorrection
        rightX = self.rect.width + self.rect.x - self.marginX - xCorrection

        for obj in playground:
            if type(obj) is Tile_block and obj.type is 'tile_block' or (type(obj) is Grave_object and obj.type == self.boxObjectType):
                if leftX <= (obj.x + obj.width) and rightX >= obj.x:
                    if feetY > obj.y > feetY - yCorrection:
                        self.inAir = False
                        self.rect.y = obj.y - self.rect.height + self.marginY
                        self.currentGravity = self.gravity
                if hasattr(obj, 'hill'):
                    if leftX <= obj.hill['x'] + obj.hill['width'] and rightX >= obj.hill['x']:
                        if feetY > obj.hill['y'] > feetY - yCorrection:
                            self.inAir = False
                            self.rect.y = obj.hill['y'] - self.rect.height + self.marginY
                            self.currentGravity = self.gravity
                    elif feetY > obj.hill['y']:
                        if rightX + xCorrection > obj.hill['x'] > rightX:
                            self.rect.x = obj.hill['x'] - self.rect.width + self.marginX
                        elif leftX - xCorrection < obj.hill['x'] + obj.hill['width'] < leftX:
                            self.rect.x = obj.hill['x'] + obj.hill['width'] - self.marginX