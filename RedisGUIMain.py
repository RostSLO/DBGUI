'''
Created on January 2, 2021

@author: Rost
'''


import redis
import rejson
from MenuBar import MenuBar
from Connect import Conn
from RedisKeysTree import MyTreeVeiw 
from RedisSetGet import RedisSetGet
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *

#establish connection with Redis DB
conn=Conn()
redisClient = conn.getRedis()

#Creating a not resizable window
root = Tk()
root.title("SLORedis GUI")
root.geometry("800x475+200+100")
#root.resizable(False, False)
# change title bar icon
root.call('wm', 'iconphoto', root._w, "-default", PhotoImage(file='Pics\\logo.png'))

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)

root.grid_rowconfigure(0, weight=5)
root.grid_rowconfigure(1, weight=14)
root.grid_rowconfigure(2, weight=1)

#creating 4 frames: Menu, DBs, Set\Get, CLI, buttons
frameDB = Frame(root, borderwidth=5, relief="ridge")
frameDB.grid(row=0, column=0, rowspan=2, sticky=(W, N, S, E))

frameSetGet = Frame(root, borderwidth=5, relief="ridge")
frameSetGet.grid(row=0, column=1, sticky=(N, E, S, W))

frameCLI = Frame(root, borderwidth=5, relief="ridge")
frameCLI.grid(row=1, column=1, sticky=(N, E, S, W))

frameButtons = Frame(root, borderwidth=5, relief="ridge")
frameButtons.grid(row=2, column=0, columnspan=2, sticky=(N, E, W, S))

#creating a menu
menuMain = MenuBar(root)


def  selectItem(event):
    #get selected element
    curItem = tree.treeKeyItems.focus()
    #get dictionary from the selscted element
    dictElement = tree.treeKeyItems.item(curItem)
    #get value of the element
    [keyValue] = dictElement['values']
    #if we selsct key show it in the key : value field
    if tree.treeKeyItems.parent(curItem):
        #clean up and add clicked element to the key Entry
        setGet.enterKeyEntry.delete(0, END)
        setGet.enterKeyEntry.insert(0, keyValue)  
        #enter value for the selected Key
        setGet.findValue("<ButtonRelease-1>")


#creating a Treeview
tree = MyTreeVeiw(frameDB, redisClient)
#fill the tree
tree.treeKeyItems.bind('<Double-1>', selectItem)

#draw SetGet frame
setGet = RedisSetGet(frameSetGet, redisClient)


#Frame Button Section
#close Button
closeButton = Button(frameButtons, borderwidth=5, text = "Close")
closeButton.pack(side = RIGHT)



'''
redis_host = "localhost"
redis_port = 6379
redis_password = ""

client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

client.set("key1", "value1")

res = client.get("key1")
print(res)
'''

#close window
def closeWindow(event):
    root.destroy()

#when you click close button
closeButton.bind("<Button-1>", closeWindow)  

# display Menu 
root.config(menu = menuMain) 
root.mainloop()