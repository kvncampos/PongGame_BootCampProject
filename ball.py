from turtle import Turtle

# Sets the Motion of the Ball. Global Variable.
X_MOVE = 1
Y_MOVE = 1


class Ball(Turtle):

    def __init__(self):
        """Creates a White Ball in the Center of the Field."""
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.goto(0, 0)
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        """Sets the Motion of the Ball. Detects Top and Bottom Boundaries"""
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Ball Bounces off Top/Bottom Walls on Collision"""
        self.y_move *= -1

    def bounce_x(self):
        """Ball Bounces off Paddles on Collision"""
        self.x_move *= -1
        self.move_speed *= 0.25

    def reset_position(self):
        """Ball Resets on Miss."""
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()

    def paddles_test(self):
        """This is to Test the Interaction of the paddles."""
        global X_MOVE
        # This is to Test the interaction of 'Paddles'.
        if self.xcor() >= 330:
            print(f"HIT East WALL {self.pos()}")
            x_move = -1

        if self.xcor() <= -10:
            # print(f"HIT West WALL {self.pos()}")
            X_MOVE = 1
