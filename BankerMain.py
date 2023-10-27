from BankDeposit import *
from BankOpen import *
from tkinter import *
from BankWithdraw import *
from BankBalance import *
class MainMenu(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.menubar=Menu(self)
        
        
        self.file=Menu(self.menubar,tearoff=0)
        self.edit=Menu(self.menubar,tearoff=0)

        self.file.add_command(label='Open Account',command=self.accountopen)
        self.file.add_command(label='Close Account')
        self.file.add_separator()
        self.file.add_command(label='Exit',command=self.exitprg)

        self.edit.add_command(label='Deposit Amount',command=self.depositac)
        self.edit.add_command(label='Withdraw Account',command=self.withdrawac)
        self.edit.add_separator()
        self.edit.add_command(label='Show Balance',command=self.mybalance)

        self.menubar.add_cascade(label='File',underline=0,menu=self.file)
        self.menubar.add_cascade(label='Edit',underline=0,menu=self.edit)

    def exitprg(self):
        quit()  
    def accountopen(self):
        room=Tk()
        ob=MyAccount(room)
        room.title('Open Account')
        room.geometry('450x450')
        room.mainloop()      
    def depositac(self):
        room=Tk()
        ob=MyDeposit(room)
        room.title('Deposit Form')
        room.geometry('450x200')
        room.mainloop()
    def withdrawac(self):
        room=Tk()
        ob=MyWithdraw(room)
        room.title('Withdraw Form')
        room.geometry('450x450')
        room.mainloop()
    def mybalance(self):
        room=Tk()
        ob=ShowBalance(room)
        room.title('Balance Form')
        room.geometry('450x200')
        room.mainloop()
