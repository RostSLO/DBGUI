'''
Created on January 5, 2021

@author: Rost
'''

try:
    from tkinter import ttk 
    import tkinter as tk 
except ImportError:
    from Tkinter import *

class MyTreeVeiw():
 
    def __init__(self, frameDB, redisClient):
        
        self.redisClient = redisClient
        self.dbList = []
        
        frameDB.grid_rowconfigure(0, weight=1)
        frameDB.grid_columnconfigure(0, weight=1)
        
        
        self.treeKeyItems = ttk.Treeview(frameDB, show='headings', selectmode='browse')
        self.treeKeyItems.grid(row=0, column=0, sticky=("NSEW"))
        
        # Calling pack method w.r.to vertical scrollbar 
        self.verscrlbar = ttk.Scrollbar(frameDB, orient ="vertical", command = self.treeKeyItems.yview) 
        self.verscrlbar.grid(row=0, column=1, sticky=("NSEW"))
        
        # Configuring treeview 
        self.treeKeyItems.configure(yscrollcommand = self.verscrlbar.set) 
        
        #set up columns   
        self.treeKeyItems["columns"]=("1")
        self.treeKeyItems.column("#0", width=30)
        self.treeKeyItems.column("1", width=240, minwidth=240)
        
        # Assigning the heading names to the respective columns 
        self.treeKeyItems.heading("#0", text ="#0")
        self.treeKeyItems.heading("1", text ="All keys") 
        
        self.drawTree(self.redisClient)
    
    #draw treeview with DB as a parent and keys as an elements    
    def drawTree(self, redisClient):
        if len(self.treeKeyItems.get_children()) > 0:
            self.treeKeyItems.delete(*self.treeKeyItems.get_children())
        #getting list of all dbs containing keys
        listOfDBs = redisClient.execute_command('info keyspace').split("\n")
        if listOfDBs:
            self.dbList.clear()
        #creating the list of db IDs for dbs containig keys
        for i in listOfDBs:
            if "db" in i:
                db = i.split(":", 1)[0][2:]
                self.dbList.append(db)
        for dbID in self.dbList:
            redisClient.execute_command('select ' + str(dbID))   
            #getting client list from redis
            clientList = redisClient.client_list()
            dbDict = clientList[0]
            dbName = '>>db' + dbDict['db']
            # Level 1
            dbLevel1 = self.treeKeyItems.insert(parent='', index='end', text=dbID, value=dbName)
            # Level 2        
            for key in redisClient.scan_iter():
                self.treeKeyItems.insert(parent=dbLevel1, index="end", text=dbID, value=[key]) 
        #open treeview children
        self.open_children(self.treeKeyItems.focus())
        redisClient.execute_command('select ' + str(self.dbList[0]))   

    def open_children(self, parent):
        self.treeKeyItems.item(parent, open=True)  # open parent
        for child in self.treeKeyItems.get_children(parent):
            self.open_children(child)  

        '''
        # iterate a list in batches of size n
def batcher(iterable, n):
    args = [iter(iterable)] * n
    return izip_longest(*args)

# in batches of 500 delete keys matching user:*
for keybatch in batcher(r.scan_iter('user:*'),500):
    r.delete(*keybatch)

scan_iter (
match: __class__=None,
count: __class__=None
)

match allows for filtering the keys by pattern

count allows for hint the minimum number of returns
    '''
        
        