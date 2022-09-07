# Importation of other python module.
import sys
import tkinter as tk

# Importation of "homemade" python module.
import amino_acid_class.sequence_manipulator as clattrib

class GraphicalRepresentation:
    RADIUS = 20
    
    def __init__(self, seq_manip):
        self.seq_manip = seq_manip
        
        self.display_seq = tk.Tk()

        self.window = tk.Canvas(self.display_seq, bg="white", height=200, width=400)
        self.window.pack()
    
    def draw_amino_acid(self, x, y, model):
        if model == "H":
            color = "#2e2e3e"
        elif model == "P":
            color = "#aaaaca"
        else:
            sys.exit(f"ERROR: Wrong model given. Choice available are 'H' or"
                     " 'P'.")
        
        self.window.create_oval(
            # Up left point.
            x - self.RADIUS,
            y - self.RADIUS,
            # Down right point.
            x + self.RADIUS,
            y + self.RADIUS,
            # Colors.
            outline="white",
            fill=color
        )
        
    def display_window(self):
        self.display_seq.title("AMINO ACID SEQUENCE DISPLAY")
        self.display_seq.mainloop()
