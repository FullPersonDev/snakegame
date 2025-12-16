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

    # Initial print scoreboard
    scoreboard.create_scoreboard()

    # Keep moving snake forward
    snake.move()

    # Check if collision with food
    if snake.head.distance(food) < 15:
        # Refresh food location, add to scoreboard and reprint it
        food.refresh()
        snake.extend()
        scoreboard.score += 1
        scoreboard.create_scoreboard()

    # Check if collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False

    # Check if collision with tail
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
