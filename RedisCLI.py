'''
Created on January 8, 2021

@author: Rost
'''
#import redis
#from redis.client import StrictRedis
#from ctypes.test import test_objects
from test.test_tracemalloc import frame
try:
    from tkinter import * 
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
    
class RedisCLI():
    
    def __init__(self, frame, redisClient, tree):
        
        self.frame = frame
        self.redisClient = redisClient
        self.tree = tree 
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        self.enterCLIText = Text(self.frame, bg="black", fg="#00FF00", font=("Cascadia Code", 11, "bold"))
        self.enterCLIText.grid(row=0, column=0, padx=5, pady=5, sticky=(N, E, S, W))
        
        self.verscrlbar=Scrollbar(frame, orient=VERTICAL, command=self.enterCLIText.yview)
        self.verscrlbar.grid(row=0, column=1, sticky=N+S+E+W)
        
        self.enterCLIText.insert(END, ">>")
        