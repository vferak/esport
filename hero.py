from myobject import MyObject


class Hero(MyObject):
    def __init__(self, screenWidth, screenHeight, type):
        super(Hero, self).__init__(screenWidth, screenHeight, type, 65, 90)
        self.hp = 180.0
        self.attackRange = 100
        self.attacking = False
        self.dead = False
        
        self.enemy_list = []
        
    def getAnimationIdle(self):
        return self.getAnimationImages('hero/Idle/0_Warrior_Idle Blinking_', 29)

    def getAnimationWalking(self):
        return self.getAnimationImages('hero/Walking/0_Warrior_Run_', 14)
    
    def getAnimationAttacking(self):
        return self.getAnimationImages('hero/Attacking/0_Warrior_Attack_2_', 14)
    
    def getAnimationDying(self):
        return self.getAnimationImages('hero/Dying/0_Warrior_Died_', 29)

    def attackEnemy(self):
        self.attacking = True
        self.speed = 0
        self.animationAttacking = self.getAnimationAttacking()
        self.attack()
        
        for enemy in self.enemy_list:
            if enemy.dead == False and enemy.can_be_attacked == True:
                enemy.dead = True
                enemy.hp -= 1
                enemy.checkDead()
        
    def checkDead(self):
        if self.hp <= 0:
            self.animationDying = self.getAnimationDying()
            self.hp = 0
            self.dead = True
            self.die()