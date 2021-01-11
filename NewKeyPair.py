'''
Created on Jan. 10, 2020

@author: rboruk
'''
try:
    from tkinter import * 
    import tkinter.scrolledtext as st 
    from tkinter import messagebox    
except ImportError:
    from Tkinter import *

class NewKeyPairWin:
    def __init__(self, root, redisClient):
        
        self.redisClient = redisClient

        #Creating a not resizable window
        self.newKeyPairWin = Toplevel(root)
        self.newKeyPairWin.title("SLORedis GUI - new Key : value pair")
        self.newKeyPairWin.geometry("520x268+500+100")
        self.newKeyPairWin.resizable(False, False)
        # change title bar icon
        #self.newKeyPairWin.call('wm', 'iconphoto', self.rootHelp._w, self.icon)
        
     
        #frame to provide information
        self.frame = Frame(self.newKeyPairWin, borderwidth=5, relief="ridge", height=340, width=395)
        self.frame.grid(row=0, column=0, sticky=(N, S, E, W))
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=4)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        #frame for buttons
        self.frameButton = Frame(self.newKeyPairWin, borderwidth=5, relief="ridge", height=55, width=395)
        self.frameButton.grid(row=1, column=0, sticky=(N, S, E, W))
        
        self.frameButton.grid_rowconfigure(0, weight=1)
        self.frameButton.grid_columnconfigure(0, weight=1)
        self.frameButton.grid_columnconfigure(1, weight=1)

        #create labels and entries for key and value
        self.enterKeyLabel = Label(self.frame, text = "Key")
        self.enterKeyLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=(W)) 
    
        self.enterKeyEntry = Entry(self.frame,text = "")
        self.enterKeyEntry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(N, E, S, W)) 
        
        self.enterValueLabel = Label(self.frame,text = "Value")
        self.enterValueLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=(W)) 
        
        self.enterValueText = Text(self.frame, height=7, width=60)
        self.enterValueText.grid(row=3, column=0, padx=5, pady=5, sticky=(N, E, S, W))
        
        self.verscrlbar=Scrollbar(self.frame, orient=VERTICAL, command=self.enterValueText.yview)
        self.verscrlbar.grid(row=3, column=1, sticky=N+S+E+W)



        #button to save the pair
        self.saveButton = Button(self.frameButton, borderwidth=5, text = "Save", command=self.saveNewPair)
        self.saveButton.grid(row=0, column=0, sticky=(N, S, E, W))    
    
        #button to close the window
        self.closeButton = Button(self.frameButton, borderwidth=5, text = "Close", command=self.endWin)
        self.closeButton.grid(row=0, column=1, sticky=(N, S, E, W))

        self.newKeyPairWin.mainloop()
        
    #close Help window
    def endWin(self):
        self.newKeyPairWin.destroy()
    
    #save new pair
    def saveNewPair(self):
        key = self.enterKeyEntry.get()
        value = self.enterValueText.get("1.0",END).rstrip()
        if key and value: 
            self.redisClient.set(key, value)
            messagebox.showinfo("Success", "Key : Value pair was successfully saved")
            self.newKeyPairWin.destroy()
        else: 
            messagebox.showwarning("Warning", "Enter a valid Key : Value pair", parent=self.newKeyPairWin) 
       
