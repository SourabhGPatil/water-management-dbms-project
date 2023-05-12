from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import pymysql
import tempfile, os
import backend

import sqlite3
my_conn = sqlite3.connect('backend.db')



def main():
    root = Tk()
    app = Check(root)

####~~~~~~~~~~Home Window~~~~~~~~~~####
    
class Check:
    def __init__(self,master):
        self.master = master
        self.master.title("Home Page")
        self.master.geometry('1920x1080+0+0')
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master, bg = 'powder blue')
        self.frame.pack()

        ###~~~Home Window Title~~~###
        
        self.lblTitle = Label(self.frame, text = 'Home Page', font=('arial',50,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

        ###~~~Buttons~~~###
        self.LoginFrame = LabelFrame(self.frame, width=1000, height=600, font=('arial',20,'bold'), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame.grid(row=2, column=0)

        self.btnCustomer = Button(self.LoginFrame, text = 'Customer', width = 17,font=('arial',20,'bold'),command = self.CustomerLogin)
        self.btnCustomer.grid(row=1,column=1,pady=20,padx=8)

        self.btnAdmin = Button(self.LoginFrame, text = 'Admin', width = 17,font=('arial',20,'bold'), command = self.AdminLogin)
        self.btnAdmin.grid(row=2,column=1,pady=20,padx=8)

        self.btnOfficer = Button(self.LoginFrame, text = 'Officer', width = 17,font=('arial',20,'bold'), command = self.OfficerLogin)
        self.btnOfficer.grid(row=3,column=1,pady=20,padx=8)

    ###~~~Admin Login Redirect~~~###
    def AdminLogin(self):
            self.newWindow = Toplevel(self.master)
            self.app = Window1(self.newWindow)
            
    ###~~~Customer Login Redirect~~~###
    def CustomerLogin(self):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)

    ###~~~Officer Login Redirect~~~###
    def OfficerLogin(self):
            self.newWindow = Toplevel(self.master)
            self.app = Window3(self.newWindow)
    
        





#~~~creates Window1 for Admin Login~~~###
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Admin Login System")
        self.master.geometry('1920x1080+0+0')
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master, bg = 'powder blue')
        self.frame.pack()

        ###~~~User Input~~~###
        self.Username = StringVar()
        self.Password = StringVar()
        
        ###~~~Window1 Title~~~###
        self.lblTitle = Label(self.frame, text = 'Admin Login Page', font=('arial',50,'bold'), bg='powder blue', fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

        ###~~~Window1 Frames~~~###

        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600, font=('arial',20,'bold'), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600, font=('arial',20,'bold'), relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)


        ###~~~Window1 Labels~~~###        
        self.lblUsername=Label(self.LoginFrame1, text = 'Username',font=('arial',20,'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1,padx=119)


        self.lblPassword=Label(self.LoginFrame1, text = 'Password',font=('arial',20,'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'),show='*',textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1,columnspan=2,pady=30) 


        ###~~~Window1 Buttons~~~###
        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17,font=('arial',20,'bold'), command = self.Login_System)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 17,font=('arial',20,'bold'), command = self.Reset)
        self.btnReset.grid(row=3,column=1,pady=20,padx=8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 17,font=('arial',20,'bold'), command = self.iExit)
        self.btnExit.grid(row=3,column=2,pady=20,padx=8)


        ###~~~Redirecting Buttons after succesful login~~~###
        self.Loginframe3 = Frame(self.frame,width=1000,height=200,bd=20,relief='ridge',bg='cadet blue')
        self.Loginframe3.grid(row=4,column=0,pady=2, padx = 20)
        
        self.btnCustomer = Button(self.Loginframe3, text = 'Customer',state = DISABLED, width = 12,font=('arial',20,'bold'), command = self.Customer)
        self.btnCustomer.grid(row = 0,column = 0)

        self.btnOfficer = Button(self.Loginframe3, text = 'Officer',state = DISABLED, width = 12, font=('arial',20,'bold'), command = self.Officer)
        self.btnOfficer.grid(row = 0,column = 1, pady = 0, padx = 20)


        self.btnBills = Button(self.Loginframe3, text = 'Bills',state = DISABLED, width = 12, font=('arial',20,'bold'), command = self.Bills)
        self.btnBills.grid(row = 0,column = 2, pady = 0, padx = 20)


        self.btnLocality = Button(self.Loginframe3, text = 'Locality',state = DISABLED, width = 12, font=('arial',20,'bold'), command = self.Locality)
        self.btnLocality.grid(row = 0,column = 3, pady = 0, padx = 20)

        self.btnReservoir = Button(self.Loginframe3, text = 'Reservoir',state = DISABLED, width = 12, font=('arial',20,'bold'), command = self.Reservoir)
        self.btnReservoir.grid(row = 0,column = 4, pady = 0, padx = 20)
        

    ###~~~Redirecting Functions~~~###
    def Customer(self):
        self.newWindow = Toplevel(self.master)
        self.app = Customer(self.newWindow)

    def Officer(self):
        self.newWindow = Toplevel(self.master)
        self.app = Officer(self.newWindow)

    def Bills(self):
        self.newWindow = Toplevel(self.master)
        self.app = Bills(self.newWindow)

    def Locality(self):
        self.newWindow = Toplevel(self.master)
        self.app = Locality(self.newWindow)

    def Reservoir(self):
        self.newWindow = Toplevel(self.master)
        self.app = Reservoir(self.newWindow)
        

    ###~~~Button Functions~~~###
    def Login_System(self):
        u=(self.Username.get())
        p=(self.Password.get())
        if(u==str('Kevin')and p==str('Owens')): #The Username is : "Kevin" and the Password is : "Owens"
            self.btnCustomer.config(state = NORMAL)
            self.btnOfficer.config(state = NORMAL)
            self.btnBills.config(state = NORMAL)
            self.btnLocality.config(state = NORMAL)
            self.btnReservoir.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Error","The entered details are wrong")
            self.btnUser.config(state = DISABLED)
            self.btnOfficer.config(state = DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.Username.set("")
        self.Password.set("")


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command=self.new_window
            return



###~~~CUSTOMER Class~~~###
class Customer:

    ###~~~CUSTOMER DB~~~###
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Customer DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        Address = StringVar()
        sector_no = StringVar()
        officer_id = StringVar()
        reservoir_id = StringVar()
        no_of_connection = StringVar()


        ###~~~CUSTOMER Functions~~~###
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.txtAddress.delete(0, END)
            self.cbosector_no.current(0)
            self.txtofficer_id.delete(0, END)
            self.txtreservoir_id.delete(0, END)
            self.txtno_of_connection.delete(0, END)
        
        def addData():
            if id.get() == "" or Name.get() == "" or Address.get() == "" or sector_no.get() == "" or officer_id.get() == "" or reservoir_id.get() == "" or no_of_connection.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addCustomer(
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    no_of_connection.get()
                )

                displayData()

                super(self.customerlist, self).delete()

                self.customerlist.insert(END,
                (
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    no_of_connection.get()
                ))
    

        def displayData():
            result = backend.viewCustomer()
            if len(result)!=0:
                self.customerlist.delete(*self.customerlist.get_children())
                for row in result:
                    self.customerlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delCustomer(sd[0])
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete", "Record successfully deleted")

        def update():
            if(len(id.get()) != 0):
                backend.delCustomer(sd[0])

            if(len(id.get()) != 0):
                backend.addCustomer(id.get(), Name.get(), Address.get(), sector_no.get(), officer_id.get(), reservoir_id.get(), no_of_connection.get())

            displayData()

        def customerREC(event):
            global sd
            iReset()
            viewInfo = self.customerlist.focus()
            learnerData = self.customerlist.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtName.insert(END,sd[1])
            self.txtAddress.insert(END,sd[2])
            sector_no.set(sd[3])
            self.txtofficer_id.insert(END,sd[4])
            self.txtreservoir_id.insert(END,sd[5])
            self.txtno_of_connection.insert(END,sd[6])
            


        ###~~~CUSTOMER Frames~~~###
        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)

        ###~~~CUSTOMER Title~~~###    
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Customer Database', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)




        ###~~~CUSTOMER Buttons~~~###
        self.btnAddNew = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)


        ###~~~CUSTOMER Widgets~~~###


        self.lblid = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Customer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Customer Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblAddress = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Address ', bd = 7, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=2,column=0,sticky =W,padx=5)
        self.txtAddress = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Address)
        self.txtAddress.grid(row=2, column=1)

        self.lblsector_no = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Sector No ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=3,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(WidgetFrame, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 3, column = 1)

        self.lblofficer_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Officer ID', bd = 7, anchor='w', justify=LEFT)
        self.lblofficer_id.grid(row=4,column=0,sticky =W,padx=5)
        self.txtofficer_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = officer_id)
        self.txtofficer_id.grid(row=4, column=1)

        self.lblreservoir_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Reservoir ID', bd = 7, anchor='w', justify=LEFT)
        self.lblreservoir_id.grid(row=5,column=0,sticky =W,padx=5)
        self.txtreservoir_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = reservoir_id)
        self.txtreservoir_id.grid(row=5, column=1)

        self.lblno_of_connection = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'No. of connections', bd = 7, anchor='w', justify=LEFT)
        self.lblno_of_connection.grid(row=6,column=0,sticky =W,padx=5)
        self.txtno_of_connection = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = no_of_connection)
        self.txtno_of_connection.grid(row=6, column=1)

        ###~~~CUSTOMER Treeview~~~###
        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.customerlist = ttk.Treeview(TreeViewFrame, height = 12, columns = ("id", "Name", "Address", "sector_no", "officer_id", "reservoir_id", "no_of_connection"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.customerlist.heading("id", text = "Customer ID")
        self.customerlist.heading("Name", text = "Customer Name")
        self.customerlist.heading("Address", text = "Customer Address")
        self.customerlist.heading("sector_no", text = "Sector No")
        self.customerlist.heading("officer_id", text = "Officer ID")
        self.customerlist.heading("reservoir_id", text = "Reservoir ID")
        self.customerlist.heading("no_of_connection", text = "No. of conns.")

        self.customerlist['show'] = 'headings'
        self.customerlist.column("id", width = 90)
        self.customerlist.column("Name", width =  130)
        self.customerlist.column("Address", width = 130)
        self.customerlist.column("sector_no", width = 90)
        self.customerlist.column("officer_id", width = 90)
        self.customerlist.column("reservoir_id", width = 90)
        self.customerlist.column("no_of_connection", width = 90)

        self.customerlist.pack(fill = BOTH, expand = 1)

        self.customerlist.bind("<ButtonRelease-1>", customerREC)
        displayData()





###~~~OFFICER Class~~~###
class Officer:
    
    ###~~~OFFICER DB~~~###
    def  __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Officer DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        sector_no = StringVar()
        
        ###~~~OFFICER Functions~~~###
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.cbosector_no.current(0)

        def addData():
            if id.get() == "" or Name.get() == "" or sector_no.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addOfficer(
                    id.get(),
                    Name.get(),
                    sector_no.get()
                )
                
                displayData()
                
                super(self.officerlist, self).delete()

                self.officerlist.insert(END,
                    (
                    id.get(),
                    Name.get(),
                    sector_no.get()
                    ))

        def displayData():
            result = backend.viewOfficer()
            if len(result)!=0:
                self.officerlist.delete(*self.officerlist.get_children())
                for row in result:
                    self.officerlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delOfficer(sd[0])
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete", "Record successfully deleted")

        def update():
            if(len(id.get()) != 0):
                backend.delOfficer(sd[0])

            if(len(id.get()) != 0):
                backend.addOfficer(id.get(), Name.get(), sector_no.get())

            displayData()


        def officerREC(event):
            global sd
            iReset()
            viewInfo = self.officerlist.focus()
            learnerData = self.officerlist.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtName.insert(END,sd[1])
            sector_no.set(sd[2])

        ###~~~OFFICER Frames~~~###

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)

        ###~~~OFFICER Title~~~###
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Officer DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ###~~~OFFICER Widgets~~~###

        self.lblid = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Officer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Officer Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblsector_no = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Sector No.', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=2,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(WidgetFrame, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 2, column = 1)

        ###~~~OFFICER Treeview~~~###
        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.officerlist = ttk.Treeview(TreeViewFrame, height = 12, columns = ("id", "Name", "sector_no"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.officerlist.heading("id", text = "Officer ID")
        self.officerlist.heading("Name", text = "Officer Name")
        self.officerlist.heading("sector_no", text = "Sector No")

        self.officerlist['show'] = 'headings'
        self.officerlist.column("id", width = 70)
        self.officerlist.column("Name", width =  150)
        self.officerlist.column("sector_no", width = 70)

        self.officerlist.pack(fill = BOTH, expand = 1)

        self.officerlist.bind("<ButtonRelease-1>", officerREC)
        displayData()
        
        
        ###~~~OFFICER Buttons~~~###
        self.btnAddNew = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)




###~~~BILLS Class~~~###
class Bills:
    


    ###~~~BILLS DB~~~###
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Billing DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        customer_id = StringVar()
        id = StringVar()
        Payments_Due = StringVar()
        due_Date = StringVar()
        
        ###~~~BILLS Functions~~~###
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtcustomer_id.delete(0, END)
            self.txtPayments_Due.delete(0, END)
            self.txtdue_Date.delete(0, END)

        def addData():
            if id.get() == "" or customer_id.get() == "" or Payments_Due.get() == "" or due_Date.get == "":
                tkinter.messagebox.askyesno("Error","Please enter the correct Data")
            else:
                backend.addBill(
                    id.get(),
                    customer_id.get(),
                    Payments_Due.get(),
                    due_Date.get(),
                )

                displayData()

                super(self.billinglist, self).delete()

                self.billinglist.insert(END,
                (
                    id.get(),
                    customer_id.get(),
                    Payments_Due.get(),
                    due_Date.get(),
                ))

        def displayData():
            result = backend.viewBill()
            if len(result)!=0:
                self.billinglist.delete(*self.billinglist.get_children())
                for row in result:
                    self.billinglist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delBill(sd[0])
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete", "Record successfully deleted")

        def update():
            if(len(id.get()) != 0):
                backend.delBill(sd[0])

            if(len(id.get()) != 0):
                backend.addBill(id.get(), customer_id.get(), Payments_Due.get(), due_Date.get())

            displayData()
            

        def billingREC(event):
            global sd
            iReset()
            viewInfo = self.billinglist.focus()
            learnerData = self.billinglist.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtcustomer_id.insert(END,sd[1])
            self.txtPayments_Due.insert(END,sd[2])
            self.txtdue_Date.insert(END,sd[3])

        ###~~~BILLS Frames~~~###
        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)

        ###~~~BILLS Title~~~###
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Billing DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ###~~~BILLS Buttons~~~###
        self.btnAddNew = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)

        ###~~~BILLS Labels~~~###
        self.lblid = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Bill ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblcustomer_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Customer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblcustomer_id.grid(row=1,column=0,sticky =W,padx=5)
        self.txtcustomer_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = customer_id)
        self.txtcustomer_id.grid(row=1, column=1)

        self.lblPayments_Due = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Payment Due ', bd = 7, anchor='w', justify=LEFT)
        self.lblPayments_Due.grid(row=2,column=0,sticky =W,padx=5)
        self.txtPayments_Due = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Payments_Due)
        self.txtPayments_Due.grid(row=2, column=1)

        self.lbldue_Date = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Due Date', bd = 7, anchor='w', justify=LEFT)
        self.lbldue_Date.grid(row=3,column=0,sticky =W,padx=5)
        self.txtdue_Date = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = due_Date)
        self.txtdue_Date.grid(row=3, column=1)

        ###~~~BILLS TreeView~~~###
        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.billinglist = ttk.Treeview(TreeViewFrame, height = 12, columns = ("id", "customer_id", "Payments_Due", "due_Date"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.billinglist.heading("id", text = "Bill ID")
        self.billinglist.heading("customer_id", text = "Customer ID")
        self.billinglist.heading("Payments_Due", text = "Payemt Due")
        self.billinglist.heading("due_Date", text = "Due Date")

        self.billinglist['show'] = 'headings'
        self.billinglist.column("id", width = 90)
        self.billinglist.column("customer_id", width =  90)
        self.billinglist.column("Payments_Due", width = 90)
        self.billinglist.column("due_Date", width = 150)

        self.billinglist.pack(fill = BOTH, expand = 1)

        self.billinglist.bind("<ButtonRelease-1>", billingREC)
        displayData()



###~~~LOCALITY Class~~~###
class Locality:
    
    ###~~~LOCALITY DB~~~###
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Locality DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        sector_no = StringVar()
        Area_Name = StringVar()
        Water_Supply_Date = StringVar()
        officer_id = StringVar()
        reservoir_id = StringVar()
        
        ###~~~LOCALITY Functions~~~###
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.cbosector_no.current(0)
            self.txtWater_Supply_Date.delete(0, END)
            self.txtofficer_id.delete(0, END)
            self.txtArea_Name.delete(0, END)
            self.txtreservoir_id.delete(0, END)

        def addData():
            if sector_no.get() == "" or Area_Name.get() == "" or Water_Supply_Date.get() == "" or officer_id.get() == "" or reservoir_id.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addLocality(
                    sector_no.get(),
                    Area_Name.get(),
                    Water_Supply_Date.get(),
                    officer_id.get(),
                    reservoir_id.get()
                )

                displayData()

                super(self.localitylist, self).delete()

                self.localitylist.insert(END,
                (
                    sector_no.get(),
                    Area_Name.get(),
                    Water_Supply_Date.get(),
                    officer_id.get(),
                    reservoir_id.get()
                ))


        def displayData():
            result = backend.viewLocality()
            if len(result)!=0:
                self.localitylist.delete(*self.localitylist.get_children())
                for row in result:
                    self.localitylist.insert('', END, values = row)

        def deleteData():
            if(len(sector_no.get())!= 0):
                backend.delLocality(sd[0])
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete", "Record successfully deleted")

        def update():
            if(len(sector_no.get()) != 0):
                backend.delLocality(sd[0])

            if(len(sector_no.get()) != 0):
                backend.addLocality(sector_no.get(), Area_Name.get(), Water_Supply_Date.get(), officer_id.get(), reservoir_id.get())

            displayData()

        def localityREC(event):
            global sd
            iReset()
            viewInfo = self.localitylist.focus()
            learnerData = self.localitylist.item(viewInfo)
            sd = learnerData['values']

            sector_no.set(sd[0])
            self.txtArea_Name.insert(END,sd[1])
            self.txtWater_Supply_Date.insert(END,sd[2])
            self.txtofficer_id.insert(END,sd[3])
            self.txtreservoir_id.insert(END,sd[4])



        ###~~~LOCALITY Frames~~~###

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)

        ###~~~LOCALITY Class~~~###
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Locality DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)




        ###~~~LOCALITY Button~~~###
        self.btnAddNew = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)



        ###~~~LOCALITY Buttons~~~###
        self.lblsector_no = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Sector No. ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=0,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(WidgetFrame, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 0, column = 1)


        self.lblArea_Name = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Area Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblArea_Name.grid(row=1,column=0,sticky =W,padx=5)
        self.txtArea_Name = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Area_Name)
        self.txtArea_Name.grid(row=1, column=1)

        self.lblWater_Supply_Date = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Water Supply Date ', bd = 7, anchor='w', justify=LEFT)
        self.lblWater_Supply_Date.grid(row=2,column=0,sticky =W,padx=5)
        self.txtWater_Supply_Date = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Water_Supply_Date)
        self.txtWater_Supply_Date.grid(row=2, column=1)

        self.lblofficer_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Officer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblofficer_id.grid(row=3,column=0,sticky =W,padx=5)
        self.txtofficer_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = officer_id)
        self.txtofficer_id.grid(row=3, column=1)


        self.lblreservoir_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Reservoir ID', bd = 7, anchor='w', justify=LEFT)
        self.lblreservoir_id.grid(row=4,column=0,sticky =W,padx=5)
        self.txtreservoir_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = reservoir_id)
        self.txtreservoir_id.grid(row=4, column=1)

        ###~~~LOCALITY TreeView~~~###
        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.localitylist = ttk.Treeview(TreeViewFrame, height = 12, columns = ("sector_no", "Area_Name", "Water_Supply_Date", "officer_id", "reservoir_id"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.localitylist.heading("sector_no", text = "Sector No.")
        self.localitylist.heading("Area_Name", text = "Area Name")
        self.localitylist.heading("Water_Supply_Date", text = "Water Supply Date")
        self.localitylist.heading("officer_id", text = "Officer ID")
        self.localitylist.heading("reservoir_id", text = "Reservoir ID")

        self.localitylist['show'] = 'headings'
        self.localitylist.column("sector_no", width = 90)
        self.localitylist.column("Area_Name", width =  150)
        self.localitylist.column("Water_Supply_Date", width = 150)
        self.localitylist.column("officer_id", width = 90)
        self.localitylist.column("reservoir_id", width = 90)

        self.localitylist.pack(fill = BOTH, expand = 1)

        self.localitylist.bind("<ButtonRelease-1>", localityREC)
        displayData()



###~~~RESERVOIR Class~~~###
class Reservoir:
    ###~~~RESERVOIR DB~~~###
    def  __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Reservoir DB")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        Water_level = StringVar()
        
        ###~~~RESERVOIR Functions~~~###
        def iExit():
            iExit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.txtWater_level.delete(0, END)

        def addData():
            if id.get() == "" or Name.get() == "" or Water_level.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addReservoir(
                    id.get(),
                    Name.get(),
                    Water_level.get()
                )

                displayData()

                super(self.reservoirlist, self).delete()

                self.reservoirlist.insert(END,
                    (
                    id.get(),
                    Name.get(),
                    Water_level.get()
                    ))

        def displayData():
            result = backend.viewReservoir()
            if len(result)!=0:
                self.reservoirlist.delete(*self.reservoirlist.get_children())
                for row in result:
                    self.reservoirlist.insert('', END, values = row)

        def deleteData():
            if(len(id.get())!= 0):
                backend.delReservoir(sd[0])
                iReset()
                displayData()
                tkinter.messagebox.showinfo("Delete","Record successfully deleted")

        def update():
            if(len(id.get()) != 0):
                backend.delReservoir(sd[0])

            if(len(id.get()) != 0):
                backend.addReservoir(id.get(), Name.get(), Water_level.get())

            displayData()
        

        def ReservoirREC(event):
            global sd
            iReset()
            viewInfo = self.reservoirlist.focus()
            learnerData = self.reservoirlist.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtName.insert(END,sd[1])
            self.txtWater_level.insert(END,sd[2])

        ###~~~RESERVOIR Frames~~~###

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)

        ###~~~RESERVOIR Title~~~###
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Reservoir DB', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ###~~~RESERVOIR Labels~~~###

        self.lblid = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Reservoir ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Reservoir Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblWater_level = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Water Level ', bd = 7, anchor='w', justify=LEFT)
        self.lblWater_level.grid(row=2,column=0,sticky =W,padx=5)
        self.txtWater_level = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Water_level)
        self.txtWater_level.grid(row=2, column=1)

        ###~~~RESERVOIR TreeView~~~###
        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.reservoirlist = ttk.Treeview(TreeViewFrame, height = 12, columns = ("id", "Name", "Water_level"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.reservoirlist.heading("id", text = "Reservoir ID")
        self.reservoirlist.heading("Name", text = "Reservoir Name")
        self.reservoirlist.heading("Water_level", text = "Water level")

        self.reservoirlist['show'] = 'headings'
        self.reservoirlist.column("id", width = 90)
        self.reservoirlist.column("Name", width =  150)
        self.reservoirlist.column("Water_level", width = 90)

        self.reservoirlist.pack(fill = BOTH, expand = 1)

        self.reservoirlist.bind("<ButtonRelease-1>", ReservoirREC)
        displayData()
        
        ###~~~RESERVOIR Buttons~~~###
        self.btnAddNew = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Insert New" ,padx = 24, width = 8, height  = 1, command = addData).grid(row = 0, column = 0, padx = 1)
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Display" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 1, padx = 1)
        self.btnDelete = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Delete" ,padx = 24, width = 8, height  = 1, command = deleteData).grid(row = 0, column = 2, padx = 1)
        self.btnUpdate = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Update" ,padx = 24, width = 8, height  = 1, command = update).grid(row = 0, column = 3, padx = 1)
        self.btnReset = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Reset" ,padx = 24, width = 8, height  = 1, command = iReset).grid(row = 0, column = 4, padx = 1)
        self.btnExit = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Exit" ,padx = 24, width = 8, height  = 1, command = iExit).grid(row = 0, column = 5, padx = 1)













###~~~creates Window2 for Customer Login~~~###
class Window2:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "USER")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        
        ###~~~Customer Login Frames~~~###
        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 2, column = 0, pady = 8)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)

        TopFrame1 = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame1.grid(row = 3, column = 0)





        ###~~~Customer Login Frames~~~###
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='User Login', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)

        ###~~~Customer Label~~~###
        self.l1 = Label(TopFrame, font = ('arial', 20, 'bold'), text='Enter User ID: ', width=15, height = 1)  
        self.l1.grid(row=1,column=1)

        self.t1 = Text(TopFrame, font = ('arial', 20, 'bold'),  height=1, width=10 ,bg='white') 
        self.t1.grid(row=1,column=2)


        ###~~~Customer Login User Data and Labels~~~###
        my_str1 = StringVar()
        my_str2 = StringVar()
        my_str3 = StringVar()
        my_str4 = StringVar()
        my_str5 = StringVar()
        my_str6 = StringVar()
        my_str7 = StringVar()
        my_str8 = StringVar()
        my_str9 = StringVar()


        self.demo_l2 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'ID', width=20,bd = 7, anchor='center')
        self.demo_l2.grid(row=3, column = 1, padx=10)
        self.l2 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str1, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l2.grid(row=3,column=2)
        
        self.demo_l3 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Name', width=20,bd = 7, anchor='center')
        self.demo_l3.grid(row=4, column = 1, padx=10)
        self.l3 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str2, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l3.grid(row=4,column=2)
        
        self.demo_l4 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Address', width=20,bd = 7, anchor='center')
        self.demo_l4.grid(row=5, column = 1, padx=10)
        self.l4 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str3, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l4.grid(row=5,column=2)
        
        self.demo_l5 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Sector No.', width=20,bd = 7, anchor='center')
        self.demo_l5.grid(row=6, column = 1, padx=10)
        self.l5 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str4, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l5.grid(row=6,column=2)
        
        self.demo_l6 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Officer ID', width=20,bd = 7, anchor='center')
        self.demo_l6.grid(row=7, column = 1, padx=10)
        self.l6 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str5, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l6.grid(row=7,column=2)
        
        self.demo_l7 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Reservoir ID', width=20,bd = 7, anchor='center')
        self.demo_l7.grid(row=8, column = 1, padx=10)
        self.l7 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str6, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE )  
        self.l7.grid(row=8,column=2)
        
        self.demo_l8 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'No. of Connections', width=20,bd = 7, anchor='center')
        self.demo_l8.grid(row=9, column = 1, padx=10)
        self.l8 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str7, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE)  
        self.l8.grid(row=9,column=2)

        self.demo_l9 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Water Supply Date', width=20,bd = 7, anchor='center')
        self.demo_l9.grid(row=10, column = 1, padx=10)
        self.l9 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str8, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE)  
        self.l9.grid(row=10,column=2)

        self.demo_l10 = Label(TopFrame1, font = ('arial', 20, 'bold'), text = 'Bill Due', width=20,bd = 7, anchor='center')
        self.demo_l10.grid(row=11, column = 1, padx=10)
        self.l10 = Label(TopFrame1, font = ('arial', 20, 'bold'), textvariable=my_str9, width=30, fg='purple', bd = 7, anchor='center',relief=RIDGE)  
        self.l10.grid(row=11,column=2)


        my_str1.set("")
        my_str2.set("")
        my_str3.set("")
        my_str4.set("")
        my_str5.set("")
        my_str6.set("")
        my_str7.set("")
        my_str8.set("")
        my_str9.set("")

        ###~~~Customer Login Function~~~###

        def my_details(id):
                try:    
                    q="SELECT * FROM Customer WHERE id= "+id
                    my_cursor=my_conn.execute(q)
                    data_row=my_cursor.fetchone()
                    my_str1.set(data_row[0])
                    my_str2.set(data_row[1])
                    my_str3.set(data_row[2])
                    my_str4.set(data_row[3])
                    my_str5.set(data_row[4])
                    my_str6.set(data_row[5])
                    my_str7.set(data_row[6])
                    
                    w="SELECT Locality.Water_Supply_Date FROM Locality, Customer WHERE Locality.sector_no = Customer.sector_no AND Customer.id = "+id
                    my_cursor1=my_conn.execute(w)
                    data_row1=my_cursor1.fetchone()
                    my_str8.set(data_row1)
                    
                    e="SELECT Bills.Payments_Due FROM Bills, Customer WHERE Bills.customer_id = Customer.id AND Customer.id= "+id
                    my_cursor2=my_conn.execute(e)
                    data_row2=my_cursor2.fetchone()
                    my_str9.set(data_row2)
                except sqlite3.Error as my_error:
                    print("error: ",my_error)

        ###~~~Customer Login Button~~~###
        self.btn = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Show Details" ,padx = 24, width = 8, height  = 1, command = lambda: my_details(self.t1.get('1.0',END))).grid(row = 0, column = 0, padx = 1)





