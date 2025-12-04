from RecordFrame import RecordFrame
from ShowFrame import ShowFrame
from tkinter import *
from tkinter import ttk

class EntranceFrame:
    def __init__(self):
        root = Tk()
        root.title("o mini beimei hong")
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe, text="请选择操作：").grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text="开始记录", command=lambda:RecordFrame(root)).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text="查看记录", command=lambda:ShowFrame(root)).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="退出", command=lambda: root.quit()).grid(column=1, row=4, sticky=W)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        root.mainloop() 

if __name__ == '__main__':
    EntranceFrame()