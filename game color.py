from tkinter import*
import time

window=Tk()
window.geometry('400x400+200+200')
window.title("Color Game")
def click1():
    window.configure(bg="red")
   # time.sleep(0.5)
   # window.configure(bg="white")

def click2():
    window.configure(bg="blue")
   # time.sleep(2)
    #window.configure(bg="white")

def click3():
    window.configure(bg="green")
    #time.sleep(2)
   # window.configure(bg="white")
def click4():
    window.configure(bg="orange")
    #time.sleep(2)
   # window.configure(bg="white")
def click5():
    window.configure(bg="black")
    #time.sleep(2)
   # window.configure(bg="white")
def click6():
    window.configure(bg="yellow")
    #time.sleep(2)
   # window.configure(bg="white")
    
bt1=Button(window,text="red",command=click1).pack()
bt2=Button(window,text="blue",command=click2).pack()
bt3=Button(window,text="green",command=click3).pack()
bt4=Button(window,text="orange",command=click4).pack()
bt5=Button(window,text="black",command=click5).pack()
bt5=Button(window,text="yellow",command=click6).pack()





window.mainloop()
