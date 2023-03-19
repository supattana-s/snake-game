from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.update_board()

    def get_score(self):
        self.score += 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_board()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT)
