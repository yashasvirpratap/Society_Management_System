import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tokenize import Name
from views import *

getmid = random.randint(0,10000)

from pkg_resources import resource_listdir

#colors
co0 = "#ffffff"
co1 = "#D9D9D9"
co2 = "#48BDDF"
co3 = "#222E35"
co4 = "#ffffff"

window = Tk ()
window.title ("Society Management")
window.geometry('610x600')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)


#frames
frame_up = Frame(window, width=610, height=50, bg=co3)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=610, height=230, bg=co4)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=600, height=400, bg=co4, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=5, pady=1, sticky=NW)



#functions

def show():
    global tree

    list_header =['MID', 'Name', 'Gender', 'Flat No.', 'Telephone', 'Email']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text='MID', anchor=NW)
    tree.heading(1, text='Name', anchor=NW)
    tree.heading(2, text='Gender', anchor=NW)
    tree.heading(3, text='Flat No.', anchor=NW)
    tree.heading(4, text='Telephone', anchor=NW)
    tree.heading(5, text='Email', anchor=NW)
    # tree.heading(0, text='MID', anchor=NW)

    #tree_columns
    tree.column(0, width=100, anchor='nw')
    tree.column(1, width=80, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=100, anchor='nw')
    tree.column(4, width=100, anchor='nw')
    tree.column(5, width=100, anchor='nw')

    for item in demo_list:
        tree.insert('','end', values=item)

show()

def insert():

    MID = getmid
    Name = e_name.get()
    Gender = e_gender.get()
    Flatno = e_flatno.get()
    Telephone = e_telephone.get()
    Email = e_email.get()

    data = [MID, Name, Gender, Flatno, Telephone, Email]
    if Name == '' or Gender == '' or Telephone== '' or Flatno== '' or Email== '':
        messagebox.showwarning('data', 'Please fill in all fields')
    else:
        add(data)
        messagebox.showinfo('data', 'Data added successfully!')
        e_name.delete(0, 'end')
        e_gender.delete(0, 'end')
        e_flatno.delete(0, 'end')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')

        show()
    

def to_update():
        
        try:
            tree_data = tree.focus()
            tree_dictionary = tree.item(tree_data)
            tree_list = tree_dictionary['values']

            MID = str(tree_list[0])
            Name = str(tree_list[1])
            Gender = str(tree_list[2])
            Flatno = str(tree_list[3])
            Telephone = str(tree_list[4])
            Email = str(tree_list[5])

            # MID.insert(0, MID)
            e_name.insert(0, Name)
            e_gender.insert(0, Gender)
            e_flatno.insert(0, Flatno)
            e_telephone.insert(0, Telephone)
            e_email.insert(0, Email)

            def confirm():
                new_MID = MID
                new_name = e_name.get()
                new_gender= e_gender.get()
                new_flatno= e_flatno.get()
                new_telephone= e_telephone.get()
                new_email= e_email.get()

                data = [new_MID, new_name, new_gender, new_flatno, new_telephone, new_email]

                update(data)

                messagebox.showinfo('Success', 'data updated successfully')

                e_name.delete(0, 'end')
                e_gender.delete(0, 'end')
                e_flatno.delete(0, 'end')
                e_telephone.delete(0, 'end')
                e_email.delete(0, 'end')

                for widget in frame_table.winfo_children():
                    widget.destroy()

                b_confirm.destroy()

                show()
                
            b_confirm =  Button(frame_down, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
            b_confirm.place(x = 290, y = 110)

        except IndexError:
            messagebox.showerror('Error', 'Select one of them from the table')
    
def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_MID = str(tree_list[0])

        remove(tree_MID)

        messagebox.showinfo('Success', 'Data deleted successfully!')

        for widget in frame_table.winfo_children():
            widget.destroy()

        show()


    except IndexError:
        messagebox.showerror('Error', 'Data deletion failed! Check details!')


def to_search():
    MID = e_search.get()

    data = search(MID)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)
        
    e_search.delete(0, 'end')


#frame_up widgets

app_name = Label(frame_up, text= "Society Management System", height=1, font=('Verdana 14 bold'), bg= co3, fg = co0)
app_name.place(x=10, y=10)

#frame_down widgets
# l_mid = Label(frame_down, text="MID", width=20, height=1, font=('Ivy 10'), bg=co4, anchor=NW)
# l_mid.place(x=10, y=20)
# e_mid =  Label(frame_down, text=getmid, width=20, height=1, font=('Ivy 10'), bg=co4, anchor=NW)
# e_mid.place(x=100, y=20)

l_name = Label(frame_down, text="Name *", width=20, height=1, font=('Ivy 10'), bg=co4, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=100, y= 20)

l_gender = Label(frame_down, text="Gender *", width=20, height=1, font=('Ivy 10'), bg=co4, anchor=NW)
l_gender.place(x=10, y=50)
e_gender = ttk.Combobox(frame_down, width=27)
e_gender['values'] =['', 'F', 'M']
e_gender.place(x=100, y= 50)

l_flatno = Label(frame_down, text="Flat No. *", height=1, font=('Ivy 10'), bg=co4, anchor=NW)
l_flatno.place(x=10, y=80)
e_flatno = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_flatno.place(x=100, y= 80)

l_telephone = Label(frame_down, text="Telephone *", height=1, font=('Ivy 10'), bg=co4, anchor=NW)
l_telephone.place(x=10, y=110)
e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_telephone.place(x=100, y= 110)

l_email = Label(frame_down, text="Email *", height=1, font=('Ivy 10'), bg=co4, anchor=NW)
l_email.place(x=10, y=140)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=100, y= 140)

#buttons
# l_search = Label(frame_down, text="Search", height=1, font=('Ivy 10'), bg=co4, anchor=NW)
# l_search.place(x=350, y=20)
b_search = Button(frame_down, text="Search", height=1, width=10, bg= co2, fg=co0, font=('Ivy 8 bold'), command=to_search)
b_search.place(x=500, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=350, y=20)

# l_searchf = Label(frame_down, text="Search By Flat Number", height=1, font=('Ivy 10'), bg=co4, anchor=NW)
# l_searchf.place(x=350, y=110)
# b_searchf = Button(frame_down, text="Search", height=1, width=10, bg= co2, fg=co0, font=('Ivy 8 bold'), command=to_searchf)
# b_searchf.place(x=500, y=140)
# e_searchf = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
# e_searchf.place(x=350, y=140)

b_view = Button(frame_down, text="View", height=1, width=10, bg= co3, fg=co0, font=('Ivy 8 bold'), command = show)
b_view.place(x=310, y=180)

b_add = Button(frame_down, text="Add", height=1, width=10, bg= co3, fg=co0, font=('Ivy 8 bold'), command=insert)
b_add.place(x=10, y=180)

b_update = Button(frame_down, text="Update", height=1, width=10, bg= co3, fg=co0, font=('Ivy 8 bold'), command=to_update)
b_update.place(x=110, y=180)

b_delete = Button(frame_down, text="Delete", height=1, width=10, bg= co3, fg=co0, font=('Ivy 8 bold'), command=to_remove)
b_delete.place(x=210, y=180)




window.mainloop()