from tinkle import*
from tinkle import messagebox
import random

def no():
messagebox.showinfo(' ', 'Thanks bro')
quit()

def motionMouse(event):
    btnYes.place(x=random.radint(0, 500), y=random.radint(0, 500))

root = Tk()
root.geometry('600*600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Es-tu gay ?' , font='Arial 20 bold' , bg='white').pack()
btnYes= Button(root, text='Non' , font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>' , motionMouse)
btnNo = Button(root, text='Yes' , font='Arial 20 bold' , command=no).place(x=350, y=100)

root.mainloop()