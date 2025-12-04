import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from BasicFrame import BasicFrame
class MainFrame(BasicFrame):
    def createFrame(self, root):
        ttk.Style('cosmo')
        global_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        global_frame.grid(column=1, row=2, sticky=(N, W, E, S))

        style_text = ttk.StringVar()
        style_text.set(["a", "b", "c", "d"])
        style_cbx = ttk.Combobox(global_frame, text="style",values=['cosmo', 'flatly', 'journal', 'litera', 'lumen', 'minty', 'pulse', 'sandstone', 'united', 'yeti', 'morph', 'simplex', 'cerculean', 'solar', 'superhero', 'darkly', 'cyborg', 'vapor'], state='readonly')
        style_cbx.grid(column=0, row=0, sticky=(N, E))
        style_cbx.current(0)
        style_cbx.bind("<<ComboboxSelected>>", lambda event: ttk.Style(style_cbx.get()))
        
        self.main_frame = ttk.Frame(global_frame, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        
        from EntranceFrame import EntranceFrame
        self.showFrame(EntranceFrame())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Daily Recorder")
    MainFrame().createFrame(root)
    root.mainloop()