# Importing packages
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Creating the window for the main menu
root = Tk()
root.title("Recycling or Rubbish?")
root.geometry("1280x720")
root.resizable(False, False)

# Defining the main frames for each separate window
main_frame = tk.Frame(root)
game_frame = tk.Frame(root)
score_frame = tk.Frame(root)

# Defining variables for use later
image_var = 0
score = 0
total_score = 0
timer = 0
multiplier = 0
state = False
current_level = ""
name = ""
sorted_scores1 = []
sorted_scores2 = []
sorted_scores3 = []
top_scores1 = ""
top_scores2 = ""
top_scores3 = ""
current_image = PhotoImage
current_image_data = []

# Importing Images
rules_image = ImageTk.PhotoImage(Image.open("img/recycling rules.png"))

# Dictionaries that store the image location and whether it is recycling or
# rubbish
level1_images = {"img1": ["img/apple.jpg", "rubbish"],
                 "img2": ["img/CAN.jpg", "recycling"],
                 "img3": ["img/cream.jpg", "rubbish"],
                 "img4": ["img/box.jfif", "recycling"],
                 "img5": ["img/vodka.jpg", "recycling"],
                 "img6": ["img/tin can.jpg", "recycling"],
                 "img7": ["img/cigarette.jpg", "rubbish"],
                 "img8": ["img/jar.jpg", "recycling"],
                 "img9": ["img/capsicum.jpg", "rubbish"],
                 "img10": ["img/egg.jpg", "recycling"]}

level2_images = {"img1": ["img/lightbulb.jpg", "rubbish"],
                 "img2": ["img/tape.jfif", "rubbish"],
                 "img3": ["img/aerosol.jfif", "recycling"],
                 "img4": ["img/newspaper.jpeg", "recycling"],
                 "img5": ["img/bubble wrap.jpg", "rubbish"],
                 "img6": ["img/milk.png", "recycling"],
                 "img7": ["img/pizza.jpg", "rubbish"],
                 "img8": ["img/tide.jfif", "recycling"],
                 "img9": ["img/15L bottle.psd.png", "rubbish"],
                 "img10": ["img/magazine.jpg", "recycling"]}

level3_images = {"img1": ["img/newspaper.jpeg", "bundle"],
                 "img2": ["img/aerosol.jfif", "recycling"],
                 "img3": ["img/egg.jpg", "bundle"],
                 "img4": ["img/rat.jpg", "rubbish"],
                 "img5": ["img/steel can.jpg", "recycling"],
                 "img6": ["img/broken glass.jpg", "rubbish"],
                 "img7": ["img/box.jfif", "bundle"],
                 "img8": ["img/paper cup.jpg", "rubbish"],
                 "img9": ["img/ultra gold.jpg", "recycling"],
                 "img10": ["img/paper plate.jfif", "rubbish"],
                 "img11": ["img/paper.jfif", "bundle"],
                 "img12": ["img/apple.jpg", "rubbish"],
                 "img13": ["img/4L no lid.jpg", "recycling"],
                 "img14": ["img/vodka.jpg", "rubbish"],
                 "img15": ["img/magazine.jpg", "bundle"],
                 "img16": ["img/flower.jfif", "rubbish"],
                 "img17": ["img/glass bottle lid.png", "rubbish"],
                 "img18": ["img/plastic bottle.jfif", "recycling"],
                 "img19": ["img/plastic container.png", "recycling"],
                 "img20": ["img/battery.jpg", "rubbish"]}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exit to main menu button
def change_to_main():
    global score, timer, multiplier, total_score, top_scores1, top_scores2, \
        top_scores3

    # Resetting all necessary variables when returning to main menu
    score = 0
    score_label.config(text=f"Score:{score}")
    total_score = 0

    top_scores1 = ""
    top_scores2 = ""
    top_scores3 = ""

    multiplier = 0

    reset()

    # Packs main menu frame, forgets the gameplay frame and scoreboard frame
    main_frame.pack(fill="both", expand=1)
    game_frame.forget()
    score_frame.forget()


# Change to gameplay frame
def change_to_game():
    game_frame.pack(fill="both", expand=1)
    main_frame.forget()


