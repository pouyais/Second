from tkinter import *
from tkinter import messagebox 



# ===== Function =====

# ===== def Insert =====
def insert(*event):
    name = ent_name.get()
    lastname = ent_lastname.get()
    city = ent_city.get()
    tel = int(ent_tel.get())
    lst_contact.insert(END,f"{name},{lastname},{city},{tel}")
    clear()
    ent_name.focus_set()
    
    
# ===== def Delete =====
def delete():
    mbox = messagebox.askyesno(title="Delete",message="Do you want to delete this item?")
    if mbox == True:
        lst_contact.delete(lst_contact.curselection())
    else:
        pass
    
    
# ===== def Clear =====
def clear():
    ent_name.delete(0,END)
    ent_lastname.delete(0,END)
    ent_city.delete(0,END)
    ent_tel.delete(0,END)
    

# ===== def Fetch =====
def fetch():
    data = lst_contact.get(lst_contact.curselection()).split(",")
    ent_name.insert(0,data[0])
    ent_lastname.insert(0,data[1])
    ent_city.insert(0,data[2])
    ent_tel.insert(0,data[3])
    lst_contact.delete(lst_contact.curselection())
    
    
# ===== def Exit =====
def exit():
    mbox = messagebox.askyesno(title="Exit",message="Do you want to exit the program?")
    if mbox == True:
        root.destroy()
    else:
        pass

    



# ===== UI Design =====
root = Tk()
root.geometry("800x500+400+100")
root.title("Contact Management")
root.config(bg="grey")
root.resizable(0,0)





# ===== Labels =====
lbl_name = Label(root,font="Arial 14 bold",text="Name : ",bg="grey")
lbl_name.place(x=50,y=50)


lbl_lastname = Label(root,font="Arial 14 bold",text="Lastname : ",bg="grey")
lbl_lastname.place(x=400,y=50)


lbl_city = Label(root,font="Arial 14 bold",text="City : ",bg="grey")
lbl_city.place(x=50,y=150)


lbl_tel = Label(root,font="Arial 14 bold",text="Tel-number : ",bg="grey")
lbl_tel.place(x=390,y=150)





# ===== Entry =====
ent_name = Entry(root,font="Arial 14 bold",bg="#E6E6E6")
ent_name.bind("<Return>",insert)
ent_name.place(x=130,y=50)


ent_lastname = Entry(root,font="Arial 14 bold",bg="#E6E6E6")
ent_lastname.bind("<Return>",insert)
ent_lastname.place(x=520,y=50)


ent_city = Entry(root,font="Arial 14 bold",bg="#E6E6E6")
ent_city.bind("<Return>",insert)
ent_city.place(x=130,y=150)


ent_tel = Entry(root,font="Arial 14 bold",bg="#E6E6E6")
ent_tel.bind("<Return>",insert)
ent_tel.place(x=520,y=150)





# ===== ListBox =====
lst_contact = Listbox(root,font="Arial 14 bold",width=28,bg="#E6E6E6")
lst_contact.place(x=50,y=210)





# ===== Buttons =====
btn_insert = Button(root,text="Insert",font="Arial 14 bold",width=10,command=insert)
btn_insert.place(x=530,y=210)


btn_delete = Button(root,text="Delete",font="Arial 14 bold",width=10,command=delete)
btn_delete.place(x=530,y=260)


btn_clear = Button(root,text="Clear",font="Arial 14 bold",width=10,command=clear)
btn_clear.place(x=530,y=310)


btn_fetch = Button(root,text="Fetch",font="Arial 14 bold",width=10,command=fetch)
btn_fetch.place(x=530,y=360)


btn_exit = Button(root,text="Exit",font="Arial 14 bold",width=10,command=exit)
btn_exit.place(x=530,y=410)





root.mainloop()