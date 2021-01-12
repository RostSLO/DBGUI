'''
Created on January 4, 2021

@author: Rost
'''

from NewKeyPair import NewKeyPairWin
from RedisGUIAbout import InfoWindow
try:
    import tkinter as tk
    from tkinter.ttk import * 
except ImportError:
    from Tkinter import *

class MenuBar(tk.Menu):
    
    def __init__(self, root, redisClient, tree, *args, **kwargs):
        
        self.root = root 
        self.redisClient = redisClient
        self.tree = tree
           
        tk.Menu.__init__(self, root, *args, **kwargs)
          
        # Adding Key : Value pair Menu and commands 
        keyValue = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Key / Value', menu = keyValue) 
        keyValue.add_command(label ='New pair', command = self.newKeyPair) 
        keyValue.add_separator() 
        keyValue.add_command(label ='Exit', command = root.destroy) 
          
        # Adding Help Menu 
        help_ = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='About SLORedis', command = self.callInfoWin)
     
    def callInfoWin(self):
        app = InfoWindow(self.root)  
    
    def newKeyPair(self):
        newKeyPair = NewKeyPairWin(self.root, self.redisClient, self.tree)

        