import tkinter
from tkinter import Button, Entry, END, Text, Spinbox, IntVar, Checkbutton, Radiobutton, Scale, Listbox

window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label
my_label=tkinter.Label(text="I Am A Label",font=("Arial",20,"bold"))
my_label.pack()

#Update label text
my_label["text"]="New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    new_text=entry.get()
    my_label.config(text=new_text)

button=Button(text="Click Me",command=button_clicked)
button.pack()

#Entry
entry= Entry(width=30)
entry.insert(END,string="Some text to begin with")
print(entry.get())
entry.pack()

#Text
text=Text(height=5,width=30)

#Puts cursor in textbox
text.focus()

#Add some text to begin with
text.insert(END,"Example of multi-line text entry")

#Gets current value in textbox at line 1,character 0
print(text.get("1.0"),END)
text.pack()

#Spinbox
#gets the current value in spinbox
def spinbox_used():
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value
def scale_used(value):
    print(value)
scale=Scale(from_=0,to=100,command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if on button clicked, otherwise 0
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on
checked_state=IntVar()
checkbutton=Checkbutton(text="Is On?",variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked
radio_state=IntVar()
radiobutton1=Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radiobutton2=Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    #Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox=Listbox(height=4)
fruits=["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

#Keep the window open
window.mainloop()