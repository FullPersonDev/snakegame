import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up screen and title
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# Create snake
snake = Snake()
# Create food
food = Food()
# Create scoreboard
scoreboard = Scoreboard()

# Start screen listening events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_is_on = True
while game_is_on:
    # Refresh screen and display snake
    screen.update()
    time.sleep(0.1)

    # Print out scoreboard
    scoreboard.create_scoreboard()

    # Keep moving snake forward
    snake.move()

    # Check if snake and food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.create_scoreboard()

    # Check if collision with wall


screen.exitonclick()