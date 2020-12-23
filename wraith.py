from myobject import MyObject


class Wraith(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Wraith, self).__init__(screenWidth, screenHeight, type, 60, 85)
        self.speed = 3

        self.direction = -1
        self.animationWalkingLeft = self.getAnimationWalking()
        self.direction = 1
        self.animationWalkingRight = self.getAnimationWalking()

        self.animationWalking = self.animationWalkingRight

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

    def getAnimationIdle(self):
        return self.getAnimationImages('enemy_wraith_1/Idle/Wraith_01_Idle Blinking_', 11)

    def getAnimationWalking(self):
        return self.getAnimationImages('enemy_wraith_1/Walking/Wraith_01_Moving Forward_', 11) if self.direction == 1 else self.getAnimationImages('enemy_wraith_1/Walking_left/Wraith_01_Moving Forward_', 11)

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