# Functions that run at the start of each level, starting the timer, starting
# the images changing, etc.
def level1():
    global score, current_level, image_var
    image_var = 0
    score = 0
    start()
    update_time()
    current_level = "Level 1"
    change_to_game()
    gameplay()


def level2():
    global score, current_level, image_var
    image_var = 0
    score = 0
    start()
    update_time()
    current_level = "Level 2"
    change_to_game()
    gameplay()


def level3():
    global score, current_level, image_var
    image_var = 0
    score = 0
    start()
    update_time()
    current_level = "Level 3"
    change_to_game()
    gameplay()


# Main gameplay variable. Retrieves images from the dictionary and changes them
# after a button has been pressed
def gameplay():
    global current_image, image_var, current_image_data

    if current_level == "Level 1" or current_level == "Level 2":
        if image_var < 10:
            if current_level == "Level 1":
                # image_var goes up by 1 every button press and this cycles to
                # the next image
                current_image_data = list(level1_images.values())[image_var]

            elif current_level == "Level 2":
                current_image_data = list(level2_images.values())[image_var]

            # Opening the image
            current_image = ImageTk.PhotoImage(Image.open(current_image_data[0]
                                                          ))
            # Displaying the image
            gameplay_image_label.config(image=current_image)

        else:
            # When all the images have been shown then it finishes the level
            finish_level()

    # Level 3 has twice as many photos so image_var needs to be
    # able to go up to 20
    elif current_level == "Level 3":
        if image_var < 20:
            current_image_data = list(level3_images.values())[image_var]
            current_image = ImageTk.PhotoImage(
                Image.open(current_image_data[0]))
            gameplay_image_label.config(image=current_image)

        else:
            finish_level()


# Function for the window after each level
def display_score():
    global score, timer, multiplier, total_score, name

    # Creating the window
    top = Toplevel(root)
    top.geometry("900x600")
    top.resizable(False, False)
    top.title("You beat the Level!")
    top.grab_set()
    top.config(bg="pink")

    # Calculating the player's multiplier depending on how quickly
    # they completed the level
    if current_level == "Level 1" or current_level == "Level 2":
        if timer < 5:
            multiplier = 10
        elif 4 < timer < 10:
            multiplier = 8
        elif 9 < timer < 20:
            multiplier = 6
        elif 19 < timer < 35:
            multiplier = 5
        elif 34 < timer < 50:
            multiplier = 4
        elif 49 < timer < 75:
            multiplier = 2
        elif timer > 74:
            multiplier = 1

    # Level 3 has twice as many items of rubbish, so the multiplier is
    # different making the maximum score still 100
    elif current_level == "Level 3":
        if timer < 10:
            multiplier = 5
        elif 9 < timer < 20:
            multiplier = 4
        elif 19 < timer < 40:
            multiplier = 3
        elif 39 < timer < 80:
            multiplier = 2
        elif timer > 79:
            multiplier = 1

    total_score = score * multiplier

    # Custom messages depending on the users score
    if total_score <= 10:
        message = "That was terrible... You should try again."
    elif 10 < total_score <= 30:
        message = "Awwww man :( You can do better next time!"
    elif 40 <= total_score <= 60:
        message = "That's pretty good!"
    elif 70 <= total_score <= 90:
        message = "Great job!"
    elif total_score == 100:
        message = "AMAZING! A perfect score!"
    else:
        message = ""

    # Custom message
    Label(top,
          text=f"Congratulations!\nIn {current_level} you got {score} "
          f"questions correct."
          f"\nYour time was: {timer} seconds"
          f"\n\nYour total score is {total_score}."
          f"\n{message}",
          font=("Calibri", 36), fg="white", bg="pink").place(relx=0.5,
                                                             rely=0.35,
                                                             anchor="center")

    # Entry box
    entry_text = Label(top,
                       text="Enter your name to save your score\nNo longer "
                            "than 10 characters.",
                       font=("Calibri", 24), fg="blue", bg="pink")
    entry_text.place(relx=0.5, rely=0.75, anchor="center")

    name_entry = Entry(top)
    name_entry.place(relx=0.5, rely=0.85, anchor="center")

    # Function for writing the score and name to the text files
    def save_score():
        global name, total_score

        # Any characters after the 10th will get deleted, making the maximum
        # length for names 10 characters
        if len(name_entry.get()) > 10:
            name_entry.delete(10, END)

        name = name_entry.get()

        # Converts all numbers to a 3 digit number, which allows them to
        # be sorted properly. E.g. 50 becomes 050
        if total_score < 100:
            total_score = str(total_score)
            total_score = total_score.zfill(3)
        else:
            pass

        # Checks if the entry box is empty
        if not name_entry.get():
            pass

        # Writing the score to the text file
        else:
            if current_level == "Level 1":
                file = open("score_1.txt", "a")  # Opens file
                file.write(
                    str(total_score) + "  -\t" + name + "\n")  # Writes to file
                file.close()  # Closes file

            elif current_level == "Level 2":
                file = open("score_2.txt", "a")
                file.write(str(total_score) + "  -\t" + name + "\n")
                file.close()
            elif current_level == "Level 3":
                file = open("score_3.txt", "a")
                file.write(str(total_score) + "  -\t" + name + "\n")
                file.close()

            # Exiting the top window after saving the score and returning
            # to main menu
            change_to_main()
            top.destroy()

    # Run when user closes the top window
    def on_close():
        change_to_main()
        top.destroy()

    name_entry_button = tk.Button(top, text="Save Score", command=save_score)
    name_entry_button.place(relx=0.5, rely=0.9, anchor="center")

    # Protocol for what to happen if the user closes the top window
    # without saving their score
    top.wm_protocol("WM_DELETE_WINDOW", on_close)


