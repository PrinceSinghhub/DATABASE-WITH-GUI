from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
root=Tk()
root.title("DataBase With GUI")
root.geometry('720x500')
root.resizable(False, False)

m = Label(root, text="ADMINISTRATOR MODE DATABASE", font="vani 27 bold", fg="gold", bg="gray15",relief=GROOVE, padx=20 )
m.place(x=20, y=30)
o = Label(root, text="FOLLOW THIS COMMAND", font="vani 15 bold", fg="black", bg="skyblue", justify=CENTER)
o.place(x=430, y=150)

Sc = Label(root, text="SEARCH", font="vani 20 bold", fg="black", justify=CENTER)
Sc.place(x=160, y=150)

n = Label(root, text='''
~ SEARCH CREATE DATABASE\n
~ SEARCH UPDATE DATA\n
~ SEARCH RERTIVE DATA\n
~ SEARCH DELETE DATA''',
font=('times', 12, 'bold'), fg='red', justify=LEFT)
n.place(x=430,y=200)

erro = n = Label(root, text='''IMPORTANT NOTE:-\n Please only Search/use for Entere in DATABASE Given Command Not try Other Command\n
otherwise command Not excepted By This Programe.... ''',
font=('times', 12, 'bold'), fg='red', justify=LEFT)
n.place(x=0,y=400)

comm = StringVar()

def createDatabase():
    # import mysql.connector as mc
    nx = Toplevel()
    nx.title("CREATE DATABASE")
    nx.geometry('1920x1080')
    # nx.configure(bg="skyblue")
    m = Label(nx, text="CREATE DATABASE", font="vani 27 bold", fg="gold", bg="gray15", relief=GROOVE,
    padx=20)
    m.place(x=550, y=30)

    TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
    TextBox.place(x=700, y=200)

    # todo create database
    SQL_Quary = StringVar()
    def createDB():

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost',port=3306)
        TC = SQL_Quary.get()
        database = MySql.cursor()
        try:
            database.execute(TC)
            TextBox.insert(END,"Sucessfully DATABASE Created\n")
        except:
            TextBox.insert(END, "Oooops DATABASE Not Created\n")
        database.close()
        MySql.close()

    def showDtabase():
        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        TC = SQL_Quary.get()
        database = MySql.cursor()
        try:
            database.execute(TC)
            TextBox.insert(END, "Your all DATABASES IS:\n")
            for DataBase in database:
                TextBox.insert(END, f"{DataBase}\n")

            TextBox.insert(END, "Sucessfully All DATABASE Fetch\n")
        except:
            TextBox.insert(END, "Oooops DATABASE not Used\n")
        database.close()
        MySql.close()


    # todo database connection
    def conectDATABASE():
        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost',port=3306)
        if MySql.is_connected() == True:
            TextBox.delete('1.0', END)
            TextBox.insert(END, "Sucessfully Connection With DATABASE\n")
        else:
            TextBox.insert(END, "Oppps Connection With DATABASE not Complete\n")

        quary = Label(nx, text="SEARCH", font="vani 20 bold", fg="black", justify=CENTER)
        quary.place(x=160, y=150)

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=200)

        # todo ourCommand Button
        r = Button(nx, fg="white", text="create database", font="Times 20 bold", bg="black", command=createDB)
        r.place(x=150, y=280)


        r = Button(nx, fg="white", text="SHOW DATABASE", font="Times 20 bold", bg="black", command=showDtabase)
        r.place(x=150, y=500)

    r = Button(nx, fg="white", text="Let's Go", font="Times 20 bold", bg="black", command=conectDATABASE)
    r.place(x=160, y=500)
    nx.mainloop()



