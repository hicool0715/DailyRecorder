import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from BasicFrame import BasicFrame
class MainFrame(BasicFrame):
    def createFrame(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=1, row=2, sticky=(N, W, E, S))
        ttk.Combobox(self.main_frame).grid(column=1, row=1, sticky=(N, E))
        interactive_frame = ttk.Frame(self.main_frame, padding=(3, 3, 12, 12))
        interactive_frame.grid(column=1, row=2, sticky=(N, W, E, S))
        
        from EntranceFrame import EntranceFrame
        self.showFrame(EntranceFrame())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("o mini beimei hong")
    MainFrame().createFrame(root)
    root.mainloop()