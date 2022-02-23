#importing
import mysql.connector, random
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
#from tkinter import ttk

def Get_From_Db(your_host, your_user, your_password, db, query):
    try:
        db_From = mysql.connector.connect(host = your_host, user = your_user, password = your_password, database = db )
        mycursor_From = db_From.cursor()
        mycursor_From.execute(query)
    except:
        print("launch db")
    return mycursor_From.fetchall()


def Get_To_Db(your_host, your_user, your_password, db, query):
    try:
        db_To = mysql.connector.connect(host = your_host, user = your_user, password = your_password, database = db )
        mycursor_To = db_To.cursor()
        mycursor_To.execute(query)
        db_To.commit()
    except Exception as e:
        print(e)



window = tk.Tk()
window.winfo_toplevel().title('Sapper')
window.geometry('400x400')



def register_In_DB():
    print(l_reg.get())
    print(l_reg2.get())
    print(p_reg.get())
    print("Insert into account values (NULL, '{0}', '{1}')".format(l_reg.get(), p_reg.get()))
    if l_reg.get() == l_reg2.get():
        try:
            (Get_To_Db('localhost', 'root', '', 'sapper', "Insert into account values (NULL, '{0}', '{1}')".format(l_reg.get(), p_reg.get())))
            (Get_To_Db('localhost', 'root', '', 'sapper', "insert into points VALUES (NULL,(select id from account order by id DESC limit 1),0)"))

            messagebox.showinfo("Information", "You've registered properly")
        except:
            print("jakis blad")


counter = 0

x_logged = False

label = tk.Label( window, text = "Select position without the bomb" )
label.pack( side = tk.BOTTOM )

l = tk.StringVar()
login = tk.Entry(window, textvariable=l)
login.place(x = 150, y = 80)

p = tk.StringVar()
password = tk.Entry(window,show = '*', textvariable = p)
password.place(x = 150, y = 105)

Label_Login_Text = tk.Label(window, text = 'Login:')
Label_Login_Text.place(x = 90, y = 80)

Password_Text = tk.Label(window, text = 'Password:')
Password_Text.place(x = 85, y = 105)

label_text = tk.StringVar()
label_text.set("Please Log in:")

Please_Log_In_Text=tk.Label(window, textvariable = label_text, font = ("Arial", 20))
Please_Log_In_Text.place(y = 30, x = 140)

def hit():
    messagebox.showinfo("Game result", "You hit, Congratulations. +1 points")
    Get_To_Db('localhost', 'root', '', 'sapper', "Update account, points set points.points=points.points +1 where points.id=account.id and account.login='{0}' ".format(l.get()))
    window_Game.destroy()


def miss():
    messagebox.showinfo("Game result","You missed")
    window_Game.destroy()



def start_Game():
    global window_Game
    window_Game=tk.Toplevel()
    window_Game.focus_set()
    window_Game.grab_set()
    window_Game.geometry('600x600')
    window_Game.resizable(0, 0)

    window_Game.columnconfigure(0, weight=6)
    window_Game.columnconfigure(1, weight=6)


    global przyciski
    przyciski = []
    dobry = []
    for w in range(5):
        dobry.append(random.randint(0,35))
    random.randint(0,35)
    for i in range(36):
        if i in dobry:
            przyciski.append(tk.Button(window_Game, text = 'Press me', command = hit, width = 13, height = 6))
        else:
            przyciski.append(tk.Button(window_Game, text = 'Press me', command = miss, width = 13, height = 6))

    for i in range(6):
        print(i)
        for j in range(6):
            przyciski[i*6+j].grid(column = i, row = j, sticky=tk.W)







def change_to_logged():
    haslo = (Get_From_Db('localhost', 'root', '', 'sapper', "Select password from account where login='{0}'".format(l.get())))
    db_Password = ((haslo)[0])[0]

    if p.get() == db_Password:
        label_text.set("You're logged")
        global  x_logged
        x_logged = True
        global button_Start_Game
        button_Start_Game = tk.Button(window, text = "Start Game", width = 30, command = start_Game)
        button_Start_Game.place(x = 90, y = 280)


def show_Score():
    score_text = tk.StringVar()
    score = tk.Entry(window, textvariable = score_text)
    score.place(x = 150, y = 240)

    if x_logged:
        score_var = (Get_From_Db('localhost', 'root', '', 'sapper', "SELECT points from points, account where account.login='{0}' and points.id=account.id".format(l.get())))
        score_text.set("Your score is: " + str((score_var[0])[0]))
    else:
        score_text.set("you're not logged")




def log_Out():
    global x_logged
    x_logged=False
    label_text.set("Please Log in:")
    button_Start_Game.destroy()

def register():

    global counter
    print(counter)
    if counter == 0:


        global l_reg, l_reg2, p_reg
        l_reg = tk.StringVar()
        l_reg2 = tk.StringVar()
        p_reg = tk.StringVar()
        window_Register = tk.Toplevel()
        window_Register.focus_set()
        window_Register.grab_set()
        login_reg = tk.Entry(window_Register, textvariable=l_reg)


        button_Register_on_Register = tk.Button(window_Register, text = "Register", width = 10, command = register_In_DB)

        window_Register.winfo_toplevel().title('Register menu')
        window_Register.geometry('300x300')
        counter += 1
        print(counter)




        Please_Register_In_Text = tk.Label(window_Register, text = 'Register', font = ("Arial", 22))
        Please_Register_In_Text.place(x = 80, y = 20)


        login_reg.place(x = 150, y = 80)


        login_reg2 = tk.Entry(window_Register, textvariable = l_reg2)
        login_reg2.place(x = 150, y = 105)


        password_reg = tk.Entry(window_Register, show = '*', textvariable = p_reg)
        password_reg.place(x = 150, y = 130)

        Label_Login_Text_reg = tk.Label(window_Register, text = 'Login:')
        Label_Login_Text_reg.place(x = 90, y = 80)

        Label_Login_Text_reg2 = tk.Label(window_Register, text = 'Repeat Login:')
        Label_Login_Text_reg2.place(x = 70, y = 105)

        Password_Text_reg = tk.Label(window_Register, text = 'Password:')
        Password_Text_reg.place(x = 85, y = 130)

        button_Register_on_Register.place(x = 180, y = 200)



        window_Register.mainloop()
    else:
        pass



button_Log = tk.Button(window, text = "Log in", width = 10, command = change_to_logged)
button_Log.place(x = 120, y = 140)

button_Register = tk.Button(window, text = "Register", width = 10, command = register)
button_Register.place(x = 280, y = 140)

button_refresh = tk.Button(window, text = "Refresh", width = 10, command = show_Score)
button_refresh.place(x = 170, y = 200)

button_LogOut = tk.Button(window, text = "Log out", width = 10, command = log_Out)
button_LogOut.place(x = 200, y = 140)

window.mainloop()
