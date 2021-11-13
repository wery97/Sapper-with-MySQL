#importing
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *

def GetFromDb(your_host, your_user, your_password, db, query):
    try:
        dbFrom = mysql.connector.connect(host=your_host, user=your_user, password=your_password, database=db )
        mycursorFrom = dbFrom.cursor()
        mycursorFrom.execute(query)
    except:
        print("launch db")
    return mycursorFrom.fetchall()

def GetToDb(your_host, your_user, your_password, db, query):
    try:
        dbTo = mysql.connector.connect(host=your_host, user=your_user, password=your_password, database=db )
        mycursorTo = dbTo.cursor()
        mycursorTo.execute(query)
        dbTo.commit()
    except:
        print("launch db")



window=tk.Tk()
window.winfo_toplevel().title('Sapper')
window.geometry('400x400')



def registerInDB():
    print(l_reg.get())
    print(l_reg2.get())
    print(p_reg.get())
    print("Insert into account values (NULL, '{0}', '{1}')".format(l_reg.get(), p_reg.get()))
    if l_reg.get() == l_reg2.get():
        try:
            (GetToDb('localhost', 'root', '', 'sapper', "Insert into account values (NULL, '{0}', '{1}')".format(l_reg.get(), p_reg.get())))
            (GetToDb('localhost', 'root', '', 'sapper', "insert into points VALUES (NULL,(select id from account order by id DESC limit 1),0)"))

            messagebox.showinfo("Information", "You've registered properly")
        except:
            print("jakis blad")


counter=0

x_logged=False

label = tk.Label( window, text = "Select position without the bomb" )
label.pack( side = tk.BOTTOM )

l=tk.StringVar()
login=tk.Entry(window, textvariable=l)
login.place(x=150, y=80)

p=tk.StringVar()
password=tk.Entry(window,show='*', textvariable=p)
password.place(x=150, y=105)

LabelLoginText = tk.Label(window, text='Login:')
LabelLoginText.place(x=90,y=80)

PasswordText = tk.Label(window, text = 'Password:')
PasswordText.place(x = 85, y = 105)

labeltext = tk.StringVar()
labeltext.set("Please Log in:")

PleaseLogInText=tk.Label(window, textvariable=labeltext, font=("Times New Roman", 20))
PleaseLogInText.place(y = 30, x = 140)


def startGame():
    print("gra sie zaczela")


def changetologged():
    haslo=(GetFromDb('localhost', 'root', '', 'sapper', "Select password from account where login='{0}'".format(l.get())))
    dbPassword=((haslo)[0])[0]

    if p.get() == dbPassword:
        labeltext.set("You're logged")
        global  x_logged
        x_logged = True
        global button_StartGame
        button_StartGame = tk.Button(window, text="Start Game", width=30, command=startGame)
        button_StartGame.place(x=90, y=280)


def showScore():
    score_text = tk.StringVar()
    score = tk.Entry(window, textvariable=score_text)
    score.place(x=150, y=240)

    if x_logged:
        score_var = (GetFromDb('localhost', 'root', '', 'sapper', "SELECT points from points, account where account.login='{0}' and points.id=account.id".format(l.get())))
        print(score_var)
        score_text.set("Your score is: "+str((score_var[0])[0]))
    else:
        score_text.set("you're not logged")




def logOut():
    global x_logged
    x_logged=False
    labeltext.set("Please Log in:")
    button_StartGame.destroy()

def register():

    global counter
    print(counter)
    if counter==0:


        global l_reg, l_reg2, p_reg
        l_reg = tk.StringVar()
        l_reg2 = tk.StringVar()
        p_reg = tk.StringVar()
        windowRegister = tk.Toplevel()
        windowRegister.focus_set()
        windowRegister.grab_set()
        login_reg = tk.Entry(windowRegister, textvariable=l_reg)


        button_RegisteronRegister = tk.Button(windowRegister, text="Register", width=10, command=registerInDB)

        windowRegister.winfo_toplevel().title('Register menu')
        windowRegister.geometry('300x300')
        counter += 1
        print(counter)




        PleaseRegisterInText = tk.Label(windowRegister, text='Register', font=("Times New Roman", 22))
        PleaseRegisterInText.place(x=80, y=20)


        login_reg.place(x=150, y=80)


        login_reg2 = tk.Entry(windowRegister, textvariable=l_reg2)
        login_reg2.place(x=150, y=105)


        password_reg = tk.Entry(windowRegister, show='*', textvariable=p_reg)
        password_reg.place(x=150, y=130)

        LabelLoginText_reg = tk.Label(windowRegister, text='Login:')
        LabelLoginText_reg.place(x=90, y=80)

        LabelLoginText_reg2 = tk.Label(windowRegister, text='Repeat Login:')
        LabelLoginText_reg2.place(x=70, y=105)

        PasswordText_reg = tk.Label(windowRegister, text='Password:')
        PasswordText_reg.place(x=85, y=130)

        button_RegisteronRegister.place(x=180, y=200)



        windowRegister.mainloop()
    else:
        pass



button_Log = tk.Button(window, text="Log in", width=10, command=changetologged)
button_Log.place(x=120, y= 140)

button_Register = tk.Button(window, text="Register", width=10, command=register)
button_Register.place(x=280, y= 140)

button_refresh = tk.Button(window, text="Refresh", width=10, command=showScore)
button_refresh.place(x=170, y= 200)

button_LogOut = tk.Button(window, text="Log out", width=10, command=logOut)
button_LogOut.place(x=200, y= 140)

window.mainloop()
