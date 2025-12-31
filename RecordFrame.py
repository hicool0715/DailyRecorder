
from datetime import date
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from BasicFrame import BasicFrame
from YamlHandler import YamlHandler
from StartRecordFrame import StartRecordFrame
import threading
import datetime

class RecordFrame(BasicFrame):
    def __init__(self, record_name):
        self.record_name = record_name

    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        
        self.yaml_message = YamlHandler(YamlHandler.record_dir,str(date.today())+'.yaml').read_yaml()
        if self.yaml_message is None:
            self.yaml_message = {}
            self.yaml_message[self.record_name] = 0
        if self.record_name not in self.yaml_message:
            self.yaml_message[self.record_name] = 0
        self.record_text = tk.StringVar()
        self.start_record_time = datetime.datetime.now()
        
        # self.th = threading.Thread(target=self.update_label_cb)
        # self.lock = threading.Lock()
        # self.stop_thread_flag = False
        # self.th.start()
        self.update_label_cb(root.master)
        ttk.Label(self.main_frame, textvariable=self.record_text).grid(column=1, row=1, sticky=W)
        ttk.Button(self.main_frame, text="增加次数", command=lambda: self.update_count(1), bootstyle=PRIMARY).grid(column=1, row=2, sticky=W)
        ttk.Button(self.main_frame, text="减少次数", command=lambda: self.update_count(-1), bootstyle=PRIMARY).grid(column=2, row=2, sticky=W)
        ttk.Button(self.main_frame, text="重置次数", command=lambda: self.update_count(-self.yaml_message[self.record_name]), bootstyle=WARNING).grid(column=3, row=2, sticky=W)
        ttk.Button(self.main_frame, text="保存并返回", command=lambda: self.save_record(), bootstyle=SUCCESS).grid(column=1, row=3, sticky=W)
        ttk.Button(self.main_frame, text="取消并返回", command=lambda: self.showFrame(StartRecordFrame()), bootstyle=DANGER).grid(column=2, row=3, sticky=W)
    
        self.main_frame.columnconfigure(2, weight=1)
        for child in self.main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def update_count(self, count_change):
        self.yaml_message[self.record_name] += count_change
        self.record_text.set(f"记录内容：{self.record_name}  当前次数：{self.yaml_message[self.record_name]}")

    def save_record(self):
        self.record_text.set(f"记录内容：{self.record_name}，当前次数：{self.yaml_message[self.record_name]}，开始记录时间：{self.start_record_time.strftime("%Y-%m-%d %H:%M:%S")}，总计时：{(datetime.datetime.now() - self.start_record_time).strftime("%Y-%m-%d %H:%M:%S")}")

    # def update_label_cb(self):
    #     while True:
    #         print("4")
    #         self.lock.acquire()
    #         print("5")
    #         self.record_text.set(f"记录内容：{self.record_name}，当前次数：{self.yaml_message[self.record_name]}，开始记录时间：{self.start_record_time}，总计时：{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    #         print("5")
    #         if self.stop_thread_flag == True:
    #             print("stop thread")
                
    #             self.lock.release()
    #             break
    #         self.lock.release()
    #         print("3")
    #         import time
    #         time.sleep(0.1)


    def update_label_cb(self, root):
        diff = datetime.datetime.now() -  self.start_record_time
        self.record_text.set(f"记录内容：{self.record_name}，当前次数：{self.yaml_message[self.record_name]}，开始记录时间：{self.start_record_time.strftime("%Y-%m-%d %H:%M:%S")}，总计时：{int(diff.total_seconds())}")
        root.after(100, self.update_label_cb, root)
        


    # def destroyWidgets(self):
    #     print("1")
    #     self.lock.acquire()
    #     print("2")
    #     self.stop_thread_flag = True
    #     self.lock.release()
    #     print("waiting for stop")
    #     self.th.join()
    #     print("thread exited")
    #     self.main_frame.destroy()
