'''
Created on January 8, 2021

@author: Rost
'''
import redis
from redis.client import StrictRedis
from ctypes.test import test_objects
try:
    from tkinter import * 
    from tkinter import messagebox
except ImportError:
    from Tkinter import *

class NewKeyValue():
    
    def __init__(self, root, key, redisClient, enterKeyEntry):
        
        self.key = key
        self.redisClient = redisClient
        self.root = root
        self.rootKeyEntry = enterKeyEntry
        
        #Creating a not resizable window
        self.NewKeyValueWin = Toplevel(root)
        self.NewKeyValueWin.title("SLORedis GUI - new Key value")
        self.NewKeyValueWin.geometry("300x73+500+100")
        self.NewKeyValueWin.resizable(False, False)
        # change title bar icon
        #self.newKeyPairWin.call('wm', 'ic -onphoto', self.rootHelp._w, self.icon)
        
     
        #frame to provide information
        self.frame = Frame(self.NewKeyValueWin, borderwidth=5, relief="ridge")
        self.frame.grid(row=0, column=0, sticky=(N, S, E, W))
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

        self.frame.grid_columnconfigure(0, weight=4)
        self.frame.grid_columnconfigure(1, weight=1)

        #create labels and entries for key
        self.enterKeyLabel = Label(self.frame, text = "Key")
        self.enterKeyLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=(W)) 
    
        self.enterKeyEntry = Entry(self.frame,text = "", width=46)
        self.enterKeyEntry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(N, E, S, W)) 

        #button to modify Key value
        self.okButton = Button(self.frame, borderwidth=5, text = "Ok", command=self.modifyValue)
        self.okButton.grid(row=1, column=1, sticky=(N, S, E, W))

        self.NewKeyValueWin.mainloop()
        
    def modifyValue(self):
        newKey = self.enterKeyEntry.get()
        if newKey:
            #update the key
            self.redisClient.rename(self.key, newKey)
            messagebox.showinfo("Success", "Key was successfully renamed")
            self.rootKeyEntry.delete(0, END)
            self.rootKeyEntry.insert(0, newKey)
            self.NewKeyValueWin.destroy()
    
class RedisSetGet():
    
    def __init__(self, frameSetGet, redisClient, tree):
        self.redisClient = redisClient
        self.frame = frameSetGet
        self._drawElements(frameSetGet, redisClient)
        self.tree = tree
        
    #set key value pair
    def setKeyValue(self, event):
        key = self.enterKeyEntry.get()
        value = self.enterValueText.get("1.0",END).rstrip()
        if key and value: 
            self.redisClient.set(key, value)
            messagebox.showinfo("Success", "Key : Value pair was successfully saved")
            self.tree.drawTree(self.redisClient)
        else: messagebox.showwarning("Warning", "Enter a valid Key : Value pair")    

    #modify key value pair
    def modifyKey(self, event):
        key = self.enterKeyEntry.get()
        if key: 
            val = self.getValue(key, self.redisClient)
            if val:
                #enter new key
                NewKeyValue(self.frame, key, self.redisClient, self.enterKeyEntry)
                self.tree.drawTree(self.redisClient)
            else: messagebox.showwarning("Warning", "Enter a valid Key")             
        else: messagebox.showwarning("Warning", "Enter a valid Key")  
    
    #return value by key
    def getValue(self, key, redisClient):
        if redisClient.get(key): return redisClient.get(key)
        return ""
    
    #find value by key    
    def findValue(self, event):
        key = self.enterKeyEntry.get()
        if key:
            val = self.getValue(key, self.redisClient)
            if val:
                self.enterValueText.delete("1.0",END)
                self.enterValueText.insert(END, val)
            else: 
                self.enterValueText.delete("1.0",END)
                messagebox.showwarning("Warning", "Could not find value for the Key") 
    
    def _drawElements(self, frame, redisClient):        
        
        #frame grid configuration
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_rowconfigure(3, weight=4)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_rowconfigure(5, weight=1)        

        
        frame.grid_columnconfigure(0, weight=1)
               
        #create labels and entries for key and value
        self.enterKeyLabel = Label(frame, text = "Key")
        self.enterKeyLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=(W)) 
    
        self.enterKeyEntry = Entry(frame,text = "")
        self.enterKeyEntry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(N, E, S, W)) 
        
        self.findButton = Button(frame, text="Find")
        self.findButton.grid(row=1, column=2, padx=5, pady=5, sticky=(E))      
        
        self.enterValueLabel = Label(frame,text = "Value")
        self.enterValueLabel.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=(W)) 
        
        self.enterValueText = Text(frame, height=7, width=60)
        self.enterValueText.grid(row=3, column=0, rowspan=4, padx=5, pady=5, sticky=(N, E, S, W))
        
        self.verscrlbar=Scrollbar(frame, orient=VERTICAL, command=self.enterValueText.yview)
        self.verscrlbar.grid(row=3, column=1, rowspan=4, sticky=N+S+E+W)
        
        self.saveButton = Button(frame, borderwidth=5, text = "Save")
        self.saveButton.grid(row=3, column=2, sticky=(N, E, S, W))
        
        self.modifyKeyButton = Button(frame, borderwidth=5, text = "Modify Key")
        self.modifyKeyButton.grid(row=4, column=2, sticky=(N, E, S, W))
                
        self.modifyValueButton = Button(frame, borderwidth=5, text = "Modify Value")
        self.modifyValueButton.grid(row=5, column=2, sticky=(N, E, S, W))
        
        self.deleteButton = Button(frame, borderwidth=5, text = "Delete")
        self.deleteButton.grid(row=6, column=2, sticky=(N, E, S, W))
        
        
        #when you click find button
        self.findButton.bind("<ButtonRelease-1>", self.findValue)        
    
        #when you click save button
        self.saveButton.bind("<ButtonRelease-1>", self.setKeyValue) 
        
        #when you modify Key button
        self.modifyKeyButton.bind("<ButtonRelease-1>", self.modifyKey)    
            
        #when you modify Value button
        self.modifyValueButton.bind("<ButtonRelease-1>", self.setKeyValue)       