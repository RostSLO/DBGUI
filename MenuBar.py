'''
Created on January 4, 2021

@author: Rost
'''

#from time import strftime 
try:
    import tkinter as tk
    from tkinter.ttk import * 
except ImportError:
    from Tkinter import *

class MenuBar(tk.Menu):
    
    def __init__(self, root, *args, **kwargs):
           
        tk.Menu.__init__(self, root, *args, **kwargs)
          
        # Adding File Menu and commands 
        file = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='File', menu = file) 
        file.add_command(label ='New File', command = None) 
        file.add_command(label ='Open...', command = None) 
        file.add_command(label ='Save', command = None) 
        file.add_separator() 
        file.add_command(label ='Exit', command = root.destroy) 
          
        # Adding Edit Menu and commands 
        edit = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Edit', menu = edit) 
        edit.add_command(label ='Cut', command = None) 
        edit.add_command(label ='Copy', command = None) 
        edit.add_command(label ='Paste', command = None) 
        edit.add_command(label ='Select All', command = None) 
        edit.add_separator() 
        edit.add_command(label ='Find...', command = None) 
        edit.add_command(label ='Find again', command = None) 
          
        # Adding Help Menu 
        help_ = tk.Menu(self, tearoff = 0) 
        self.add_cascade(label ='Help', menu = help_) 
        help_.add_command(label ='SLORedis Help', command = None) 
        help_.add_command(label ='Demo', command = None) 
        help_.add_separator() 
        help_.add_command(label ='About SLORedis', command = None)
        