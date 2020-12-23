from myobject import MyObject


class Reaper(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Reaper, self).__init__(screenWidth, screenHeight, type, 74, 100)
        self.speed = 3
        self.rangeX = 300
        self.rangeY = 100

        self.direction = 1
        self.animationRunningRight = self.getAnimationRunning()
        self.animationWalkingRight = self.getAnimationWalking()
        self.direction = -1
        self.animationRunningLeft = self.getAnimationRunning()
        self.animationWalkingLeft = self.getAnimationWalking()

        self.animationWalking = self.animationWalkingLeft

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

    def getAnimationIdle(self):
        return self.getAnimationImages('reaper_3/Idle/0_Reaper_Man_Idle Blinking_', 17)

    def getAnimationWalking(self):
        return self.getAnimationImages('reaper_3/Walking/0_Reaper_Man_Walking_', 23) if self.direction == 1 else self.getAnimationImages('reaper_3/Walking_left/0_Reaper_Man_Walking_', 23)

    def getAnimationRunning(self):
        return self.getAnimationImages('reaper_3/Running/0_Reaper_Man_Running_', 11) if self.direction == 1 else self.getAnimationImages('reaper_3/Running_left/0_Reaper_Man_Running_', 11)

    def move(self, hero):
        self.checkHero(hero)
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

    def checkHero(self,hero):
        if self.rect.y - self.rangeY <= hero.rect.y <= self.rect.y + self.rangeY:
            if hero.rect.x <= self.rect.x + self.rangeX and hero.rect.x > self.rect.x:
                self.direction = 1
                self.animationWalking = self.animationRunningRight
                self.speed = 5

            elif hero.rect.x >= self.rect.x - self.rangeX and hero.rect.x < self.rect.x:
                self.direction = -1
                self.animationWalking = self.animationRunningLeft
                self.speed = 5
            else:
                self.speed = 3
        else:
            self.speed = 3
