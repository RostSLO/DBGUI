'''
Created on January 4, 2021

@author: Rost
'''

try:
    import tkinter as tk
    from tkinter.ttk import * 
except ImportError:
    from Tkinter import *

class MenuBar(tk.Menu):
    
    def __init__(self, root, *args, **kwargs):
           
        tk.Menu.__init__(self, root, *args, **kwargs)
          
        # Adding File Menu and commands 
        keyValue = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Key / Value', menu = keyValue) 
        keyValue.add_command(label ='New pair', command = None) 
        keyValue.add_command(label ='Modify', command = None) 
        keyValue.add_command(label ='Delete', command = None) 
        keyValue.add_separator() 
        keyValue.add_command(label ='Exit', command = root.destroy) 
          
        # Adding Help Menu 
        help_ = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='SLORedis Help', command = None) 
        help_.add_separator() 
        help_.add_command(label ='About SLORedis', command = None)
        