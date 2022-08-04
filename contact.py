from tkinter import * 

#creation of contactbook window
root = Tk()
root.geometry('500x500')
root.config(bg = 'thistle1')
root.title('Contact Book')

contactlist = [
    ['rida',  '9176738493', '11-13-1764, Bay road'],
    ['david ',  '7684430000', '2-14-8623, Street no: 06'],
    ['kabir',   '8438354432', '12-03-1548, Vegas'],
    ['naina','6834552341', '12-15-1489, Maple road'],
    ['sakshi',   '9648512689', '15-12-1364, Street no: 12'],
    ['johana' , '9819876543', '12-14-1896, Beside Theresa Statue'],
    ['radika' , '9596876893', '16-12-1523, Fling road'],
    ['sindu' , '7439876543', '12-16-1987, Bakes Street'],
    ['stela' , '8149876234', '15-12-8946, Street no: 03'],
    ['arush' , '7241876983', '16-07-5623, Rocks Street'],
    ['amyra' , '8681876543', '15-14-1785, Salsa Road'],
    ['joseph' , '9523687413','12-16-4879, Street no: 10'],
    ]

Name = StringVar()
Number = StringVar()

#create frame
frame = Frame(root)
frame.pack(side = RIGHT)

#represents contact names
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=15)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#this function returns contact selected by cursor

def Selected():
    return int(select.curselection()[0])

    
#adding a contact
def AddContact():
    contactlist.append([Name.get(), Number.get(), address.get(1.0, "end-1c")])
    print('Added new contact')
    Select_set()


#editing existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), address.get(1.0, "end-1c")]
    print('Edited Successfully')
    Select_set()

    
#to delete selected contact
def DELETE():
    del contactlist[int(select.curselection()[0])]
    print('contact deleted')
    Select_set()

   
# to view selected contact
def VIEW():
    Name.set(contactlist[int(select.curselection()[0])][0])
    Number.set(contactlist[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0, contactlist[int(select.curselection()[0])][2])


def EXIT():
    root.destroy()


#empty name and number field
def RESET():
    Name.set('')
    Number.set('')
    address.delete(1.0,"end")


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,add in contactlist :
        select.insert (END, name.upper())
Select_set()


#labels and entry widget
frame = Frame()
frame.pack(pady=10)
  
frame1 = Frame()
frame1.pack()
  
frame2 = Frame()
frame2.pack(pady=10)
  
Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()
  
Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()
  
Label(frame2, text = 'Address', font='arial 12 bold').pack(side=LEFT)
address = Text(frame2,width=37,height=3)
address.pack()



#define buttons 
Button(root,text=" ADD", font='arial 12 bold',bg='snow3', command = AddContact).place(x= 150, y=150)
Button(root,text="EDIT", font='arial 12 bold',bg='snow3',command = EDIT).place(x= 150, y=300)
Button(root,text="DELETE", font='arial 12 bold',bg='snow3',command = DELETE).place(x= 150, y=250)
Button(root,text="VIEW", font='arial 12 bold',bg='snow3', command = VIEW).place(x= 150, y=200)
Button(root,text="EXIT", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 200, y=420)
Button(root,text="RESET", font='arial 12 bold',bg='snow3', command = RESET).place(x= 150, y=350)


root.mainloop()
