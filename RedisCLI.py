'''
Created on January 8, 2021

@author: Rost
'''

from test.test_tracemalloc import frame
import keyboard
from pynput.keyboard import Listener
from symbol import except_clause
try:
    from tkinter import * 
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
    
class RedisCLI():
    
    def __init__(self, frame, redisClient, tree, host, port):
        
        self.frame = frame
        self.redisClient = redisClient
        self.tree = tree 
        self.host = host
        self.port = port
        self.lastLine = ''
        self.keyPressed = False
        
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
       
        self.enterCLIText = Text(self.frame, heigh=10, bg="black", fg="#00FF00", font=("Cascadia Code", 11, "bold"))
        self.enterCLIText.grid(row=0, column=0, padx=5, pady=5, sticky=(N, E, S, W))
        
        
        self.verscrlbar=Scrollbar(frame, orient=VERTICAL, command=self.enterCLIText.yview)
        self.verscrlbar.grid(row=0, column=1, sticky=N+S+E+W)
        
        self.hostPort = self.host + ":" + str(self.port) + ">> "
        
        self.enterCLIText.insert(END, self.hostPort)
        
        self.enterCLIText.bind('<Key>', self.runCommand)
        self.enterCLIText.bind('<KeyRelease>', self.runCommand)
        
    def CLICommand(self, command):
        #execute command
        try:
            res = self.redisClient.execute_command(command)
            if res:
                if (isinstance(res, int)):
                    self.enterCLIText.insert(END, "\n(integer) " + str(res))
                else:
                    self.enterCLIText.insert(END, "\n" + res)
                self.tree.drawTree(self.redisClient)
        except:
            #if command is unknown show error message and new line
            self.enterCLIText.insert(END, "\n '" + command + "' is not recognized as an internal or external command")

        
    def runCommand(self, event): 
        #print("i am in")
        if self.keyPressed:
            self.hostPort = self.host + ":" + str(self.port) + ">> "
            self.enterCLIText.see(END)
            self.enterCLIText.insert(END, self.hostPort)
            self.keyPressed = False
        if keyboard.is_pressed("\n"):
            listRows = self.enterCLIText.get('current linestart',END).split("\n")
            self.hostPort = self.host + ":" + str(self.port) + ">> "
            command = listRows[len(listRows)-2].replace(self.hostPort, '')
            command = command.replace("'", "\\'").replace('"', '\\"')
            self.CLICommand(command)
            self.keyPressed = True
