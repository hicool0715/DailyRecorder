import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from BasicFrame import BasicFrame
class EntranceFrame(BasicFrame):
    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        ttk.Label(self.main_frame, text="请选择操作：").pack(side=(tk.LEFT))
        from StartRecordFrame import StartRecordFrame
        from ShowRecordFrame import ShowRecordFrame
        ttk.Button(self.main_frame, text="开始记录", command=lambda: self.showFrame(StartRecordFrame()), bootstyle=PRIMARY).pack(side=tk.LEFT, padx=10)
        ttk.Button(self.main_frame, text="查看记录", command=lambda: self.showFrame(ShowRecordFrame()), bootstyle=SUCCESS).pack(side=tk.LEFT, expand=TRUE, padx=10)
        ttk.Button(self.main_frame, text="退出", command=lambda: root.quit(), bootstyle=DANGER).pack(side=tk.RIGHT, padx=10)

    