def insertData():
    nx = Toplevel()
    nx.title("INSERT DATA")
    nx.geometry('1920x1080')
    nx.configure(bg="skyblue")

    TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
    TextBox.place(x=700, y=200)

    Take_Command = StringVar()
    SQL_Quary = StringVar()
    connection = StringVar()

    def CheckCommand():
        if Take_Command.get().lower() == "create table":
            usedataBase()

        if Take_Command.get().lower() == "show tables":
            showTables()

        if Take_Command.get().lower() == "show data":
            showData()

        if Take_Command.get().lower() == "insert data":
            insertData()

        if Take_Command.get().lower() == "update data":
            updateData()

        if Take_Command.get().lower() == "delete table":
            deleteTable()

        else:
            messagebox.showerror("Error", "You Entered Invalid Command Try Again")

    # todo delete table

    def deleteTable():

        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")

        def tableDelet():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()
            TC = SQL_Quary.get()

            try:
                conn.execute(TC)
                MySql.commit()
                TextBox.insert(END, "Table Sucessfully Delete in DataBase\n")
            except:
                TextBox.insert(END, "Oooops Table not Delete in DataBase\n")

            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=400)

        r = Button(nx, fg="white", text="UPDATE DATA ", font="Times 20 bold", bg="black", command=tableDelet)
        r.place(x=60, y=500)
        nx.mainloop()
    # todo update data
    def updateData():
        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")

        def dataupdate():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()
            TC = SQL_Quary.get()

            try:
                conn.execute(TC)
                MySql.commit()
                TextBox.insert(END, "Data updated Sucessfully in Table\n")
            except:
                TextBox.insert(END, "Oooops Data not updated in Table\n")

            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=400)

        r = Button(nx, fg="white", text="UPDATE DATA ", font="Times 20 bold", bg="black", command=dataupdate)
        r.place(x=60, y=500)
        nx.mainloop()
    # todo insert data
    def insertData():
        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        Command_TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        Command_TextBox.place(x=20, y=200)

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            MySql.commit()

            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")

        def dataInsert():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()

            TC = SQL_Quary.get()

            try:
                conn.execute(TC)
                MySql.commit()
                TextBox.insert(END, "SucessFully data insert in Table\n")

            except:
                TextBox.insert(END, "Oooops data not insert in Table\n")
            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=200, y=400)

        r = Button(nx, fg="white", text="INSERT DATA ", font="Times 20 bold", bg="black", command=dataInsert)
        r.place(x=200, y=600)
        nx.mainloop()
    # todo for show Table
    def showTables():
        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            MySql.commit()

            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")

        def showTabels():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()

            TC = SQL_Quary.get()

            try:
                conn.execute(TC)
                TextBox.insert(END, "All Table in Your DATABASE\n")
                for i in conn:
                    TextBox.insert(END, f"{i}\n")

            except:
                TextBox.insert(END, "Oooops not Able to show Tables in DATABASE\n")
            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=400)

        r = Button(nx, fg="white", text="SHOW TABLE ", font="Times 20 bold", bg="black", command=showTabels)
        r.place(x=60, y=600)
        nx.mainloop()

    # todo fetch data from Table
    def showData():
        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            MySql.commit()

            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")

        def fetchdata():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()
            TC = SQL_Quary.get()


            try:
                conn.execute(TC)
                row = conn.fetchall()
                TextBox.insert(END, "Data in Table\n")
                for i in row:
                    TextBox.insert(END, f"{i}\n")
            except:
                TextBox.insert(END, "Oooops not able to show data\n")

            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=400)

        r = Button(nx, fg="white", text="SHOW DATA ", font="Times 20 bold", bg="black", command=fetchdata)
        r.place(x=60, y=500)
        nx.mainloop()

    # todo for create Table
    def usedataBase():
        nx = Toplevel()
        nx.title("INSERT DATA")
        nx.geometry('1920x1080')
        nx.configure(bg="skyblue")

        TextBox = Text(nx, height=25, width=50, font='Verdana 10 bold', fg='#00154f')
        TextBox.place(x=700, y=200)

        MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
        conn = MySql.cursor()
        tk = connection.get()

        try:
            conn.execute(tk)
            MySql.commit()

            TextBox.insert(END, "DATABASE USE SUCCESSFULLY\n")
        except:
            TextBox.insert(END, "DATABASE COULD NOT FOUND\n")


        def createTable():
            MySql = mc.connect(user='root', password='2005@Anushka', host='localhost', port=3306)
            conn = MySql.cursor()
            conn.execute(tk)
            MySql.commit()
            TC = SQL_Quary.get()

            try:
                conn.execute(TC)
                MySql.commit()
                TextBox.insert(END, "Sucessfully Table Create in  DATABASE\n")
            except:
                TextBox.insert(END, "Oooops not Table Create in  DATABASE\n")
            MySql.close()
            conn.close()

        a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=SQL_Quary)
        a.place(x=20, y=400)

        r = Button(nx, fg="white", text="CREATE TABLE ", font="Times 20 bold", bg="black", command=createTable)
        r.place(x=60, y=500)
        nx.mainloop()

    quary = Label(nx, text="Enter Command", font="vani 20 bold", fg="black", justify=CENTER)
    quary.place(x=20, y=70)
    a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=Take_Command)
    a.place(x=20, y=100)

    quary = Label(nx, text="Use DATABASE Name", font="vani 20 bold", fg="black", justify=CENTER)
    quary.place(x=20, y=350)
    a = Entry(nx, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=connection)
    a.place(x=20, y=400)

    r = Button(nx, fg="white", text="CLICK ", font="Times 20 bold", bg="black", command=CheckCommand)
    r.place(x=60, y=155)
    nx.mainloop()




def command():
    Input = comm.get().lower()

    if Input == "create database":
        createDatabase()

    if Input == "retrive data":
        insertData()

    else:
        messagebox.showerror("Error", "You Entered Invalid Command Try Again")


a = Entry(root, font='arial 25 bold', fg='black', justify=CENTER, relief=GROOVE, textvariable=comm)
a.place(x=20, y=200)
r= Button(root, fg= "white", text="Let's Go", font="Times 20 bold",bg= "black", command = command)
r.place(x= 160, y=280)
root.mainloop()
