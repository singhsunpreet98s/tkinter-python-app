import sqlite3 as sql
from tkinter import *;
class Database:
	def __init__(self):
		global con
		try:
			con =  sql.connect("namess.db")
			with con:
				cur = con.cursor()
				cur.execute("CREATE TABLE IF NOT EXISTS names(sno INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
		except Exception:
			print("error while creating")
	def addName(seld,data):
		if len(data)>0:
			try:
				with con:
					cur = con.cursor()
					cur.execute("INSERT INTO names (name) values('"+str(data)+"')")
					print("succes")
			except Exception:
				print("eroor while adding")	
	def show(self):
		try:
			with con:
				cur = con.cursor()
				cur.execute("SELECT * FROM names")
				data = cur.fetchall()
				return data

		except Exception:
			print("error while show")
	def deleteEntry(self,data):
		try:
			with con:
				cur = con.cursor()
				cur.execute("DELETE FROM names where name ='"+data+"'")
				print(cur.fetchall())
				return True
		except Exception:
			return False
class Outfit:
	def __init__(self,param):
		global tk
		global usrname
		global db
		db = Database()
		usrname = StringVar()
		tk=param
		tk.geometry("300x500")
	def home(self):
		pro = Frame(tk)
		def pg1():
			frame=False
			pro.destroy()
			self.login()
		def pg2():
			pro.destroy()
			self.disp()
		def pg3():
			pro.destroy()
			self.delete()
		btn1 = Button(pro,text="add",width=10,height=2,bg="red",fg="white",command=pg1).grid(row=1,column=1)
		btn2 = Button(pro,text="show",width=10,height=2,bg="red",fg="white",command=pg2).grid(row=1,column=2)
		btn3 = Button(pro,text="delete",width=10,height=2,bg="red",fg="white",command=pg3).grid(row=2,column=1)
		pro.pack()
	def login(self):
		def er():
			db.addName(usrname.get())
		def change():
			frm.destroy()
			self.home()
		frm = Frame(tk)
		lbl = Label(frm,text="Enter name here").grid(row=1)
		inp = Entry(frm,textvariable=usrname).grid(row=2)
		btn = Button(frm,text="submit",command=er).grid(row=3)
		btn = Button(frm,text="Home",command=change).grid(row=4)
		frm.pack()
	def disp(self):
		def change():
			lis.destroy()
			self.home()
		
		data = db.show()
		lis = Frame(tk)
		for i in range(0,len(data)):
				li = Label(lis,text=str(i+1)).grid(row=i+1,column=0)
				bi = Button(lis,text=str(data[i][1]),bd=0,cursor="dot").grid(row=i+1,column=1)
		btn = Button(lis,text="Home",command=change).grid(row=0)
		lis.pack()
	def delete(self):
		ery = StringVar()
		frm = Frame(tk)
		def fun():
			ret = db.deleteEntry(ery.get())
			if ret == True:
				frm.destroy()
				self.home()
			else:
				print('fail')
		inp = Entry(frm,textvariable=ery).grid(row=1)
		btn = Button(frm,text="delete",bg="red",fg="white",command=fun).grid(row=2)
		frm.pack()
def main():
	tk = Tk()
	o = Outfit(tk)
	o.home()
	tk.mainloop()

	
	
if(__name__ ==  "__main__"):
	
	main()
