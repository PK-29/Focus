from Tkinter import *
#initializing windows frame
frame = Tk("WebBlock")
buttonf=Tk()

#making texts in windows frame
label1 = Label(frame, text="name")
label2 = Label(frame, text="Password")
cb = Checkbutton(frame, text="Keep me logged in")

#making user entries in windows frame
entry1 = Entry(frame)
entry2 = Entry(frame)

#organizing labels in the frame using grid method
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
def logined():
    print ("logged in")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
cb.grid(columnspan=2)
login = Button(frame, text="login", bg="red",fg="black", command=logined())
login.grid(columnspan=2)


#using the pack method to create buttons and organizing on frame
topFrame = Frame(buttonf)
topFrame.pack()
bottomFrame = Frame(buttonf)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="One", fg="red")
button2 = Button(topFrame, text="two", fg="green")
button3 = Button(topFrame, text="three", fg="blue")
button4 = Button(bottomFrame, text="four", fg="orange")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

frame.mainloop()
