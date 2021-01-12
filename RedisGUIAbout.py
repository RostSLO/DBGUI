'''
Created on Jan. 11, 2021

@author: rboruk
'''
try:
    from tkinter import * 
    import tkinter.scrolledtext as st 
except ImportError:
    from Tkinter import *

class InfoWindow:
    def __init__(self, master):

        #Creating a not resizable window
        self.rootHelp = Toplevel(master)
        self.rootHelp.title("RedisGUI About")
        self.rootHelp.geometry("600x440+500+100")
        self.rootHelp.resizable(False, False)

        
        #game rules describedhere
        guideText="""This GUI was built to provide basic capabilities to work with Redis DB mostly for learning purposes. 
In the current version, RedisGUI supports the simple CLI and commands like:
        SET Key : Value pair
        GET Key : Value pair
        Modify Key
        Modify Value
        Delete Key : Value pair

Enjoy!!!
"""

        #frame to provide information
        self.frameHelpInfo = Frame(self.rootHelp, borderwidth=5, relief="ridge", height=395, width=395)
        self.frameHelpInfo.grid(row=0, column=0, sticky=(N, S, E, W))
        
        self.frameHelpInfogameRules = st.ScrolledText(self.frameHelpInfo, fg="#3366CC", width=70)
        self.frameHelpInfogameRules.grid(row=0, column = 0, pady = 5, padx = 5, sticky=(N, S, E, W))
        self.frameHelpInfogameRules.insert(INSERT, guideText)
        self.frameHelpInfogameRules.config(state=DISABLED)
     
        #button to close the game
        self.closeHelpButton = Button(self.rootHelp, borderwidth=5, text = "Close", command=self.endHelp)
        self.closeHelpButton.grid(row=1, column=0, sticky=(N, S, E, W))
        
    #close Help window
    def endHelp(self):
        self.rootHelp.destroy()
        
        
        self.rootHelp.mainloop()