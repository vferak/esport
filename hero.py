from myobject import MyObject


class Hero(MyObject):
    def __init__(self, screenWidth, screenHeight, type):
        super(Hero, self).__init__(screenWidth, screenHeight, type, 65, 90)

    def getAnimationIdle(self):
        return self.getAnimationImages('hero/Idle/0_Warrior_Idle Blinking_', 29)

    def getAnimationWalking(self):
        return self.getAnimationImages('hero/Walking/0_Warrior_Run_', 14)
