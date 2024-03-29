import pygame
from hero import Hero
from wraith import Wraith
from reaper import Reaper
from scarecrow import Scarecrow
from graveyard.tile_block import Tile_block
from graveyard.grave_object import Grave_object
from numpy import math



class Playground:
    def __init__(self):
        """
        Constructor
        """
        self.width = 1920
        self.height = 1080
        self.background = pygame.image.load('background/PNG/2_game_background/2_game_background.png')
        self.playground = self.create_playground()

    def create_playground(self):
        """
        Generates the playground with the tiles and graveyard objects
        """
        my_playground = []

        my_playground.append(Tile_block(0, self.height - 100, 0))  # Ground
        my_playground.append(Tile_block(450, 600, 3))  # Island with dead bushes
        my_playground.append(Tile_block(0, 450, 2))  # I sland on the left
        my_playground.append(Tile_block(500, 300, 6))  # Island in the middle
        my_playground.append(Tile_block(1280, 350, 4))  # Island on the right (top)
        my_playground.append(Tile_block(800, 700, 3))  # Island on the right (middle)

        # Graveyard objects - trees, tombstones, sign arrows, bushes, bones
        my_playground.append(Grave_object(800, 215, 8))
        my_playground.append(Grave_object(500, 65, 9))
        my_playground.append(Grave_object(900, 65, 9))
        my_playground.append(Grave_object(1200, 120, 9))
        my_playground.append(Grave_object(1620, 120, 9))
        my_playground.append(Grave_object(1450, 280, 11))
        my_playground.append(Grave_object(1550, 280, 11))
        my_playground.append(Grave_object(1650, 280, 11))
        my_playground.append(Grave_object(1170, self.height - 205, 13))
        my_playground.append(Grave_object(1400, 800, 1))
        my_playground.append(Grave_object(1350, 900, 3))
        my_playground.append(Grave_object(200, 890, 8))
        my_playground.append(Grave_object(100, 370, 5))
        my_playground.append(Grave_object(10, 410, 14))
        my_playground.append(Grave_object(500, self.height - 160, 6))
        my_playground.append(Grave_object(700, self.height - 160, 6))
        my_playground.append(Grave_object(550, self.height - 180, 5))
        my_playground.append(Grave_object(1400, self.height - 590, 9))
        my_playground.append(Grave_object(1300, self.height - 420, 7))
        my_playground.append(Grave_object(1450, self.height - 405, 10))
        my_playground.append(Grave_object(1700, self.height - 205, 13))
        my_playground.append(Grave_object(550, self.height - 570, 12))
        my_playground.append(Grave_object(600, self.height - 550, 7))
        my_playground.append(Grave_object(450, self.height - 550, 7))

        return my_playground

    def show_playground(self, game_display):
        """
        Display plaground
        @param game_display: gpygame.display
        """
        for my_obj in self.playground:
            my_obj.show(game_display)

    def run(self, enemy_types):
        """
        Main loop of the application
        @param enemy_types:
        """
        clock = pygame.time.Clock()
        pygame.font.init()
        pygame.init()
        game_display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Halloween Party')
        hero = Hero(self.width, self.height, 0)
        hero.rect.x = 800
        hero.rect.y = 10

        wraith1 = Wraith(self.width, self.height, 0, 0, 400)
        wraith1.rect.x = 0
        wraith1.rect.y = 100

        wraith2 = Wraith(self.width, self.height, 0, 0, 1280)
        wraith2.rect.x = 500
        wraith2.rect.y = self.height - 200

        scarecrow = Scarecrow(self.width, self.height, 0, 1280, 1664)
        scarecrow.rect.x = 1550
        scarecrow.rect.y = 600

        reaper = Reaper(self.width, self.height, 0, 1280, self.width)
        reaper.rect.x = self.width - 100
        reaper.rect.y = 50

        moveLeft = 0
        moveRight = 0
        
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        
        hero.enemy_list.append(wraith1)
        hero.enemy_list.append(wraith2)
        hero.enemy_list.append(reaper)
        
        while True:
            textsurface = myfont.render(str(hero.hp), False, (255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and hero.dead == False:
                    if event.key == pygame.K_a:
                        moveLeft = moveRight + 1
                    elif event.key == pygame.K_d:
                        moveRight = moveLeft + 1

                    if event.key == pygame.K_w:
                        hero.jump()
                        
                    if event.key == pygame.K_SPACE:
                        hero.attackEnemy()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        moveLeft = 0
                    elif event.key == pygame.K_d:
                        moveRight = 0
                    elif event.key == pygame.K_SPACE:
                        hero.attacking = False

            if moveLeft == 0 and moveRight == 0 and hero.attacking == False and hero.dead == False:
                hero.idle()
            elif moveLeft > moveRight:
                hero.moveLeft()
            elif moveRight > moveLeft:
                hero.moveRight()

            if reaper.dead == False:
                reaper.move(hero)
            if wraith1.dead == False:
                wraith1.move(hero)
            else:
                wraith1.die()
            if wraith2.dead == False:
                wraith2.move(hero)
            else:
                wraith2.die()
                
            scarecrow.move(hero)

            game_display.blit(self.background, [0, 0])  # Display background
            self.show_playground(game_display)  # Show playground

            wraith1.update(self.playground, game_display)
            wraith2.update(self.playground, game_display)
            scarecrow.update(self.playground, game_display)
            reaper.update(self.playground, game_display)
            hero.update(self.playground, game_display)
            
            if hero.dead == False:
                textsurface = myfont.render('HP:  ' + str(math.ceil(hero.hp / 30)), False, (255, 255, 255))
                game_display.blit(textsurface,(20,self.height - 70))
            else:
                textsurface = myfont.render('YOU DIED', False, (255, 0, 0))
                game_display.blit(textsurface,(self.width / 2 - 100, self.height / 2 - 30))

            pygame.display.update()  # Update of the screen
            clock.tick(60)


if __name__ == '__main__':
    enemy_types = [3, 2, 4, 5]
    pg = Playground()
    pg.run(enemy_types)
