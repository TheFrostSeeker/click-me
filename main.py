from tkinter import *

global easy_clicking, medium_clicking, hard_clicking
easy_clicking = 0
medium_clicking = 0
hard_clicking = 0

def easy_click():
    global easy_clicking
    easy_clicking += 1
    myLabel = Label(root, text="Look I clicked {} times !".format(easy_clicking))
    myLabel.grid(row=1, column=0)
def medium_click():
    global medium_clicking
    medium_clicking += 1
    myLabel = Label(root, text="Look I clicked {} times !".format(medium_clicking))
    myLabel.grid(row=1, column=1)
def hard_click():
    global hard_clicking
    hard_clicking += 1
    myLabel = Label(root, text="Look I clicked {} times !".format(hard_clicking))
    myLabel.grid(row=1, column=2)

if __name__ == '__main__':
    root = Tk()
    root.title("Simple tests")

    easy = Button(root, text="EASY", padx=50, pady=50, command=easy_click, fg="black", bg="green")
    medium = Button(root, text="MEDIUM", padx=45, pady=50, command=medium_click, fg="black", bg="yellow")
    hard = Button(root, text="HARD", padx=50, pady=50, command=hard_click, fg="black", bg="red")

    easy.grid(row=0, column=0)
    medium.grid(row=0, column=1)
    hard.grid(row=0, column=2)

    root.mainloop()