import turtle

def koch_snowflake(turtle, iterations, length):
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.right(120)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)

def draw_snowflake(turtle, iterations, length):
    for i in range(3):
        koch_snowflake(turtle, iterations, length)
        turtle.right(120)

# Create turtle screen and turtle
screen = turtle.Screen()
flake_turtle = turtle.Turtle()
flake_turtle.speed(0)  # fastest drawing speed
arColors =  ["blue","green", "yellow", "orange", "red", "purple"]
flake_turtle.penup()
flake_turtle.goto(-350,250)
flake_turtle.pendown()
flake_turtle.pensize(2)
# Draw the Koch Snowflake
for intLevel in range(4,0,-1):
    flake_turtle.color(arColors[intLevel], arColors[intLevel])
    flake_turtle.begin_fill()
    draw_snowflake(flake_turtle, intLevel, 600)  # You can experiment with different iterations and lengths
    flake_turtle.end_fill()
# Close the window on click
screen.exitonclick()



#
# import turtle
#
# # User-definable variables
# initial_length = 100  # Initial length of the branch
# angle = 20            # Angle of the branching
# decrease_factor = 0.70 # Factor by which branch length decreases
#
# def draw_branch(turtle, branch_length):
#     if branch_length > 5:
#         # Draw the branch
#         turtle.forward(branch_length)
#         # Right branch
#         turtle.right(angle)
#         draw_branch(turtle, branch_length * decrease_factor)
#         # Left branch
#         turtle.left(2 * angle)
#         draw_branch(turtle, branch_length * decrease_factor)
#         # Return to base position
#         turtle.right(angle)
#         turtle.backward(branch_length)
#
# # Set up the turtle
# screen = turtle.Screen()
# my_turtle = turtle.Turtle()
# my_turtle.left(90)  # Point the turtle upwards
# my_turtle.up()
# my_turtle.backward(100)
# my_turtle.down()
# my_turtle.speed(1)
#
# # Draw the fractal tree
# draw_branch(my_turtle, initial_length)
#
# # Close the window on click
# screen.exitonclick()
