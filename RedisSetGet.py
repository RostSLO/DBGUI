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
    
class RedisSetGet():
    
    def __init__(self, frameSetGet, redisClient):
        self.redisClient = redisClient
        self._drawElements(frameSetGet, redisClient)
        
    #set key value pair
    def setKeyValue(self, event):
        key = self.enterKeyEntry.get()
        value = self.enterValueText.get("1.0",END).rstrip()
        if key and value: 
            self.redisClient.set(key, value)
            messagebox.showinfo("Success", "Key : Value pair was successfully saved")
        else: messagebox.showwarning("Warning", "Enter a valid Key : Value pair")    
    
    #return value by key
    def getValue(self, key, redisClient):
        return redisClient.get(key)
    
    #find value by key    
    def findValue(self, event):
        key = self.enterKeyEntry.get()
        if key:
            val = self.getValue(key, self.redisClient)
            self.enterValueText.delete("1.0",END)
            self.enterValueText.insert(END, val)

    
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
        self.enterValueText.grid(row=3, column=0, rowspan=3, padx=5, pady=5, sticky=(N, E, S, W))
        
        self.verscrlbar=Scrollbar(frame, orient=VERTICAL, command=self.enterValueText.yview)
        self.verscrlbar.grid(row=3, column=1, rowspan=3, sticky=N+S+E+W)
        
        self.saveButton = Button(frame, borderwidth=5, text = "Save")
        self.saveButton.grid(row=3, column=2, sticky=(N, E, S, W))
        
        self.modifyButton = Button(frame, borderwidth=5, text = "Modify")
        self.modifyButton.grid(row=4, column=2, sticky=(N, E, S, W))
        
        self.deleteButton = Button(frame, borderwidth=5, text = "Delete")
        self.deleteButton.grid(row=5, column=2, sticky=(N, E, S, W))
        
        
        #when you click find button
        self.findButton.bind("<ButtonRelease-1>", self.findValue)        
    
        #when you click find button
        self.saveButton.bind("<ButtonRelease-1>", self.setKeyValue) 
   