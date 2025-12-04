import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from BasicFrame import BasicFrame
class StartRecordFrame(BasicFrame):
    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.main_frame, text="请输入要记录的内容").grid(column=1, row=1, sticky=W)
        record_name = tk.StringVar()
        ttk.Entry(self.main_frame, width=20, textvariable=record_name).grid(column=2, row=1, sticky=(W, E))
        from RecordFrame import RecordFrame
        from EntranceFrame import EntranceFrame
        ttk.Button(self.main_frame, text="确认", command=lambda: self.showFrame(RecordFrame(record_name.get())), bootstyle=SUCCESS).grid(column=1, row=2, sticky=W)
        ttk.Button(self.main_frame, text="返回", command=lambda: self.showFrame(EntranceFrame()), bootstyle=DANGER).grid(column=2, row=2, sticky=W)