from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
question_index = 0


def display_logo(display_data, on_screen):
    for frame in display_data.values():
        frame.pack_forget()
    display_data['logo'].pack()
    on_screen.grid_forget()
    on_screen['text'] = "Logo"
    on_screen.grid(sticky='w', row=0, column=1, pady=1)


def answer_display(display_data, on_screen, questions):
    if question_index-1 < 0:
        messagebox.showinfo("Error","There is no question to display the answer")
    else:
        for frame in display_data.values():
            frame.pack_forget()
        display_data["answer_frame"].pack(fill="both", expand=1)
        display_data["answer"]['text'] = questions[question_index-1][-1]
        display_data["answer"].pack()
        on_screen.grid_forget()
        on_screen['text'] = "Answer"
        on_screen.grid(sticky='w', row=0, column=1, pady=1)


def next_ques(questions, next_question_log, display_data, on_screen, question_frame, flag):
    global question_index
    if flag == 1:
        question_index -= 1
    if question_index >= len(questions):
        display_logo(display_data, on_screen)
    else:
        for frame in question_frame:
            frame.grid_forget()
        question_frame[0]['text'] = questions[question_index][0]
        question_frame[0].grid(row=0, column=0, columnspan=2)
        size = len(questions[question_index])
        if size >= 2:
            question_frame[1]['text'] = questions[question_index][1]
            question_frame[1].grid(row=1, column=0, padx=30, sticky="se", pady=10)
        if size >= 3:
            question_frame[2]['text'] = questions[question_index][2]
            question_frame[2].grid(row=1, column=1, padx=30, sticky="sw", pady=10)
        if size >= 4:
            question_frame[3]['text'] = questions[question_index][3]
            question_frame[3].grid(row=2, column=0, padx=30, sticky="ne", pady=10)
        if size >= 5:
            question_frame[4]['text'] = questions[question_index][4]
            question_frame[4].grid(row=2, column=1, padx=30, sticky="nw", pady=10)
        for frame in display_data.values():
            frame.pack_forget()
        display_data["question_container"].pack(anchor="center", pady=300)
        display_data["question"].pack(fill="both", expand=1)
        next_question_log.grid_forget()
        if question_index+1 < len(questions):
            next_question_log['text'] = questions[question_index+1][0]
        else:
            next_question_log['text'] = "No more questions to display"
        next_question_log.grid(sticky='w', row=1, column=1, pady=1)
        on_screen.grid_forget()
        on_screen['text'] = "Question"
        on_screen.grid(sticky='w', row=0, column=1, pady=1)
        question_index += 1


def display_score(teams, display_data, on_screen, scores):
    for frame in display_data.values():
        frame.pack_forget()
    for labels in scores:
        labels.pack_forget()
    display_data['score'].pack(fill="both", expand=1)
    on_screen.grid_forget()
    on_screen['text'] = "Score Board"
    on_screen.grid(sticky='w', row=0, column=1, pady=1)
    teams.sort(key=lambda x: x.get_score(), reverse=True)
    colors = ["yellow", "grey", "bisque", "blue", "blue", "blue"]
    for i in range(len(teams)):
        scores[i]['bg'] = colors[i%6]
        text = "#"+str(i+1)+"\t\t"+teams[i].get_name()+"\t\t"+str(teams[i].get_score())+"  "
        scores[i]['text'] = text
        scores[i].pack(side="top", pady=10)


