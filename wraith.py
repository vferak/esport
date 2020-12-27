from myobject import MyObject


class Wraith(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Wraith, self).__init__(screenWidth, screenHeight, type, 60, 85)
        self.hp = 1.0
        self.rangeY = 40
        self.attackRange = 70
        self.damage = 1
        self.dead = False
        self.can_be_attacked = False
        
        self.direction = -1
        self.animationWalkingLeft = self.getAnimationWalking()
        self.animationAttackingLeft = self.getAnimationAttacking()
        self.direction = 1
        self.animationWalkingRight = self.getAnimationWalking()
        self.animationAttackingRight = self.getAnimationAttacking()

        self.animationWalking = self.animationWalkingRight
        self.animationDying = self.getAnimationDying()

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

        self.speed = 3

    def getAnimationIdle(self):
        return self.getAnimationImages('enemy_wraith_1/Idle/Wraith_01_Idle Blinking_', 11)

    def getAnimationWalking(self):
        return self.getAnimationImages('enemy_wraith_1/Walking/Wraith_01_Moving Forward_', 11) if self.direction == 1 else self.getAnimationImages('enemy_wraith_1/Walking_left/Wraith_01_Moving Forward_', 11)

    def getAnimationAttacking(self):
        return self.getAnimationImages('enemy_wraith_1/Attacking/Wraith_01_Attack_', 11) if self.direction == 1 else self.getAnimationImages('enemy_wraith_1/Attacking_left/Wraith_01_Attack_', 11)
    
    def getAnimationDying(self):
        return self.getAnimationImage('enemy_wraith_1/Dying/Wraith_01_Dying_014')
    
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
            if self.rect.x < hero.rect.x < self.rect.x + self.attackRange:
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

