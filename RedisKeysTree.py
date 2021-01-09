'''
Created on January 5, 2021

@author: Rost
'''

try:
    from tkinter import ttk 
    import tkinter as tk 
except ImportError:
    from Tkinter import *

class MyTreeVeiw(ttk.Treeview):
    
    def __init__(self, frameDB, *args, **kwargs):
           
        ttk.Treeview.__init__(self, frameDB, *args, **kwargs)
        
        # Calling pack method w.r.to vertical scrollbar 
        verscrlbar = ttk.Scrollbar(frameDB,  
                           orient ="vertical",  
                           command = self.yview) 
        
        verscrlbar.pack(side ='right', fill ='x')
        
        # Configuring treeview 
        self.configure(xscrollcommand = verscrlbar.set) 
        
        #set up columns   
        self["columns"]=("1")
        self.column("1", width=270, minwidth=270, stretch=tk.NO)
        
        # Assigning the heading names to the respective columns 
        self.heading("1", text ="All keys") 
        
    def drawTree(self, redisClient):
        # Level 1
        #db = self.insert("", 1, "", text="db0")

        # Level 2
        for key in redisClient.scan_iter("user:*"):
            self.insert(db, "end", "", text=key)
       
        
        
        