#importing
import mysql.connector
import tkinter as tk


def QueryToDb(your_host, your_user, your_password, db, query):
    try:
        db = mysql.connector.connect(host=your_host, user=your_user, password=your_password, database=db )
        mycursor = db.cursor()
        mycursor.execute(query)
    except:
        print("launch db")
    return mycursor.fetchall()

counter=0

window=tk.Tk()
window.winfo_toplevel().title('Sapper')
window.geometry('400x400')

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
    haslo=(QueryToDb('localhost', 'root', '', 'sapper', "Select password from account where login='{0}'".format(l.get())))
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
        score_var = (QueryToDb('localhost', 'root', '', 'sapper', "SELECT points from points, account where account.login='{0}' and points.id_points=account.id".format(l.get())))
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
        global windowRegister
        windowRegister = tk.Tk()
        windowRegister.winfo_toplevel().title('Register menu')
        windowRegister.geometry('300x300')
        counter += 1
        print(counter)
        #windowRegister.mainloop()
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
