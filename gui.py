from tkinter import *
import game_logic as gl
# Create the main window
window = Tk()
window.title("AI-ASSIGNEMENT GAME")
window.geometry('500x500')
window.configure(bg='black')
window.tk.call('tk', 'scaling', 3.0)

#Define the actions
lbl = Label(window, text="choose the starting number", font=("Arial Bold", 6), bg='black', fg='white', padx=3, pady=2)
lbl.grid(column=0, row=0)

#chosing the number
numbers = gl.generate_numbers()
spinboxNumber = Spinbox(window, values=numbers, width=5, font=("Arial Bold", 6))
spinboxNumber.grid(column=1, row=0, padx=3, pady=2)

def ChosenNumber():
    lblChosenNumber = Label(window, text="You have chosen the number: "+spinboxNumber.get(), font=("Arial Bold", 6), bg='black', fg='white')
    lblChosenNumber.grid(column=0, row=2)
    btnChosenNumber.destroy()
    return spinboxNumber.get()

btnChosenNumber=Button(window, command=ChosenNumber, text="Choose", bg='black', fg='white',font=("Arial Bold", 6))
btnChosenNumber.grid(column=3,row=0, padx=3, pady=2)


#cancel button
#btnCancel = Button(window, command=window.destroy, text="Cancel", bg='black', fg='white',font=("Arial Bold", 6))
#btnCancel.grid(column=3,row=2, padx=3, pady=2)

#Main loop ?



window.mainloop()

