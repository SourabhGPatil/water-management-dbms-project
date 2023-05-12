import sqlite3
import dates as dates
from datetime import datetime as dt
import datetime as datetime
from tkinter import *
#BACKEND

def officerData():
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE IF NOT EXISTS officer (id INTEGER PRIMARY KEY, Name text, sector_no text, FOREIGN KEY('sector_no') REFERENCES 'Locality'('sector_no') ON UPDATE CASCADE ON DELETE CASCADE)")
    con.commit()
    con.close()

def addOfficer(id, Name, sector_no):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO officer VALUES (?, ?, ?)", (id, Name, sector_no))
    con.commit()
    con.close()

def viewOfficer():
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM officer")
    rows = cur.fetchall()
    con.close()
    return rows

def delOfficer(id):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("DELETE FROM officer WHERE id=?",(id,))
    con.commit()
    con.close()

def officerView(officer_id):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Customer WHERE officer.id = Customer.officer_id AND Customer.officer_id = ? ", (officer_id,))
    rows = cur.fetchall()
    con.close()
    return rows

def reservoirData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE IF NOT EXISTS Reservoir (id INTEGER PRIMARY KEY, Name text, Water_level text)")
    con.commit()
    con.close()

def addReservoir(id, Name, Water_level):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO Reservoir VALUES (?, ?, ?)", (id, Name, Water_level))
    con.commit()
    con.close()

def delReservoir(id):
    con = sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("DELETE FROM Reservoir WHERE id=?",(id,))
    con.commit()
    con.close()

def viewReservoir():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM Reservoir")
    rows = cur.fetchall()
    con.close()
    return rows

def billData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE IF NOT EXISTS Bills ('id' INTEGER PRIMARY KEY,  'customer_id' text, 'Payments_Due' text, 'due_Date' text, FOREIGN KEY('customer_id') REFERENCES 'Customer'('id') ON UPDATE CASCADE ON DELETE CASCADE)")
    con.commit()
    con.close()

def addBill(id, customer_id, Payments_Due, due_Date):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO Bills VALUES (?, ?, ?, ?)", (id, customer_id, Payments_Due, due_Date))
    con.commit()
    con.close()

def delBill(id):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("DELETE FROM Bills WHERE id=?",(id,))
    con.commit()
    con.close()

def viewBill():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM Bills")
    rows = cur.fetchall()
    con.close()
    return rows

def localityData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("CREATE TABLE IF NOT EXISTS Locality ('sector_no' INTEGER PRIMARY KEY, 'Area_Name' text, 'Water_Supply_Date' text, 'officer_id' text, 'reservoir_id' text, FOREIGN KEY('reservoir_id') REFERENCES 'Reservoir'('id') ON UPDATE CASCADE ON DELETE CASCADE)")
    con.commit()
    con.close()

def updateDateEveryday():
    seclist = []
    nextdate = 4
    d = 0
    today = (datetime.date.today())
    timedelta = (datetime.timedelta(days = nextdate))
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("SELECT Water_Supply_Date FROM Locality")
    dAteS = cur.fetchall()
    for every in dAteS:
        EveryDate = every[0]
        string_date = changeToDate(EveryDate)
        seclist.append(string_date)
    appended_Date = today + timedelta
    for all in seclist:
        if all == datetime.date.today():
            seclist[d] = appended_Date
        d=d+1
    for all in seclist:
        dst = changeToString(all)
        cur.execute("UPDATE Locality SET Water_Supply_Date = ? WHERE TRUE",(dst,))
    con.commit()
    cur.close()

def changeToDate(strng):
    return dt.strptime(strng, '%d %B %Y').date()

def changeToString(date):
    return date.strftime('%d %B %Y')

def addLocality(sector_no, Area_Name, Water_Supply_Date, officer_id, reservoir_id):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO Locality VALUES (?, ?, ?, ?, ?)", (sector_no, Area_Name, Water_Supply_Date, officer_id, reservoir_id))
    con.commit()
    con.close()

def delLocality(sector_no):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("DELETE FROM Locality WHERE sector_no=?",(sector_no,))
    con.commit()
    con.close()

def viewLocality():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM Locality")
    rows = cur.fetchall()
    con.close()
    return rows

def customerData():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Customer (id INTEGER PRIMARY KEY, Name text, Address text, sector_no text, officer_id text, reservoir_id text, no_of_connection text, FOREIGN KEY("sector_no") REFERENCES "Locality"("sector_no") ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY("officer_id") REFERENCES "Officer"("id") ON UPDATE CASCADE ON DELETE CASCADE, FOREIGN KEY("reservoir_id") REFERENCES "Reservoir"("id") ON UPDATE CASCADE ON DELETE CASCADE)''')
    con.commit()
    cur.close()

def addCustomer(id, Name, Address, sector_no, officer_id, reservoir_id, no_of_connection):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?)", (id, Name, Address, sector_no, officer_id, reservoir_id, no_of_connection))
    con.commit()
    cur.close()

def delCustomer(id):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("DELETE FROM Customer WHERE id = ?",(id,))
    con.commit()
    cur.close()

def viewCustomer():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM Customer")
    rows = cur.fetchall()
    con.close()
    return rows

def viewCustomerFromOfficerID(officer_id):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("SELECT * FROM Customer WHERE officer_id = ?",(officer_id,))
    rows = cur.fetchall()
    con.close()
    return rows

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~UPDATES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def updateOfficer():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE Officer SET id = ? , Name = ? , sector_no = ? ", (id, Name, sector_no))
    con.commit()
    cur.close()

def updateReservoir():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE Reservoir SET id = ? , Name = ? , Water_level = ? ", (id, Name, Water_level))
    con.commit()
    cur.close()

def updateBill():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE Bills SET id = ? , Payments_Due = ? , due_Date = ? , customer_id = ? ", (id, Payments_Due, due_Date, customer_id))
    con.commit()
    cur.close()

def updateLocality():
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE Locality SET sector_no = ? , Area_Name = ? , Water_Supply_Date = ? , officer_id = ? , reservoir_id = ? ", (sector_no, Area_Name, Water_Supply_Date, officer_id, reservoir_id))
    con.commit()
    cur.close()

def updateCustomer(id):
    con = sqlite3.connect('backend.db')
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE Customer SET id = ? , Name = ? , sector_no = ? , officer_id = ? , reservoir_id = ? , no_of_connection = ? WHERE id = ? ", (id, Name, Address, sector_no, officer_id, reservoir_id, no_of_connection, id))
    con.commit()
    cur.close()

def dataOfficerUpdate(id="", Name="", sector_no=""):
    con=sqlite3.connect("backend.db")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("UPDATE officer SET id=?, Name=?, sector_no=?", (id, Name, sector_no))
    con.commit()
    con.close()

officerData()
reservoirData()
billData()
localityData()
customerData()
updateDateEveryday()