from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from CTkMessagebox import CTkMessagebox
import time


class AppBrain:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.colormode(255)
        self.screen.bgcolor(128, 223, 255)
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.screen.listen()
        self.screen.onkey(fun=self.snake.up, key="Up")
        self.screen.onkey(fun=self.snake.down, key="Down")
        self.screen.onkey(fun=self.snake.left, key="Left")
        self.screen.onkey(fun=self.snake.right, key="Right")

    def game(self):
        """ Game rules"""
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            self.ate_food()
            self.wall_collision()
            self.teil_collision()

    def start(self):
        """ Starting with the question """
        msg = CTkMessagebox(title="Snake Game?", message="Start Game?",
                            icon="icons/start_icon.png", option_1="No", option_2="Yes")
        response = msg.get()
        
        if response=="Yes": 
            self.game()      
        else:
            self.screen.bye()

    def ask_restart(self):
        """ Ask to restart if user lose """
        msg = CTkMessagebox(title="Snake Game", message="Do you want to restart the Game?",
                            icon="icons/refresh_icon.png", option_1="No", option_2="Yes")
        response = msg.get()
        
        if response=="Yes": 
            self.scoreboard.reset()
            self.snake.reset()
            self.food.refresh()  
            self.game()    
        else:
            self.screen.bye()

    def wall_collision(self):
        """ Detect collision with wall """
        if self.snake.head.xcor() > 290 or self.snake.head.xcor() < -290 or self.snake.head.ycor() > 290 or self.snake.head.ycor() < -290:
            self.ask_restart()

    def teil_collision(self):
        """ Detect collision with tail """
        for segment in self.snake.segments:
                if segment == self.snake.head:
                    pass
                elif self.snake.head.distance(segment) < 10:
                    self.ask_restart()

    def ate_food(self):
        """ Detect eaten food """
        if self.snake.head.distance(self.food) < 15:
                self.food.refresh()
                self.snake.extend()
                self.scoreboard.increase_score()
