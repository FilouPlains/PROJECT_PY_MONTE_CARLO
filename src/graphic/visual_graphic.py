import tkinter as tk

racine = tk.Tk()
canv = tk.Canvas(racine, bg="white", height=200, width=400)
canv.pack()
canv.create_oval(400 - 150, 50, 150, 150, outline="white", fill="red")
racine.mainloop()
