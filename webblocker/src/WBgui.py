from Tkinter import *


def clear_entry(event, entry):
    entry.delete(0, END)

#setting up application window
window = Tk()
window.title("FOCUS")
window.geometry("500x400")
window.wm_iconbitmap('fc.ico')
background_image=PhotoImage(file="dj.gif")
background_label =Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#setting up titles and labels
Title = Label(window, text="Focus WebBlocker", fg="#383a40", font=("Helvetica",18))
instr1 = Label(window, text= "Enter the websites to be blocked", font=("Helvetica", 13))
entInstr1 = Entry(window, fg="#273746", insertwidth="5")
instr2 = Label(window, text= "Enter your working hours", font=("Helvetica", 13))
entInstr2 = Entry(window, fg="#273746", insertwidth="5")

#allows entry to have a default text
entInstr1.insert(0, 'facebook,yahoo,youtube,....')
entInstr2.insert(0, 'Ex: 2:30-22:40')
#that gets erased after a mouse click
entInstr1.bind("<Button-1>", lambda event: clear_entry(event, entInstr1))
entInstr2.bind("<Button-1>", lambda event: clear_entry(event, entInstr2))

#oraganizing the labels
#Title.pack(pady=(50,40))
instr1.pack(pady=(160,3))
entInstr1.pack(fill=X, padx=50)
instr2.pack(pady=(20,3))
entInstr2.pack()
#Buttons
blockbtn=Button(window, text="Block", fg="#000000", font=("Helvetica",10))
blockbtn.config(height=3, width=10)
blockbtn.pack(side=LEFT, padx=(155,6), pady=0)
cancelbt=Button(window, text="Cancel", fg="#000000", font=("Helvetica",10))
cancelbt.config(height=3, width=10)
cancelbt.pack(side=LEFT )

window.mainloop()