import turtle
import pandas
#  make screen of the game
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# read data from stats file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# we have a 50 the while repeat intel we complete all states

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    #  if user choose exit
    if answer_state == "Exit":
        # clean missing states
        missing_states = []
        for state in all_states:
            # if user choose state not in all states the missing state go to another list called missing_states
            if state not in guessed_states:
                missing_states.append(state)
        # make file for missing stats and finishing system
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # check if stat in stats
        guessed_states.append(answer_state)
        # The Turtle module is commonly used in Python for drawing shapes and graphics.
        t = turtle.Turtle()
        # This line hides the turtle cursor so that it won't be visible on the screen.
        t.hideturtle()
        # moving the turtle will not draw lines on the screen
        t.penup()
        # This line filters the data DataFrame to find the row where the state column matches answer_state.
        # state_data will be a DataFrame containing only the row of the matched state.
        state_data = data[data.state == answer_state]
        # moves the turtle to the coordinates specified by the x and y columns of state_data
        t.goto(int(state_data.x), int(state_data.y))
        # writes the name of the answer_state at the turtle's current position on the screen.
        t.write(answer_state)