###~~~Creates Window3 for Officer Login~~~###
class Window3:
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Officer Details")
        self.root.geometry("1920x1080+0+0")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        id = StringVar()
        Name = StringVar()
        Address = StringVar()
        sector_no = StringVar()
        officer_id = StringVar()
        reservoir_id = StringVar()
        no_of_connection = StringVar()


    ###~~~Officer Login Button~~~###       

        def addData():
            if id.get() == "" or Name.get() == "" or Address.get() == "" or sector_no.get() == "" or officer_id.get() == "" or reservoir_id.get() == "" or no_of_connection.get() == "":
                tkinter.messagebox.askyesno("Error", "Please enter the correct Data")
            else:
                backend.addCustomer(
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    no_of_connection.get()
                )

                displayData()

                super(self.OfficerCustomerList, self).delete()

                self.OfficerCustomerList.insert(END,
                (
                    id.get(),
                    Name.get(),
                    Address.get(),
                    sector_no.get(),
                    officer_id.get(),
                    reservoir_id.get(),
                    no_of_connection.get()
                ))

        
        def displayData():
            result = backend.viewCustomerFromOfficerID(officer_id.get())
            if len(result)!=0:
                self.OfficerCustomerList.delete(*self.OfficerCustomerList.get_children())
                for row in result:
                    self.OfficerCustomerList.insert('', END, values = row)

        def iReset():
            self.txtid.delete(0, END)
            self.txtName.delete(0, END)
            self.txtAddress.delete(0, END)
            self.cbosector_no.current(0)
            self.txtofficer_id.delete(0, END)
            self.txtreservoir_id.delete(0, END)
            self.txtno_of_connection.delete(0, END)

        

        def OfficerCustomerREC(event):
            global sd
            iReset()
            viewInfo = self.OfficerCustomerList.focus()
            learnerData = self.OfficerCustomerList.item(viewInfo)
            sd = learnerData['values']

            self.txtid.insert(END,sd[0])
            self.txtName.insert(END,sd[1])
            self.txtAddress.insert(END,sd[2])
            sector_no.set(sd[3])
            self.txtofficer_id.insert(END,sd[4])
            self.txtreservoir_id.insert(END,sd[5])
            self.txtno_of_connection.insert(END,sd[6])

        ###~~~Officer Frames~~~###        

        MainFrame = Frame(self.root, bd = 10, width = 1350, height = 700, relief = RIDGE, bg = "cadet blue")
        MainFrame.grid()

        ButtonFrame = Frame(MainFrame, bd = 5, width = 1340, height = 100, relief = RIDGE)
        ButtonFrame.grid(row = 3, column = 0, pady = 5)

        TitleFrame = Frame(MainFrame, bd = 7, width = 1340, height = 100, relief = RIDGE)
        TitleFrame.grid(row = 0, column = 0)

        TopFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        TopFrame.grid(row = 4, column = 0)

        LabelFrame = Frame(MainFrame, bd = 5, width = 1340, height = 500, relief = RIDGE)
        LabelFrame.grid(row = 2, column = 0, pady = 8)

        LeftFrame = Frame(TopFrame, bd = 5, width = 1340, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        LeftFrame.pack(side = LEFT)

        WidgetFrame = Frame(LeftFrame, bd = 5, width = 300, height = 180, padx = 2, pady = 4, relief = RIDGE)
        WidgetFrame.pack(side = TOP, padx = 0, pady = 4)

        RightFrame = Frame(TopFrame, bd = 5, width = 320, height = 400, padx = 2, bg = "cadet blue", relief = RIDGE)
        RightFrame.pack(side = RIGHT)

        TreeViewFrame = Frame(RightFrame, bd = 5, width = 310, height = 200, padx = 2, pady = 2, relief = RIDGE)
        TreeViewFrame.pack(side = TOP)




        ###~~~Officer Login Title~~~###
    
        self.lblTitle = Label(TitleFrame, font = ('arial', 56, 'bold'), text='Officer\'s Records', bd = 7)
        self.lblTitle.grid(row = 0, column = 0, padx =132)
        
        ###~~~Officer Login Button~~~###
        self.btnDisplay = Button(ButtonFrame, pady = 1, bd = 4, font = ('arial', 20, 'bold'), text = "Get Details" ,padx = 24, width = 8, height  = 1, command = displayData).grid(row = 0, column = 0, padx = 1)



        ###~~~Officer Login Label~~~###
        self.lblofficer_id = Label(LabelFrame, font = ('arial',20,'bold'), text = 'Enter Officer ID:', width=15, height = 1, pady = 1, bd = 4,)
        self.lblofficer_id.grid(row=1,column=1)
        
        self.txtofficer_id = Entry(LabelFrame, font = ('arial',20,'bold'), width=10 ,bg='white',bd=5, textvariable = officer_id)
        self.txtofficer_id.grid(row=1, column=2)
        
       
        ###~~~Officer Login Widgets~~~###
        self.lblid = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Customer ID ', bd = 7, anchor='w', justify=LEFT)
        self.lblid.grid(row=0,column=0,sticky =W,padx=5)
        self.txtid = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = id)
        self.txtid.grid(row=0, column=1)

        self.lblName = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Customer Name ', bd = 7, anchor='w', justify=LEFT)
        self.lblName.grid(row=1,column=0,sticky =W,padx=5)
        self.txtName = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Name)
        self.txtName.grid(row=1, column=1)

        self.lblAddress = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Address ', bd = 7, anchor='w', justify=LEFT)
        self.lblAddress.grid(row=2,column=0,sticky =W,padx=5)
        self.txtAddress = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = Address)
        self.txtAddress.grid(row=2, column=1)

        self.lblsector_no = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Sector No ', bd = 7, anchor='w', justify=LEFT)
        self.lblsector_no.grid(row=3,column=0,sticky =W,padx=5)
        self.cbosector_no = ttk.Combobox(WidgetFrame, width = 39, font = ('arial', 12, 'bold'), state = 'readonly', textvariable = sector_no)
        self.cbosector_no['values'] = ('','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13')
        self.cbosector_no.current(0)
        self.cbosector_no.grid(row = 3, column = 1)

        self.lblreservoir_id = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'Reservoir ID', bd = 7, anchor='w', justify=LEFT)
        self.lblreservoir_id.grid(row=4,column=0,sticky =W,padx=5)
        self.txtreservoir_id = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = reservoir_id)
        self.txtreservoir_id.grid(row=4, column=1)

        self.lblno_of_connection = Label(WidgetFrame, font = ('arial',12,'bold'), text = 'No. of connections', bd = 7, anchor='w', justify=LEFT)
        self.lblno_of_connection.grid(row=5,column=0,sticky =W,padx=5)
        self.txtno_of_connection = Entry(WidgetFrame, font = ('arial',12,'bold'), bd = 5, width = 40, justify = "left", textvariable = no_of_connection)
        self.txtno_of_connection.grid(row=5, column=1)

        ###~~~Officer Login TreeView~~~###

        scroll_x = Scrollbar(TreeViewFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(TreeViewFrame, orient = VERTICAL)

        self.OfficerCustomerList = ttk.Treeview(TreeViewFrame, height = 12, columns = ("id", "Name", "Address", "sector_no", "officer_id", "reservoir_id", "no_of_connection"), xscrollcommand = scroll_x.set,yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = BOTTOM, fill = Y)

        self.OfficerCustomerList.heading("id", text = "Customer ID")
        self.OfficerCustomerList.heading("Name", text = "Customer Name")
        self.OfficerCustomerList.heading("Address", text = "Customer Address")
        self.OfficerCustomerList.heading("sector_no", text = "Sector No")
        self.OfficerCustomerList.heading("officer_id", text = "Officer ID")
        self.OfficerCustomerList.heading("reservoir_id", text = "Reservoir ID")
        self.OfficerCustomerList.heading("no_of_connection", text = "No. of conns.")

        self.OfficerCustomerList['show'] = 'headings'
        self.OfficerCustomerList.column("id", width = 90)
        self.OfficerCustomerList.column("Name", width =  200)
        self.OfficerCustomerList.column("Address", width = 200)
        self.OfficerCustomerList.column("sector_no", width = 90)
        self.OfficerCustomerList.column("officer_id", width = 90)
        self.OfficerCustomerList.column("reservoir_id", width = 90)
        self.OfficerCustomerList.column("no_of_connection", width = 90)

        self.OfficerCustomerList.pack(fill = BOTH, expand = 1)

        self.OfficerCustomerList.bind("<ButtonRelease-1>", OfficerCustomerREC)
        displayData()






if __name__ == '__main__':
    main()