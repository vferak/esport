from myobject import MyObject


class Scarecrow(MyObject):
    def __init__(self, screenWidth, screenHeight, type, leftEdge, rightEdge):
        super(Scarecrow, self).__init__(screenWidth, screenHeight, type, 90, 120)
        self.speed = 3

        self.direction = 1
        self.animationWalkingRight = self.getAnimationWalking()
        self.direction = -1
        self.animationWalkingLeft = self.getAnimationWalking()

        self.animationWalking = self.animationWalkingLeft

        self.leftEdge = leftEdge
        self.rightEdge = rightEdge

    def getAnimationIdle(self):
        return self.getAnimationImages('scarecrow/Idle/std_', 29, 0)

    def getAnimationWalking(self):
        return self.getAnimationImages('scarecrow/Walking/walk_', 29, 0) if self.direction == 1 else self.getAnimationImages('scarecrow/Walking_left/walk_', 29, 0)

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
