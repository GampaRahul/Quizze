from tkinter import *
from tkinter import messagebox
from player import *
from PIL import Image, ImageTk

start_game = 0


def display(data_frame, players, remove, names, start_button, input_quesions, file_label):
    for i in range(len(players)):
        names[i].grid(row=i+1, column=0, sticky="w", padx=20)
        remove[i].grid(row=i+1, column=3, sticky="e", padx=20)
    if len(players) > 0:
        file_label.grid(row=len(players) + 1, column=0)
        input_quesions.grid(row=len(players) + 1, column=1)
        start_button.grid(row=len(players) + 2, column=1, padx=20, pady=20)
    else:
        start_button.grid_forget()
        input_quesions.grid_forget()
        file_label.grid_forget()


def add_player(data_frame, team_name_entry, team_no_entry, team_name_value, team_no_value, players, remove, names,
               start_button, input_questions, file_label):
    if team_name_value.get() == "":
        messagebox.showinfo("Error", "Please enter the team name")
        return
    try:
        team_no = int(team_no_value.get())
    except ValueError as vr:
        messagebox.showinfo("Error", "Invalid Team Number")
        team_no_entry.delete(0, END)
        return
    players.append(Player(team_name_value.get(), team_no))
    team_no_entry.delete(0, END)
    team_name_entry.delete(0, END)
    label = Label(data_frame, text=f"{players[len(players)-1].get_name()}"f"-  {players[len(players)-1].get_team_no()}",
                  font=("", 14, "italic"), bg="bisque")
    names.append(label)
    img = Image.open("remove.png")
    img = img.resize((30, 30), Image.ANTIALIAS)
    button_image = ImageTk.PhotoImage(img)
    remove_button = Button(data_frame, image=button_image, text=team_no_value.get(), background="bisque", borderwidth=0,
                           relief="solid", command=lambda: remove_player(data_frame, remove_button, players, remove,
                                                                         names, start_button, input_questions, file_label))
    remove_button.image = button_image
    remove.append(remove_button)
    display(data_frame, players, remove, names, start_button, input_questions, file_label)


def remove_player(data_frame, remove_button, players, remove, names, start_button, input_questions, file_label):
    ind = remove.index(remove_button)
    remove[ind].grid_forget()
    names[ind].grid_forget()
    remove.pop(ind)
    names.pop(ind)
    players.pop(ind)
    print(len(players), len(remove))
    display(data_frame, players, remove, names, start_button, input_questions, file_label)


def start_quiz(window, file, questions):
    flag = 1
    try:
        f = open(file.get()+".txt", "r")
    except (OSError, IOError) as e:
        flag = 0
        messagebox.showinfo("Error", "Enter correct File Name")
    if flag == 1:
        lines = f.readlines()
        question = []
        for i in range(len(lines)):
            if lines[i] != "\n":
                text = lines[i][:-1]
                txt = ""
                flag = 0
                for i in range(len(text)):
                    if i % 50 == 0 and i > 0:
                        flag = 1
                    if flag == 1 and text[i] == " " and text[i+1] !="?":
                        txt += "\n"
                        flag = 0
                    txt += text[i]
                question.append(txt)
            else:
                questions.append(tuple(question))
                question.clear()
        global start_game
        start_game = 1
        window.destroy()


def player_entry_gui():
    players = []
    questions = []
    remove = []
    names = []
    # create main window
    window = Tk()
    window.title("Quizze")
    h = 400
    w = 800
    window.geometry(f"{w}x{h}")
    window.maxsize(w, h)
    window.minsize(w, h)

    # creation of left frame
    left_frame = Frame(window, bg="bisque")

    # creation of entry frame
    entry_frame = Frame(left_frame, background="#ffffff")
    data_entry_frame = Frame(entry_frame, bg="#ffffff")
    heading = Label(data_entry_frame, text="Add Players", bg="#ffffff", font=("", 14, ""))
    heading.grid(row=0, columnspan=2, pady=20)
    team_name = Label(data_entry_frame, text="Team Name:", bg="#ffffff")
    team_name.grid(row=1, column=0, sticky="e", pady=2)

    team_name_value = StringVar() # contains entered team name
    team_name_entry = Entry(data_entry_frame, textvariable=team_name_value, relief="solid")
    team_name_entry.grid(row=1, column=1, pady=2)

    team_no = Label(data_entry_frame, text="Team Number:", bg="#ffffff")
    team_no.grid(row=2, column=0, pady=2)

    team_no_value = StringVar() # contains entered team no
    team_no_entry = Entry(data_entry_frame, textvariable=team_no_value, relief="solid")
    team_no_entry.grid(row=2, column=1, pady=2)
    data_entry_frame.place(anchor="c", relx=.5, rely=.5)
    entry_frame.place(relx=0.15, rely=0.38, height=200, width=250)
    left_frame.place(relwidth=.4, relheight=1, anchor="nw")

    # creation of right frame
    right_frame = Frame(window,  background="bisque", borderwidth=2, relief="solid")

    # creation of data display frame
    data_frame = Frame(right_frame, bg="bisque")
    label = Label(data_frame, text="Teams:", font=("", 20, "underline"), bg="bisque")
    label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    data_frame.place(relheight=1, relwidth=1)

    # Button for adding new player
    img = Image.open("add_button.png")
    img = img.resize((100, 30), Image.ANTIALIAS)
    add_button_image = ImageTk.PhotoImage(img)

    # Input questions file
    file = StringVar()
    input_questions = Entry(data_frame, textvariable=file)

    # button for starting the quiz
    img = Image.open("start.png")
    img = img.resize((50, 50), Image.ANTIALIAS)
    start_button_image = ImageTk.PhotoImage(img)
    start_button = Button(data_frame, image=start_button_image, background="bisque", borderwidth=0, relief="solid",
                          command=lambda: start_quiz(window, file, questions))
    file_label = Label(data_frame, text="File name:")
    add_team_button = Button(data_entry_frame, image=add_button_image,background="#ffffff", borderwidth=0, relief="solid",
            command=lambda: add_player(data_frame, team_name_entry, team_no_entry,
                                team_name_value, team_no_value, players, remove, names, start_button, input_questions, file_label))
    add_team_button.grid(row=3, column=0, columnspan=2, pady=10)
    right_frame.place(relx=.4, height=h+5, width=w, y=-2)
    window.mainloop()
    return players,questions

