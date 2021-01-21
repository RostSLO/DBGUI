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
        
        self.redis_host = ""
        self.redis_port = 0
        self.redis_password = ""
        
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

        self.hostnameLabel = Label(self.frameHelpInfo,text ="Host name: ")
        self.hostnameLabel.grid(row=3, column=0, sticky=(E))

        self.hostnameEntry = Entry(self.frameHelpInfo, width=33)
        self.hostnameEntry.grid(row=3, column=1, sticky=(N, E, S, W))
        #for testing purposes
        #self.hostnameEntry.insert(0, "localhost")
        
        self.title = Label(self.frameHelpInfo,text = "")
        self.title.grid(row=4, column=0, columnspan=2, sticky=(N, E, S, W))

        self.hostportLabel = Label(self.frameHelpInfo,text ="Host port: ")
        self.hostportLabel.grid(row=5, column=0, sticky=(E))

        self.hostportEntry = Entry(self.frameHelpInfo)
        self.hostportEntry.grid(row=5, column=1, sticky=(N, E, S, W))
        #for testing purposes
        #self.hostportEntry.insert(0, "6379")
        
        self.title = Label(self.frameHelpInfo,text = "")
        self.title.grid(row=6, column=0, columnspan=2, sticky=(N, E, S, W))

        self.passwordLabel = Label(self.frameHelpInfo,text ="Password: ")
        self.passwordLabel.grid(row=7, column=0, sticky=(E))

        self.passwordEntry= Entry(self.frameHelpInfo)
        self.passwordEntry.grid(row=7, column=1, sticky=(N, E, S, W))

        #button to close the connection window
        self.closeHelpButton = Button(self.rootConn, borderwidth=5, text = "Connect", command=self.connect)
        self.closeHelpButton.grid(row=1, column=0, sticky=(N, S, E, W))
        
        self.rootConn.mainloop()

    #close Help window
    def connect(self):
        #establishing connection with redis
        if not self.hostnameEntry.get(): self.redis_port = ""
        else: self.redis_host = self.hostnameEntry.get()
        if not self.hostportEntry.get(): self.redis_port = 0
        else: self.redis_port = (int(self.hostportEntry.get()))
        if not self.passwordEntry.get(): self.redis_password = ""
        else: self.redis_password = self.passwordEntry.get()

        self.client = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
        
        try:
            self.client.ping()
            self.rootConn.destroy()
        except (redis.exceptions.ConnectionError, 
            redis.exceptions.BusyLoadingError):
            messagebox.showerror("Connection Error", "Connection was not established. Please, review parameters and validate that Redis Server is up and running!")

    def getRedis(self):
        return self.client    
        
