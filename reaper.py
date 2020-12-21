from myobject import MyObject


class Reaper(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Reaper, self).__init__(screenWidth, screenHeight, type, 74, 100)
        self.direction = 1
        self.animationWalkingRight = self.getAnimationWalking()
        self.direction = -1
        self.animationWalkingLeft = self.getAnimationWalking()

        self.animationWalking = self.animationWalkingLeft

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

    def getAnimationIdle(self):
        return self.getAnimationImages('reaper_3/Idle/0_Reaper_Man_Idle Blinking_', 17)

    def getAnimationWalking(self):
        return self.getAnimationImages('reaper_3/Walking/0_Reaper_Man_Walking_', 23) if self.direction == 1 else self.getAnimationImages('reaper_3/Walking_left/0_Reaper_Man_Walking_', 23)

    def move(self):
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