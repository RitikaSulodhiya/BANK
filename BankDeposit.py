from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from BankerMain import *
from datetime import *
class MyDeposit(Frame):
    def _init_(self,master):
        super().__init__(master)

        l1=Label(self,text="Account No",fg='red',bg='light blue',justify='center',font=('times',16))
        l2=Label(self,text="Amount Deposit",fg='red',bg='light blue',justify='center',font=('times',16))
        self.t1=Entry(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t2=Entry(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.b1=Button(self,text="Deposit",fg='red',bg='light blue',justify='center',font=('times',16),bd=6,command=self.deposit)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        self.b1.grid(columnspan=2)
        self.pack()

    def deposit(self):
        con=connect(db='hdfc',user='root',password='arrdsf147122',host='localhost')
        cur=con.cursor()
        acno=int(self.t1.get())
        amt=float(self.t2.get())
        dt=datetime.now()
        ndate=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
        i=cur.execute("update customer set balance=balance+%f where acno=%d"%(amt,acno))
        if(i==1):
            j=cur.execute("insert into trans values(%d,'%s',%f,'%s')"%(acno,ndate,amt,'D'))
            if(j==1):
                con.commit()
                msg.showinfo('Confirmation','Amount Deposited')
                self.t1.delete(0,'end')
                self.t2.delete(0,'end')
        else:
            msg.showerror('Error','Account Not Found')
        con.close()