'''
Created on January 2, 2021

@author: Rost
'''


import redis
from MenuBar import MenuBar
from Connect import Conn
from RedisKeysTree import MyTreeVeiw 
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

root.grid_rowconfigure(0, weight=7)
root.grid_rowconfigure(1, weight=11)
root.grid_rowconfigure(2, weight=2)

#creating 4 frames: Menu, DBs, Set\Get, CLI, buttons
frameDB = Frame(root, borderwidth=5, relief="ridge", bg='blue', width=200, height=400)
frameDB.grid(row=0, column=0, rowspan=2, sticky=(W, N, S, E))

frameSetGet = Frame(root, borderwidth=5, relief="ridge", bg='red', width=600, height=250)
frameSetGet.grid(row=0, column=1, sticky=(N, E, S, W))

frameCLI = Frame(root, borderwidth=5, relief="ridge", bg='green', width=600, height=150)
frameCLI.grid(row=1, column=1, sticky=(N, E, S, W))

frameButtons = Frame(root, borderwidth=5, relief="ridge", bg='yellow', width=200, height=50)
frameButtons.grid(row=2, column=0, columnspan=2, sticky=(N, E, W, S))

#creating a menu
menuMain = MenuBar(root)

#creating a Treeview
tree = MyTreeVeiw(frameDB, redisClient)

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