def update_score(score_updater_frame, current_score, new_score, team_name_score, right_frame, player, log, buzzer_val, display_data):
    if buzzer_val.get() == 1:
        for frame in display_data.values():
            frame.pack_forget()
        display_data["logo"].pack_forget()
        display_data["buzzer"].pack(fill="both", expand=1)
        display_data["buzzered_team"].pack_forget()
        display_data["buzzered_team"]['text'] = player.get_name()
        display_data["buzzered_team"].pack()
    # #start of right frame
    custom_score = StringVar()
    score_updater_frame.pack_forget()
    team_name_score.grid_forget()
    Label(score_updater_frame, text="Update Score:", font=("", 18, "underline"), bg="bisque").grid(row=0, column=0)
    # score updater frame
    Label(score_updater_frame, text="Team:", font=("", 14), bg="bisque") \
        .grid(row=1, column=0, columnspan=2, sticky="w", padx=5)
    team_name_score['text'] = player.get_name()
    team_name_score.grid(row=1, column=2, columnspan=2, sticky="w", padx=5)
    Label(score_updater_frame, text="Current Score:", font=("", 14), bg="bisque") \
        .grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    current_score['text'] = player.get_score()
    current_score.grid(row=2, column=2, columnspan=2, sticky="w", padx=5, pady=3)
    Label(score_updater_frame, text="Auto:", bg="bisque", font=("", 14)) \
        .grid(row=3, column=0, sticky="w", padx=5, pady=3)
    Label(score_updater_frame, text="Custom Score:", bg="bisque", font=("", 14)) \
        .grid(row=4, column=0, sticky="w", padx=5, pady=3)
    custom_score_entry = Entry(score_updater_frame, textvariable=custom_score, width=8)
    custom_score_entry.grid(row=4, column=1, sticky='e')
    custom_score_ok_btn = Button(score_updater_frame, text="Ok", font=("", 12),
                    command=lambda: add_score(new_score['text'], custom_score.get(), new_score, custom_score_entry))
    custom_score_ok_btn.grid(row=4, column=2, sticky="w", padx=5, pady=3)
    Auto_incr_btn = Button(score_updater_frame, text="+10", font=("", 12),
                           command=lambda: add_score(new_score['text'], 10, new_score, custom_score_entry))
    Auto_incr_btn.grid(row=3, column=2, sticky="w", padx=5, pady=3)
    Auto_decr_btn = Button(score_updater_frame, text="-5", font=("", 12),
                           command=lambda: add_score(new_score['text'], -5, new_score, custom_score_entry))
    Auto_decr_btn.grid(row=3, column=3, sticky="w", padx=5, pady=3)
    reset_new_score = Button(score_updater_frame, text="Reset", font=("", 12),
                             command=lambda: reset(new_score, player.get_score()))
    reset_new_score.grid(row=5, column=0, sticky='w', padx=5, pady=3)
    Label(score_updater_frame, text="New Score:", font=("", 14), bg="bisque") \
        .grid(row=6, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    new_score['text'] = player.get_score()
    new_score.grid(row=6, column=2, columnspan=2, sticky="w", padx=5, pady=3)
    right_frame.place(y=-1, relx=.5, relwidth=.6, relheight=.64)
    score_updater_frame.pack(side="left", anchor='n', pady=20)
    update_btn = Button(score_updater_frame, text="Update", font=("", 12),
                        command=lambda: update(int(new_score['text']), player, right_frame, log, player.get_score()))
    update_btn.grid(row=7, column=0, columnspan=4)
    # #end of right frame


def reset(field, cur_score):
    field.grid_forget()
    field['text'] = cur_score
    field.grid(row=6, column=2, columnspan=2, sticky="w", padx=5, pady=3)


def add_score(cur_score, score, field, custom_score_entry):
    field.grid_forget()
    if score == "":
        messagebox.showinfo("Error", "Enter proper custom score")
        return
    try:
        field['text'] = int(cur_score) + int(score)
    except ValueError as vr:
        messagebox.showinfo("Error", "Enter proper custom score")
        custom_score_entry.delete(0, END)
    field.grid(row=6, column=2, columnspan=2, sticky="w", padx=5, pady=3)


def update(score, player, right_frame, log, oldscore):
    player.set_score(score)
    right_frame.place_forget()
    log[0].grid_forget()
    log[0]['text'] = player.get_name()
    log[0].grid(sticky='w', row=3, column=1, pady=1)
    log[1].grid_forget()
    log[1]['text'] = oldscore
    log[1].grid(sticky='w', row=5, column=1)
    log[2].grid_forget()
    log[2]['text'] = player.get_score()
    log[2].grid(sticky='w', row=6, column=1)


def game(teams, questions):
    controller_screen = Tk()
    controller_screen.configure(background="bisque")
    controller_screen.title("Quizze")
    display_screen = Toplevel()
    display_screen.title("Display")
    w1, h1 = display_screen.winfo_screenwidth(), display_screen.winfo_screenheight()
    display_screen.geometry("%dx%d+0+0" % (w1, h1))
    h = 600
    w = 850
    controller_screen.geometry(f"{w}x{h}")
    controller_screen.maxsize(w, h)
    controller_screen.minsize(w, h)

    # Log frame
    bottom_frame = Frame(controller_screen, borderwidth=1, relief="solid", bg="bisque")
    bottom_frame.place(y=-1, x=-1, rely=.639, relwidth=1.01, relheight=.364)
    log_frame = Frame(bottom_frame, bg="#ffffff", borderwidth=1, relief="solid")
    log_frame.place(relx=.4, relheight=1, relwidth=.6)
    Label(log_frame, text="Log", font=("", 8), bg="grey").pack(fill="x")

    # frame for log data
    log_data_frame = Frame(log_frame, bg="#ffffff")
    log_data_frame.pack(anchor="nw", padx=2, pady=1)
    Label(log_data_frame, text="Displaying:", font=("", 10), bg="#ffffff").grid(sticky='w', row=0, column=0, pady=1)
    on_screen = Label(log_data_frame, text="Logo", font=("", 10), bg="#ffffff")
    on_screen.grid(sticky='w', row=0, column=1, pady=1)
    Label(log_data_frame, text="Next Question:", font=("", 10), bg="#ffffff").grid(sticky='w', row=1, column=0, pady=1)
    next_question_label = Label(log_data_frame, text=questions[0][0], font=("", 10), bg="#ffffff")
    next_question_label.grid(sticky='w', row=1, column=1, pady=1)
    Label(log_data_frame, bg="#ffffff", text="Last Changed:", font=("", 11, "underline")). \
        grid(sticky='w', row=2, column=0, columnspan=2, pady=1)
    Label(log_data_frame, text="Team:", font=("", 10), bg="#ffffff").grid(sticky='w', row=3, column=0, pady=1)
    team_name_log = Label(log_data_frame, text="null", font=("", 10), bg="#ffffff")
    team_name_log.grid(sticky='w', row=3, column=1, pady=1)
    Label(log_data_frame, bg="#ffffff", text="Score Updated:", font=("", 10, "underline")). \
        grid(sticky='w', row=4, column=0, columnspan=2, pady=1)
    Label(log_data_frame, text="From:", font=("", 10), bg="#ffffff").grid(sticky='w', row=5, column=0)
    from_score = Label(log_data_frame, text="null", font=("", 10), bg="#ffffff")
    from_score.grid(sticky='w', row=5, column=1)
    Label(log_data_frame, text="To:", font=("", 10), bg="#ffffff").grid(sticky='w', row=6, column=0)
    to_score = Label(log_data_frame, text="null", font=("", 10), bg="#ffffff")
    to_score.grid(sticky='w', row=6, column=1)
    log = [team_name_log, from_score, to_score]
    # end of log Gui

    # display Gui
    img = Image.open("bg.png")
    img = img.resize((w1, h1), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(img)
    next_ques_frame = Frame(display_screen, background="#7274d4")
    bg_label = Label(next_ques_frame, image=bg)
    bg_label.image = bg
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    question_container = Frame(next_ques_frame, bg="#fff", highlightbackground="#eddd2f", highlightcolor="#e83810", highlightthickness=8)
    question_label = Label(question_container, background="#fff", font=("", 25))
    question_label.grid(row=0, column=0, columnspan=2)
    opt1 = Label(question_container, bg="#fff", font=("", 25), borderwidth=1)
    opt1.grid(row=1, column=0)
    opt2 = Label(question_container, bg="#fff", font=("", 25), borderwidth=1)
    opt2.grid(row=1, column=1)
    opt3 = Label(question_container, bg="#fff", font=("", 25), borderwidth=1)
    opt3.grid(row=2, column=0)
    opt4 = Label(question_container, bg="#fff", font=("", 25), borderwidth=1)
    opt4.grid(row=2, column=1)
    scoreboard_frame = Frame(display_screen, bg="bisque")
    score_bg_label = Label(scoreboard_frame, image=bg)
    score_bg_label.image = bg
    score_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    scores = []
    Label(scoreboard_frame, text="Leaderboard", font=("Times New Roman", 30)).pack(side="top", pady=20)
    for i in range(len(teams)):
        L = Label(scoreboard_frame, relief="raised", font=("Times New Roman", 22), borderwidth=20)
        L.pack()
        scores.append(L)
    buzzer_frame = Frame(display_screen, background="#7274d4")
    img = Image.open("buzzer1.png")
    img = img.resize((500, 250), Image.ANTIALIAS)
    buzzer_img = ImageTk.PhotoImage(img)
    buzzer_bg = Label(buzzer_frame, image=bg)
    buzzer_bg.image = bg
    buzzer_bg.place(x=0, y=0, relwidth=1, relheight=1)
    buzzer = Label(buzzer_frame, image=buzzer_img)
    buzzer.image = buzzer_img
    logo_frame = Frame(display_screen)
    img = Image.open("logo.png")
    buzzer.pack(side="top", pady=80)
    buzzer_clicked = Label(buzzer_frame, text="Clicked!", font=("", 70), relief="solid", borderwidth=2)
    buzzer_clicked.pack()
    img = img.resize((w1, h1), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(img)
    logo = Label(logo_frame, image=logo_img)
    logo.image = logo_img
    logo.pack(fill='both')
    logo_frame.pack()
    answer_frame = Frame(display_screen)
    img = Image.open("correct.png")
    img = img.resize((500, 250), Image.ANTIALIAS)
    correct_img = ImageTk.PhotoImage(img)
    answer_bg = Label(answer_frame, image=bg)
    answer_bg.image = bg
    answer_bg.place(x=0, y=0, relwidth=1, relheight=1)
    answer_img = Label(answer_frame, image=correct_img)
    answer_img.image = correct_img
    answer_img.pack(side="top", pady=80)
    answer = Label(answer_frame, text="Clicked!", font=("", 45), relief="solid", borderwidth=2)
    answer.pack(padx=10)
    question_frame = [question_label, opt1, opt2, opt3, opt4]
    display_data = {"logo": logo_frame, "buzzer": buzzer_frame,
                    "question": next_ques_frame, "score": scoreboard_frame, "buzzered_team": buzzer_clicked,
                    "question_container": question_container, "answer_frame": answer_frame, "answer": answer}


    # controller Gui
    left_frame = Frame(controller_screen, borderwidth=1, relief="solid", bg="bisque")
    left_frame.place(x=-1, y=-1, relwidth=.501, relheight=.64)
    right_frame = Frame(controller_screen,  bg="bisque")
    score_updater_frame = Frame(right_frame, bg="bisque")
    current_score = Label(score_updater_frame, font=("", 14), bg="bisque")
    new_score = Label(score_updater_frame, font=("", 14), bg="bisque")
    team_name_score = Label(score_updater_frame, font=("", 14), bg="bisque")

    # #start of bottom frame

    # display buttons frame
    display_buttons_frame = Frame(bottom_frame, bg="bisque")
    display_buttons_frame.place(x=10, y=10)
    scoreboard_btn = Button(display_buttons_frame, text="Score Board", font=("", 12),
                            command=lambda: display_score(teams, display_data, on_screen, scores))
    nextques_btn = Button(display_buttons_frame, text="Next Question", font=("", 12),
            command=lambda: next_ques(questions, next_question_label, display_data, on_screen, question_frame, flag=0))
    logo_btn = Button(display_buttons_frame, text="Logo", font=("", 12), command=lambda: display_logo(display_data, on_screen))
    curques_btn = Button(display_buttons_frame, text="Current Question", font=("", 12),
                         command=lambda: next_ques(questions, next_question_label, display_data, on_screen,
                                                   question_frame, flag=1))
    answer_btn = Button(display_buttons_frame, text="Answer", font=("", 12), command= lambda: answer_display(display_data, on_screen, questions))
    curques_btn.grid(row=1, column=0, padx=10, pady=10)
    answer_btn.grid(row=1, column=1, padx=10, pady=10)
    scoreboard_btn.grid(row=0, column=0, padx=10, pady=10)
    nextques_btn.grid(row=0, column=1, padx=10, pady=10)
    logo_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    # #end of bottom_frame

    # #start of left frame
    Label(left_frame, text="Teams:", font=("", 18, "underline"), bg="bisque").pack(anchor='w', padx=10)
    buzzer_val = IntVar()
    Checkbutton(left_frame, text="Buzzer!!", font=("", 10), variable=buzzer_val, bg="bisque").pack()
    # team buttons frame
    team_buttons_frame = Frame(left_frame, bg="bisque")
    team_buttons_frame.pack(side="left", anchor='n')
    buttons = []
    for i in range(len(teams)):
        button = Button(team_buttons_frame, text=teams[i].get_team_no(), width=50,
                              command=lambda player=teams[i]: update_score(score_updater_frame, current_score,
                                                        new_score, team_name_score,right_frame, player, log, buzzer_val, display_data))
        buttons.append(button)
        buttons[i].grid(row=i, column=0, padx=10, pady=5)
    # #end of left frame

    controller_screen.mainloop()
    display_screen.mainloop()