# Opens top window and resets timer
def finish_level():
    display_score()
    reset()


# Runs when player presses the rubbish button
def rubbish():
    global image_var
    image_var += 1
    check_rubbish()


# Runs when player presses the recycling button
def recycling():
    global image_var
    image_var += 1
    check_recycling()


# Runs when player presses the bundle and bag button
def bundle():
    global image_var
    image_var += 1
    check_bundle()


# The following functions check if the user's input is correct or wrong.
def check_rubbish():
    global score, current_image_data

    # Takes the list from the current dictionary value and checks the
    # second value in the list, to see if its "rubbish"
    if current_image_data[1] == "rubbish":
        # GUI label that pops up and shows CORRECT
        correct = tk.Label(gameplay_button_frame, text="CORRECT!",
                           anchor="center",
                           font=("Comic Sans MS", 40, "bold",),
                           fg="green", bg="blue")
        correct.place(relx=0.5, rely=0.48, anchor="center")

        # Destroys the correct label after 2 seconds
        correct.after(1000, correct.destroy)

        score += 1  # Increase score
        score_label.config(text=f"Score:{score}")  # Updating the score label

    elif current_image_data[1] != "rubbish":
        # GUI label that pops up and shows WRONG
        wrong = tk.Label(gameplay_button_frame, text="WRONG!", anchor="center",
                         font=("Comic Sans MS", 40, "bold",),
                         fg="red", bg="blue", width=8)
        wrong.place(relx=0.5, rely=0.48, anchor="center")
        wrong.after(1000, wrong.destroy)

    # Run the gameplay command again to switch the image and
    # continue the gameplay cycle
    gameplay()


def check_recycling():
    global score, current_image_data
    if current_image_data[1] == "recycling":
        correct = tk.Label(gameplay_button_frame, text="CORRECT!",
                           anchor="center",
                           font=("Comic Sans MS", 40, "bold",),
                           fg="green", bg="blue")
        correct.place(relx=0.5, rely=0.48, anchor="center")
        correct.after(1000, correct.destroy)
        score += 1
        score_label.config(text=f"Score:{score}")
    elif current_image_data[1] != "recycling":
        wrong = tk.Label(gameplay_button_frame, text="WRONG!", anchor="center",
                         font=("Comic Sans MS", 40, "bold",),
                         fg="red", bg="blue", width=8)
        wrong.place(relx=0.5, rely=0.48, anchor="center")
        wrong.after(1000, wrong.destroy)

    gameplay()


