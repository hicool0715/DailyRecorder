import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from YamlHandler import YamlHandler
from datetime import date

from BasicFrame import BasicFrame
class StartRecordFrame(BasicFrame):
    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        label_frame = ttk.Frame(self.main_frame, padding=(3, 3, 12, 12))
        label_frame.pack(side=tk.TOP)
        ttk.Label(label_frame, text="请输入要记录的内容").grid(column=1, row=1, sticky=W)
        record_name = tk.StringVar()
        ttk.Entry(label_frame, width=20, textvariable=record_name).grid(column=2, row=1, sticky=(W, E))

        yaml_message = YamlHandler(YamlHandler.record_dir, str(date.today()) + '.yaml').read_yaml()

        if yaml_message is not None:
            recorded_cbx = ttk.Combobox(label_frame, values=list(yaml_message.keys()), state="readonly")
            recorded_cbx.grid(column=3, row=1, sticky=(W, E))
            recorded_cbx.bind("<<ComboboxSelected>>", lambda e: record_name.set(recorded_cbx.get()))
            recorded_cbx.set("从已有记录中选择")

        from RecordFrame import RecordFrame
        from EntranceFrame import EntranceFrame
        ttk.Button(self.main_frame, text="确认", command=lambda: self.showFrame(RecordFrame(record_name.get())), bootstyle=SUCCESS).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.main_frame, text="返回", command=lambda: self.showFrame(EntranceFrame()), bootstyle=DANGER).pack(side=tk.RIGHT, padx=5)