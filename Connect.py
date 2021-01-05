'''
Created on January 5, 2021

@author: rboruk
'''

import redis
try:
    from tkinter import * 
    from tkinter import messagebox
except ImportError:
    from Tkinter import *

class Conn:
    def __init__(self):

        #Creating a not resizable window
        self.rootConn = Tk()
        self.rootConn.title("Connect to Redis DB")
        self.rootConn.geometry("300x250+400+100")
        self.rootConn.resizable(False, False)
        self.rootConn.call('wm', 'iconphoto', self.rootConn._w, "-default", PhotoImage(file='Pics\\logo.png'))

        self.rootConn.grid_rowconfigure(0, weight=1)
        self.rootConn.grid_columnconfigure(0, weight=1)

        #frame to provide information
        self.frameHelpInfo = Frame(self.rootConn, borderwidth=5, relief="ridge", width=300, height=250)
        self.frameHelpInfo.grid(row=0, column=0, sticky=(N, S, E, W))
        
        self.title= Label(self.frameHelpInfo,text = "")
        self.title.grid(row=0, column=0, columnspan=2, sticky=(N, E, S, W)) 
        
        self.title= Label(self.frameHelpInfo,text = "Connect to Redis DB")
        self.title.grid(row=1, column=0, columnspan=2, sticky=(N, E, S, W))
        
        self.title= Label(self.frameHelpInfo,text = "")
        self.title.grid(row=2, column=0, columnspan=2, sticky=(N, E, S, W))

        self.hostname_label = Label(self.frameHelpInfo,text ="Host name: ")
        self.hostname_label.grid(row=3, column=0, sticky=(E))

        self.hostname_entry = Entry(self.frameHelpInfo, width=33)
        self.hostname_entry.grid(row=3, column=1, sticky=(N, E, S, W))
        
        self.title= Label(self.frameHelpInfo,text = "")
        self.title.grid(row=4, column=0, columnspan=2, sticky=(N, E, S, W))

        self.hostport_label = Label(self.frameHelpInfo,text ="Host port: ")
        self.hostport_label.grid(row=5, column=0, sticky=(E))

        self.hostport_entry = Entry(self.frameHelpInfo)
        self.hostport_entry.grid(row=5, column=1, sticky=(N, E, S, W))
        
        self.title= Label(self.frameHelpInfo,text = "")
        self.title.grid(row=6, column=0, columnspan=2, sticky=(N, E, S, W))

        self.password_label = Label(self.frameHelpInfo,text ="Password: ")
        self.password_label.grid(row=7, column=0, sticky=(E))

        self.password_entry= Entry(self.frameHelpInfo)
        self.password_entry.grid(row=7, column=1, sticky=(N, E, S, W))

        #button to close the connection window
        self.closeHelpButton = Button(self.rootConn, borderwidth=5, text = "Connect", command=self.endHelp)
        self.closeHelpButton.grid(row=1, column=0, sticky=(N, S, E, W))
        
        self.rootConn.mainloop()

    #close Help window
    def endHelp(self):
        #establishing connection with redis
        if not self.hostname_entry.get(): redis_port = ""
        redis_host = self.hostname_entry.get()
        if not self.hostport_entry.get(): redis_port = 0
        else: redis_port = (int(self.hostport_entry.get()))
        if not self.password_entry.get(): redis_password = ""
        else: redis_password = self.password_entry.get()

        client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
        try:
            client.ping()
            self.rootConn.destroy()
        except (redis.exceptions.ConnectionError, 
            redis.exceptions.BusyLoadingError):
            messagebox.showerror("Connection Error", "Connection was not established. Please, review parameters and validate that Redis Server is up and running!")

        
        