def check_bundle():
    global score, current_image_data
    if current_image_data[1] == "bundle":
        correct = tk.Label(gameplay_button_frame, text="CORRECT!",
                           anchor="center",
                           font=("Comic Sans MS", 40, "bold",),
                           fg="green", bg="blue")
        correct.place(relx=0.5, rely=0.48, anchor="center")
        correct.after(1000, correct.destroy)
        score += 1
        score_label.config(text=f"Score:{score}")
    elif current_image_data[1] != "bundle":
        wrong = tk.Label(gameplay_button_frame, text="WRONG!", anchor="center",
                         font=("Comic Sans MS", 40, "bold",),
                         fg="red", bg="blue", width=8)
        wrong.place(relx=0.5, rely=0.48, anchor="center")
        wrong.after(1000, wrong.destroy)

    gameplay()


def update_time():
    global timer
    if state:
        timer += 1

        # Update the time label box with the current time
        time_label.configure(text=f"Time:{timer}")

        # Call the update_time() function after 1 second to keep
        # the clock ticking
        root.after(1000, update_time)
    else:
        pass

    return timer


# Starts the timer by setting state to True
def start():
    global state
    state = True


# Resets timer by setting state to False and updating the timer label to 0
def reset():
    global state, timer
    state = False
    timer = 0
    time_label.config(text=f"Time:{timer}")


# Changes the window to the scoreboard frame
def change_to_score():
    scoreboard_read()
    score_frame.pack(fill="both", expand=1)
    main_frame.forget()


# Function that reads the text files with the top scores and
# then sorts them in order of highest score
def scoreboard_read():
    global top_scores1, top_scores2, top_scores3, sorted_scores1, \
        sorted_scores2, sorted_scores3

    # Opens file
    file = open("score_1.txt", "r")
    # Reads file and stores to variable
    read_file = file.readlines()
    # Sorts the var by highest number to lowest, assigns to new var
    sorted_scores1 = sorted(read_file, reverse=True)

    file = open("score_2.txt", "r")
    read_file = file.readlines()
    sorted_scores2 = sorted(read_file, reverse=True)

    file = open("score_3.txt", "r")
    read_file = file.readlines()
    sorted_scores3 = sorted(read_file, reverse=True)

    # Adds the top 10 scores to a string value
    for i in sorted_scores1[0:10]:
        top_scores1 += i

    for i in sorted_scores2[0:10]:
        top_scores2 += i

    for i in sorted_scores3[0:10]:
        top_scores3 += i

    # Updates the scoreboard label with the current top 10 scores
    level1_scores_scores_label.config(text=f"{top_scores1}")
    level2_scores_scores_label.config(text=f"{top_scores2}")
    level3_scores_scores_label.config(text=f"{top_scores3}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN MENU GUI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title section
title_frame = tk.Frame(main_frame, bg="purple", highlightthickness=5,
                       highlightbackground="black")
title_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW")

title_text_frame = tk.LabelFrame(title_frame, borderwidth=0,
                                 highlightthickness=0)
title_text_frame.place(relx=0.5, rely=0.45, anchor="center")

title_text = tk.Label(title_text_frame, text="Recycling or Rubbish?",
                      font=("Helvetica", 55, "bold",), fg="#ffffff",
                      background="purple")
title_text.grid()

scoreboard_button = tk.Button(title_frame, text="High Scores",
                              font=("Helvetica", 20, "bold"),
                              command=change_to_score)
scoreboard_button.place(relx=0.915, rely=0.5, anchor="center")

# Rules Section
rules_frame = tk.Frame(main_frame, bg="red", highlightthickness=5,
                       highlightbackground="black")
rules_frame.grid(row=1, column=0, sticky="NSEW")

rules_title_frame = tk.LabelFrame(rules_frame, background="red", borderwidth=0,
                                  highlightthickness=0)
rules_title_frame.place(relx=0.5, rely=0.1, anchor="center")

rules_title = tk.Label(rules_title_frame, text="Instructions",
                       font=("Helvetica", 40, "bold", "underline"),
                       bg="red", fg="#ffffff")
rules_title.grid()

rules_text_frame = tk.LabelFrame(rules_frame, background="purple",
                                 borderwidth=0, highlightthickness=0)
rules_text_frame.place(relx=0.5, rely=0.6, anchor="center")

rules_text = tk.Label(rules_text_frame,
                      text="You will be presented with items of trash and\n it"
                           " is up to you to decide whether\nit gets recycled "
                           "or put in the rubbish.\n\n Level 3 is a special "
                           "level\n which takes place on Great Barrier Island."
                           "\n There are some different rules on Great Barrier"
                           "\nIsland so watch out for that!\n\n Your total "
                           "score will also be affected by your time!\nBe "
                           "quick and accurate.",
                      font=("Helvetica", 24), bg="red", fg="#ffffff")
rules_text.grid()

# Levels Section
levels_frame = tk.LabelFrame(main_frame, bg="yellow", highlightthickness=5,
                             highlightbackground="black")
levels_frame.grid(row=1, column=1, sticky="NSEW")

levels_title_frame = tk.LabelFrame(levels_frame, bg="yellow", borderwidth=0,
                                   highlightthickness=0)
levels_title_frame.place(relx=0.5, rely=0.1, anchor="center")

levels_title = tk.Label(levels_title_frame, text="Levels",
                        font=("Helvetica", 35, "bold", "underline"),
                        bg="yellow",
                        fg="#ffffff")
levels_title.grid()

# Buttons for the different levels
level1_button = tk.Button(levels_frame, text="Level 1",
                          font=("Helvetica", 24, "bold"), command=level1)
level1_button.place(relx=0.5, rely=0.25, anchor="center")

level2_button = tk.Button(levels_frame, text="Level 2",
                          font=("Helvetica", 24, "bold"), command=level2)
level2_button.place(relx=0.5, rely=0.5, anchor="center")

level3_button = tk.Button(levels_frame, text="Level 3:\nGreat Barrier\nIsland",
                          font=("Helvetica", 24, "bold"), command=level3)
level3_button.place(relx=0.5, rely=0.8, anchor="center")

# Giving the empty rows weight to align the widgets correctly
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=4)
main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GAMEPLAY GUI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title Section
game_title_frame = tk.Frame(game_frame, bg="purple", highlightthickness=5,
                            highlightbackground="black")
