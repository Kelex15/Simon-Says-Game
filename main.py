from tkinter import *
import random

# Constants
BUTTON_WIDTH = 20
BUTTON_HEIGHT = 10
FONT = ("Times", 15, "normal")

# Global Variables
stage = 0
selected_button_sequence = []
button_position = 0
game_over_ = False
no_of_button_pressed = 0
shown_buttons = 0
color = ""


def game_over():
    """
    Stores and displays the player's score and also the correct button
    :return: None
    """
    global no_of_button_pressed, button_position, shown_buttons, stage, game_over_
    game_over_ = True
    score = stage-1
    stage = 0
    pressed_ = color
    try:
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
    except FileNotFoundError:
        with open("high_score.txt", "w") as _:
            high_score = 0

    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as f:
            f.write(f"{high_score}")

    check_color(selected_button_sequence[no_of_button_pressed-1])
    correct = color

    level_label.config(text=f"Game Over\nScore: {score}\nBest: {high_score}\nPressed: {pressed_}\n"
                            f"Correct: {correct}")
    no_of_button_pressed = 0
    button_position = 0
    shown_buttons = 0
    start_button.config(text="Play again")


def check_color(button_selected: Button):
    """
    Checks the color of the selected button and sets the global color variable to the color
    :param button_selected: tkinter button
    :return: None
    """
    global color
    if str(button_selected) == ".!button":
        button_selected.config(bg="green")
        color = "Green"
    elif str(button_selected) == ".!button2":
        button_selected.config(bg="red")
        color = "Red"
    elif str(button_selected) == ".!button3":
        button_selected.config(bg="blue")
        color = "Blue"
    elif str(button_selected) == ".!button4":
        button_selected.config(bg="yellow")
        color = "Yellow"


def white():
    """
    Changes the color of the button when it is pressed
    :return: None
    """
    global shown_buttons
    shown_buttons += 1
    button = selected_button_sequence[shown_buttons-1]
    button.config(bg="white")
    window.after(1000, check_color, button)
    if shown_buttons < len(selected_button_sequence):
        window.after(1200, white)


def start():
    global game_over_
    game_over_ = False
    selected_button_sequence.clear()
    game_play()


def game_play():
    global no_of_button_pressed, button_position, shown_buttons, stage
    stage += 1
    level_label.config(text=f"Stage: {stage}")
    no_of_button_pressed = 0
    button_position = 0
    shown_buttons = 0
    button_list = [green_button, red_button, yellow_button, blue_button]
    button_selected = random.choice(button_list)
    selected_button_sequence.append(button_selected)
    window.after(500, white)


def pressed(button_color):
    global button_position, no_of_button_pressed
    if game_over_:
        return
    else:
        check_color(button_color)
    if no_of_button_pressed == len(selected_button_sequence):
        return
    no_of_button_pressed += 1

    if button_color == selected_button_sequence[button_position]:
        button_position += 1
        if no_of_button_pressed == len(selected_button_sequence):
            game_play()
    else:
        game_over()


def green_pressed():
    pressed(green_button)


def red_pressed():
    pressed(red_button)


def blue_pressed():
    pressed(blue_button)


def yellow_pressed():
    pressed(yellow_button)


# --------------------- GUI SETUP --------------------- #
window = Tk()
window.title("Simon Say's Game")
window.config(padx=30, pady=10, bg="black")

level_label = Label(text=f"Stage: {stage}", bg="black", fg="white", font=FONT)
level_label.grid(row=0, column=0, columnspan=2, pady=10, sticky=W+E)

green_button = Button(text="Green", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg="green", command=green_pressed)
green_button.grid(row=1, column=0, padx=10, pady=10, sticky=W+E)
red_button = Button(text="Red", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg="red", command=red_pressed)
red_button.grid(row=1, column=1, padx=10, pady=10, sticky=W+E)
blue_button = Button(text="Blue", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg="blue", command=blue_pressed)
blue_button.grid(row=2, column=0, padx=10, pady=10, sticky=W+E)
yellow_button = Button(text="Yellow", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, bg="yellow", command=yellow_pressed)
yellow_button.grid(row=2, column=1, padx=10, pady=10, sticky=W+E)
start_button = Button(text="Start", font=FONT, command=start)
start_button.grid(row=3, column=0)
quit_button = Button(text="Quit", font=FONT, command=quit)
quit_button.grid(row=3, column=1)

window.mainloop()
