import os
from tkinter import *

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def shutdown():
    os.system("shutdown /s /t /1")
def logout():
    os.system("shutdown -l")


sd = Tk()

# all the work has to be done bw Tk() and mainloop()

sd.title("ShutDown App")
sd.geometry("500x500")
sd.config(bg="Brown")

# This is normal restart 
restart_button = Button(sd,text="Restart", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command = restart)
restart_button.place(x=150,y=60,height=50,width=200)

# this is timed restart
restart_button_time = Button(sd,text="Restart Time", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command = restart_time)
restart_button_time.place(x=150,y=170,height=50,width=200) 

# x is distance of button from left
# y is distance from button from top
# width and height is understood

# this is for shutdown
shutdown_button = Button(sd,text="ShutDown", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command = shutdown)
shutdown_button.place(x=150,y=280,height=50,width=200)

# this is for Log out
sleep_button = Button(sd,text="LOG OUT", font=("Times New Roman", 30, "bold"), relief=RAISED, cursor="plus", command = logout)
sleep_button.place(x=150,y=390,height=50,width=200)



sd.mainloop()