game_title_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW")

title_text_frame = tk.LabelFrame(game_title_frame, borderwidth=0,
                                 highlightthickness=0)
title_text_frame.place(relx=0.5, rely=0.45, anchor="center")

title_text = tk.Label(title_text_frame, text="Recycling or Rubbish?",
                      font=("Helvetica", 55, "bold",), fg="#ffffff",
                      background="purple")
title_text.grid()

exit_button = tk.Button(game_title_frame, text="Exit to\nMain Menu",
                        font=("Helvetica", 20, "bold"),
                        command=change_to_main)
exit_button.place(relx=0.915, rely=0.5, anchor="center")

score_label = tk.Label(game_title_frame, text=f"Score:{score}",
                       font=("Helvetica", 32, "bold"),
                       bg="purple", fg="white")
score_label.place(relx=0.03, rely=0.1)

time_label = tk.Label(game_title_frame, text=f"Time:{timer}",
                      font=("Helvetica", 32, "bold"), bg="purple", fg="white")
time_label.place(relx=0.03, rely=0.5)

# Rules Section
game_rules = tk.Frame(game_frame, bg="red", highlightthickness=5,
                      highlightbackground="black")
game_rules.grid(row=2, column=0, columnspan=2, sticky="NSEW")

game_rules_img = tk.Label(game_rules)
game_rules_img.place(relx=0.5, rely=0.5, anchor="center")
game_rules_img.config(image=rules_image)

# Image Section
gameplay_image_frame = tk.Frame(game_frame, bg="yellow", highlightthickness=5,
                                highlightbackground="black")
gameplay_image_frame.grid(row=1, column=0, sticky="NSEW")
gameplay_image_frame.grid_propagate(False)  # Makes the frame not resizable

gameplay_image_label = tk.Label(gameplay_image_frame, width=535, height=400)
gameplay_image_label.place(relx=0.5, rely=0.5, anchor="center")
gameplay_image_label.grid_propagate(False)

# Button Section
gameplay_button_frame = tk.Frame(game_frame, bg="blue", highlightthickness=5,
                                 highlightbackground="black")
gameplay_button_frame.grid(row=1, column=1, sticky="NSEW")

rubbish_button = tk.Button(gameplay_button_frame, text="Rubbish",
                           font=("Helvetica", 20, "bold"),
                           command=rubbish)
rubbish_button.place(relx=0.5, rely=0.33, anchor="center")

