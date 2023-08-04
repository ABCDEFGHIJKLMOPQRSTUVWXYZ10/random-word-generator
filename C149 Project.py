from tkinter import *
import random

root=Tk()

root.title("Random Word Generator")
root.geometry("500x500")


list1 = ["Yes", "No", "May be", "lets go", "YAY"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_word = list1[random_no]
    print("Random word :" + random_word)

btn1 = Button(root, text = "random word generator", command = random_number)
btn1.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()