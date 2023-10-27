from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from BankerMain import *
from datetime import *
class ShowBalance(Frame):
    def __init__(self,master):
        super().__init__(master)

        l1=Label(self,text="Account No",fg='red',bg='light blue',justify='center',font=('times',16))
        self.t1=Entry(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.b1=Button(self,text="Show",fg='red',bg='light blue',justify='center',font=('times',16),bd=6,command=self.getBalance)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        self.b1.grid(columnspan=2)
        self.pack()

    def getBalance(self):
        con=connect(db='hdfc',user='root',password='arrdsf147122',host='localhost')
        cur=con.cursor()
        acno=int(self.t1.get())
        cur.execute("select balance from customer where acno=%d"%(acno))
        data=cur.fetchall()
        if(len(data)>=1):
            msg.showinfo('Balance','Account Balance are '+str(data[0][0]))
        else:
            msg.showerror('Error','Account not opened')