import tkinter as tk

from numpy import column_stack
import PyPDF2
from PIL import Image, ImageTk

root=tk.Tk()
canva = tk.Canvas(root, width=500, height=700)
canva.grid(columnspan=3)

logo=Image.open("logo.png")

root.mainloop()