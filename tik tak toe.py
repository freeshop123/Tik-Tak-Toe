from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("TicTacTo")

clicked = True
count = 0

def disabe_all_button():
    b1.config(text=" ")
    b2.config(text=" ")
    b3.config(text=" ")
    b4.config(text=" ")
    b5.config(text=" ")
    b6.config(text=" ")
    b7.config(text=" ")
    b8.config(text=" ")
    b9.config(text=" ")

    b1.config(bg="gray")
    b2.config(bg="gray")
    b3.config(bg="gray")
    b4.config(bg="gray")
    b5.config(bg="gray")
    b6.config(bg="gray")
    b7.config(bg="gray")
    b8.config(bg="gray")
    b9.config(bg="gray")

    global clicked, count
    clicked = True
    count = 0

def checkwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(background="red")
        b2.config(background="red")
        b3.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(background="red")
        b5.config(background="red")
        b6.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(background="red")
        b8.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(background="red")
        b4.config(background="red")
        b7.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(background="red")
        b5.config(background="red")
        b8.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(background="red")
        b6.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(background="red")
        b5.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(background="red")
        b5.config(background="red")
        b7.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "X győzött")
        disabe_all_button()

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(background="red")
        b2.config(background="red")
        b3.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(background="red")
        b5.config(background="red")
        b6.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(background="red")
        b8.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(background="red")
        b4.config(background="red")
        b7.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(background="red")
        b5.config(background="red")
        b8.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(background="red")
        b6.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()

    if count == 9 and winner == False:
        messagebox.showinfo("tic tac toe", "Döntetlen")
        disabe_all_button()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(background="red")
        b5.config(background="red")
        b9.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(background="red")
        b5.config(background="red")
        b7.config(background="red")
        winner = "True"
        messagebox.showinfo("tic tac toe", "O győzött")
        disabe_all_button()

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"]= "X"
        clicked = False
        count += 1
        checkwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Ez a mező már foglalt")

b1 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b1))
b2 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b2))
b3 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b3))

b4 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b4))
b5 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b5))
b6 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b6))

b7 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b7))
b8 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b8))
b9 = Button(root, text=" ", heigh=4, width=7, fg="white", bg="gray", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

root.mainloop()