recycling_button = tk.Button(gameplay_button_frame, text="Recycling",
                             font=("Helvetica", 20, "bold"),
                             command=recycling)
recycling_button.place(relx=0.5, rely=0.66, anchor="center")

bundle_button = tk.Button(gameplay_button_frame, text="Bundle and Bag",
                          font=("Helvetica", 20, "bold"),
                          command=bundle)
bundle_button.place(relx=0.5, rely=0.8, anchor="center")

# Giving the empty rows weight to align the widgets correctly
game_frame.grid_rowconfigure(0, weight=1)
game_frame.grid_rowconfigure(1, weight=3)
game_frame.grid_rowconfigure(2, weight=1)
game_frame.grid_columnconfigure(0, weight=3)
game_frame.grid_columnconfigure(1, weight=1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SCOREBOARD GUI~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title Section
score_title_frame = tk.Frame(score_frame, bg="purple", highlightthickness=5,
                             highlightbackground="black")
score_title_frame.grid(row=0, column=0, sticky="NSEW")

title_text_frame = tk.LabelFrame(score_title_frame, borderwidth=0,
                                 highlightthickness=0)
title_text_frame.place(relx=0.5, rely=0.45, anchor="center")

title_text = tk.Label(title_text_frame, text="Recycling or Rubbish?",
                      font=("Helvetica", 55, "bold",), fg="#ffffff",
                      background="purple")
title_text.grid()

exit_button = tk.Button(score_title_frame, text="Exit to\nMain Menu",
                        font=("Helvetica", 20, "bold"),
                        command=change_to_main)
exit_button.place(relx=0.915, rely=0.5, anchor="center")

# High Scores Section
high_scores_frame = tk.Frame(score_frame, bg="hot pink", highlightthickness=5,
                             highlightbackground="black")
high_scores_frame.grid(row=1, column=0, sticky="NSEW")

level1_scores_label = tk.Label(high_scores_frame, bg="hotpink", fg="black",
                               text=str("Top 10 Scores for Level One\n"
                                        f"Score\tName"),
                               font=("Helvetica", 23, "underline"),
                               justify="left")
level1_scores_label.grid(row=0, column=0)

level1_scores_scores_label = tk.Label(high_scores_frame, bg="hotpink",
                                      fg="black", text=f"{top_scores1}",
                                      font=("Helvetica", 20), justify="left")
level1_scores_scores_label.grid(row=1, column=0, sticky="NEW")

level2_scores_label = tk.Label(high_scores_frame, bg="hotpink", fg="black",
                               text=f"Top 10 Scores for Level Two\n"
                               f"Score\tName",
                               font=("Helvetica", 23, "underline"),
                               justify="left")
level2_scores_label.grid(row=0, column=1)

level2_scores_scores_label = tk.Label(high_scores_frame, bg="hotpink",
                                      fg="black", text=f"{top_scores2}",
                                      font=("Helvetica", 20), justify="left")
level2_scores_scores_label.grid(row=1, column=1, sticky="NEW")

level3_scores_label = tk.Label(high_scores_frame, bg="hotpink", fg="black",
                               text=f"Top 10 Scores for Level Three"
                               f"\nScore\tName",
                               font=("Helvetica", 23, "underline"),
                               justify="left")
level3_scores_label.grid(row=0, column=2)

level3_scores_scores_label = tk.Label(high_scores_frame, bg="hotpink",
                                      fg="black", text=f"{top_scores3}",
                                      font=("Helvetica", 20), justify="left")
level3_scores_scores_label.grid(row=1, column=2, sticky="NEW")

# Giving the empty rows weight to align the widgets correctly
score_frame.grid_rowconfigure(0, weight=1)
score_frame.grid_rowconfigure(1, weight=4)
score_frame.grid_columnconfigure(0, weight=1)
score_title_frame.grid_propagate(False)
high_scores_frame.grid_propagate(False)
high_scores_frame.grid_columnconfigure(0, weight=1)
high_scores_frame.grid_columnconfigure(1, weight=1)
high_scores_frame.grid_columnconfigure(2, weight=1)
high_scores_frame.grid_rowconfigure(0, weight=1)
high_scores_frame.grid_rowconfigure(1, weight=5)

# Code starts
main_frame.pack(fill="both", expand=1)
root.mainloop()
