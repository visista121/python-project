from tkinter import *

#contactbook window
root = Tk()
root.geometry('400x400')
root.config(bg = 'thistle1')
root.title('Contact Book')

contactlist = [
    ['rida',  '9176738493'],
    ['David ',  '7684430000'],
    ['kabir',   '8438354432'],
    ['naina','6834552341'],
    ['sakshi',   '9648512689'],
    ['Johana' , '9819876543'],
    ['radika' , '9596876893'],
    ['sindu' , '7439876543'],
    ['stela' , '8149876234'],
    ['sid' , '8943876523'],
    ['salim' , '9866601529'],
    ['arush' , '7241876983'],
    ['amyra' , '8681876543'],
    ['joseph' , '9523687413'],
    ['rohan' , '8688787384'],
    ]

Name = StringVar()
Number = StringVar()

#create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#this function returns contact selected by cursor

def Selected():
    return int(select.curselection()[0])

    
#adding a contact
def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()


#editing existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()

    
#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()

   
# to view selected contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def EXIT():
    root.destroy()


#empty name and number field
def RESET():
    Name.set('')
    Number.set('')



def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


#labels and entry widget
Label(root, text = 'NAME', font='arial 12 bold', bg = 'peachpuff').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='arial 12 bold',bg = 'peachpuff').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)



#define buttons 
Button(root,text=" ADD", font='arial 12 bold',bg='snow3', command = AddContact).place(x= 50, y=110)
Button(root,text="EDIT", font='arial 12 bold',bg='snow3',command = EDIT).place(x= 50, y=260)
Button(root,text="DELETE", font='arial 12 bold',bg='snow3',command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", font='arial 12 bold',bg='snow3', command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 300, y=320)
Button(root,text="RESET", font='arial 12 bold',bg='snow3', command = RESET).place(x= 50, y=310)


root.mainloop()