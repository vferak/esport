from myobject import MyObject


class Scarecrow(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Scarecrow, self).__init__(screenWidth, screenHeight, type, 90, 120)
        self.rangeY = 40
        self.attackRange = 70
        self.damage = 1.2
        self.dead = False
        self.can_be_attacked = False
        
        self.direction = 1
        self.animationWalkingRight = self.getAnimationWalking()
        self.animationAttackingRight = self.getAnimationAttacking()
        self.direction = -1
        self.animationWalkingLeft = self.getAnimationWalking()
        self.animationAttackingLeft = self.getAnimationAttacking()

        self.animationWalking = self.animationWalkingLeft
        self.animationAttacking = self.animationAttackingLeft

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

        self.speed = 6

    def getAnimationIdle(self):
        return self.getAnimationImages('scarecrow/Idle/std_', 29, 0)

    def getAnimationWalking(self):
        return self.getAnimationImages('scarecrow/Walking/walk_', 29, 0) if self.direction == 1 else self.getAnimationImages('scarecrow/Walking_left/walk_', 29, 0)
    
    def getAnimationAttacking(self):
        return self.getAnimationImages('scarecrow/Attacking/atk_', 29, 0) if self.direction == 1 else self.getAnimationImages('scarecrow/Attacking_left/atk_', 29, 0)

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
            return True
        else:
            self.speed = 3
            return True