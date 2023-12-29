from tkinter import *
import random

root = Tk()
root.title("Testing Random Function")
root.geometry("400x400")

guessed_password_label = Label(root)
generated_password_label = Label(root)

entry_word = Entry(root)

array_3d = [[["I", "J", "K", "L", "M", "N", "O", "P"], ["King", "Queen"], ["!", "@", "#", "$", "%", "^", "&", "*"]]]
print(array_3d[0][2][3])

def new_password():
    guessed_password_label["text"] = "Guessed Password : " + entry_word.get()
    
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    
    letter1 = (array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    
    generated_password_label["text"] = "Generated Password : " + letter1 + "" + letter2 + "" + letter3
    
entry_word.place(relx= 0.5, rely= 0.3, anchor=CENTER)

guessed_password_label.place(relx= 0.5, rely= 0.4, anchor=CENTER)
    
btn = Button(root, text = "New Password", command = new_password, bg = "blue", fg = "white")
btn.place(relx= 0.5, rely= 0.5, anchor=CENTER)

generated_password_label.place(relx= 0.5, rely= 0.6, anchor=CENTER)

root.mainloop()

