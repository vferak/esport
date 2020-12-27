from myobject import MyObject
import time

class Reaper(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Reaper, self).__init__(screenWidth, screenHeight, type, 74, 100)
        self.speed = 3
        self.rangeX = 300
        self.rangeY = 10
        self.damage = 1.5
        self.attackRange = 80
        self.can_be_attacked = False
        self.dead = False
        self.hp = 1.0

        self.direction = 1
        self.animationRunningRight = self.getAnimationRunning()
        self.animationWalkingRight = self.getAnimationWalking()
        self.animationAttackingRight = self.getAnimationAttacking()
        self.direction = -1
        self.animationRunningLeft = self.getAnimationRunning()
        self.animationWalkingLeft = self.getAnimationWalking()
        self.animationAttackingLeft = self.getAnimationAttacking()

        self.animationWalking = self.animationWalkingLeft
        self.animationAttacking = self.animationAttackingLeft
        
        self.animationDying = self.getAnimationDying()

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

        self.speed = 3

    def getAnimationIdle(self):
        return self.getAnimationImages('reaper_3/Idle/0_Reaper_Man_Idle Blinking_', 17)

    def getAnimationWalking(self):
        return self.getAnimationImages('reaper_3/Walking/0_Reaper_Man_Walking_', 23) if self.direction == 1 else self.getAnimationImages('reaper_3/Walking_left/0_Reaper_Man_Walking_', 23)

    def getAnimationRunning(self):
        return self.getAnimationImages('reaper_3/Running/0_Reaper_Man_Running_', 11) if self.direction == 1 else self.getAnimationImages('reaper_3/Running_left/0_Reaper_Man_Running_', 11)
    
    def getAnimationAttacking(self):
        return self.getAnimationImages('reaper_3/Attacking/0_Reaper_Man_Slashing_', 11) if self.direction == 1 else self.getAnimationImages('reaper_3/Attacking_left/0_Reaper_Man_Slashing_', 11)
    
    def getAnimationDying(self):
        return self.getAnimationImage('reaper_3/Dying/0_Reaper_Man_Dying_014')


    def move(self, hero):
        do_move = self.checkHero(hero)
        if do_move == True:
            if self.direction == 1:
                if self.rect.x + self.rect.width - self.marginX < self.rightEdge:
                    self.moveRight()
                else:
                    self.changeDirection()
                    self.animationWalking = self.animationWalkingLeft
            elif self.direction == -1:
                if self.rect.x + self.marginX > self.leftEdge:
                    self.moveLeft()
                else:
                    self.changeDirection()
                    self.animationWalking = self.animationWalkingRight
                
    def attackEnemy(self, hero):
        if self.direction == 1:
            self.animationAttacking = self.animationAttackingRight
        else:
            self.animationAttacking = self.animationAttackingLeft
        self.attack()
        if hero.dead == False:
            hero.hp -= self.damage
            hero.checkDead()

    def checkHero(self,hero):
        if self.rect.y - self.rangeY <= hero.rect.y <= self.rect.y + self.rangeY:
            if hero.rect.x - hero.attackRange <= self.rect.x <= hero.rect.x + hero.attackRange:
                self.can_be_attacked = True
                
            if self.rect.x + self.rangeX >= hero.rect.x > self.rect.x + self.attackRange:
                self.direction = 1
                self.animationWalking = self.animationRunningRight
                self.speed = 5
                self.can_be_attacked = False

            elif self.rect.x - self.rangeX <= hero.rect.x < self.rect.x - self.attackRange:
                self.direction = -1
                self.animationWalking = self.animationRunningLeft
                self.speed = 5
                self.can_be_attacked = False
    
            elif self.rect.x < hero.rect.x < self.rect.x + self.attackRange:
                self.speed = 0
                self.attackEnemy(hero)
                return False
                
            elif self.rect.x > hero.rect.x > self.rect.x - self.attackRange:
                self.speed = 0
                self.attackEnemy(hero)
                return False

            else:
                self.speed = 3
                self.can_be_attacked = False
            return True
        else:
            self.speed = 3
            self.can_be_attacked = False
            return True
        
    def checkDead(self):
        if self.hp <= 0:
            self.animationDying = self.getAnimationDying()
            self.hp = 0
            self.dead = True
            self.die()