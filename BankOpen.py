from tkinter import *
from datetime import *
from tkinter import messagebox as msg
from pymysql import *
class MyAccount(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.l1=Label(self,text="User Name",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l2=Label(self,text="Password",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l3=Label(self,text="First Name",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l4=Label(self,text="Last Name",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l5=Label(self,text="Account No",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l6=Label(self,text="Opening Account",fg='red',bg='light blue',justify='center',font=('times',16))
        self.l7=Label(self,text="User Type",fg='red',bg='light blue',justify='center',font=('times',16))
        self.t1=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t2=Label(self,fg='red',show='*',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t3=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t4=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t5=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t6=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.t7=Label(self,fg='red',bg='light blue',justify='center',font=('times',16),bd=6)
        self.b1=Button(self,text="Open Account",fg='red',bg='light blue',justify='center',font=('times',16),bd=6,command=self.savedata)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)
        self.rowconfigure(index=7,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)

        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        
        self.l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)
        
        self.l4.grid(row=3,column=0)
        self.t4.grid(row=3,column=1)
        
        self.l5.grid(row=4,column=0)
        self.t5.grid(row=4,column=1)
        
        self.l6.grid(row=5,column=0)
        self.t6.grid(row=5,column=1)
        
        self.l7.grid(row=6,column=0)
        self.t7.grid(row=6,column=1)

        self.b1.grid(columnspan=2)
        self.pack()

    def savedata(self):
        con=connect(db='hdfc',user='root',password='arrdsf147122',host='localhost')
        cur=con.cursor()
        dt=datetime.now()
        ndate=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
        uname=self.t1.get()
        passwd=self.t2.get()
        fname=self.t3.get()
        lname=self.t4.get()
        acno=int(self.t5.get())
        amt=float(self.t6.get())
        utype=self.t7.get()

        log=cur.execute("insert into login values('%s','%s','%s')"%(uname,passwd,utype))
        if(log==1):
            cust=cur.execute("insert into customer values('%s','%s','%s','%s',%f,%d)"%(uname,fname,lname,ndate,amt,acno))
            if(cust==1):
                t=cur.execute("insert into trans values(%d,'%s',%f,'%s')"%(acno,ndate,amt,'D'))
                if(t==1):
                    con.commit()
                    msg.showinfo('Confrimation','Account Opened')
                    self.t1.delete(0,'end')
                    self.t2.delete(0,'end')
                    self.t3.delete(0,'end')
                    self.t4.delete(0,'end')
                    self.t5.delete(0,'end')
                    self.t6.delete(0,'end')
                    self.t7.delete(0,'end')
                else:
                    msg.showerror('Error Box','Something not correct')
            else:
                msg.showerror('Error Box','Something not correct')
        else:
            msg.showerror('Error Box','Something not correct')
            con.close()        



