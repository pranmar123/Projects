#Making a calculator

#importing the system and tkinter; import * means import all of it
import sys
from tkinter import *

#Adding pre code to button so you can click on them and then later intergrating it to the buttons itself

def cb(bs):    #cb=click on button, bs=whatever the button equals (button stuff)
    global bd #bd= stres and accumulates recieved button data
    bd=bd+str(bs) #bd= bd + the new button stuff
    tv.set(bd) #at some point you will want to clear out button data (bd)

#Defining the function for button clear
def klr():
    global bd #the accumulator of all btn data sent to cb()
    bd=""  #sets bd to nothing
    tv.set(bd) #tv variable is bound to the text box: "textvariable" from earlier

#Defining the clear button
def eqf():
    global bd #the accumulator of all btn data sent to cb()
    bd= eval(bd) #evaluates strings
    tv.set(bd)
    bd=""

#Creates the window
root = Tk() #This creates the window
root.title("Calculator by Pranay V.1") #title of the program
tv=StringVar()
global bd
bd=""

#Create the textbox to where we will type in number
#Textbox variable: tb
tb = Entry(root,font=("arial",12,"bold"), #Access root, and assign font,and conditions. NOTE: commas are used to sepearate
           textvariable= tv, #You bind it so that whatever happens to tv also happens to textvariable
           bd=15, #border
           insertwidth=3, #blinkingcursor
           bg= "lightgreen", #backgroundcolor
           justify="right").grid(columnspan=4) #justify is where you type in; grid adds a grid box and makes it the 3 columns wide
tv.set("0.00") #Prints out 0.00 as the default value in the textbox where numbers go


#Add buttons to the keypad

    #First row
btn7=Button(root,padx=5,bd=8, #Adds button to root window; padx is the space in text 7 and the border in 7 on the calculator; bd= lentgh borderline
            fg="black",font=("arial",20,"bold"), #fg=foreground chooses the color of the button; font;
            text="7",
            command=lambda:cb(7)).grid(row=1, column=0) #sets cb to buttonnumber
            #.grid row=1... etc function = goes back to the grid that was defined in line19 and acesses it and puts it on column0
btn8=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="8",
            command=lambda:cb(8)).grid(row=1, column=1) #basically it sees lambda function and says i have to call cb and assign 8 to it
btn9=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="9",
            command=lambda:cb(9)).grid(row=1, column=2)

divbtn=Button(root,padx=5,bd=8,  #adding division button
            fg="black",font=("arial",20,"bold"),
            text="/",
            command=lambda:cb("/")).grid(row=1, column=3) #NOTE symbols need "" in cb
#Row2
btn4=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="4",
            command=lambda:cb(4)).grid(row=2,column=0)
btn5=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="5",
            command=lambda:cb(5)).grid(row=2,column=1)
btn6=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="6",
            command=lambda:cb(6)).grid(row=2,column=2)
mulbtn=Button(root,padx=5,bd=8,  #adding multiplication button
            fg="black",font=("arial",20,"bold"),
            text="*",
              command=lambda:cb("*")).grid(row=2,column=3)

#Row3
btn1=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="1",
            command=lambda:cb(1)).grid(row=3,column=0)
btn2=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="2",
            command=lambda:cb(2)).grid(row=3,column=1)
btn3=Button(root,padx=5,bd=8,
            fg="black",font=("arial",20,"bold"),
            text="3",
            command=lambda:cb(3)).grid(row=3,column=2)
subtn=Button(root,padx=5,bd=8,  #adding subtraction button
            fg="black",font=("arial",20,"bold"),
            text="-",
             command=lambda:cb("-")).grid(row=3,column=3)

#Row4
btn0=Button(root,padx=5,bd=8, #making this bigger because button 0 is bigger in calculator
            fg="black",font=("arial",20,"bold"),
            text="0",
            command=lambda:cb(0)).grid(row=4,column=0)
decbtn=Button(root,padx=5,bd=8,  #adding decimal button
            fg="black",font=("arial",20,"bold"),
            text=".",
            command=lambda:cb(".")).grid(row=4,column=1)
addbtn=Button(root,padx=5,bd=8,  #adding addition button
            fg="black",font=("arial",20,"bold"),
            text="+",
            command=lambda:cb("+")).grid(row=4,column=2)

eqbtn=Button(root,padx=5,bd=8,  #adding equal button
            fg="black",font=("arial",20,"bold"),
            text="=",
            command=lambda:eqf()).grid(row=4,column=3)

klrbtn=Button(root,padx=5,bd=8,
              fg="black",font=("arial", 20, "bold"),
              text="Clear",
              command=lambda:klr()).grid(row=4,column=4)
root.mainloop()
