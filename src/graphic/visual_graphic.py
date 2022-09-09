 # Importation of other python module.
import numpy as np
import sys
import tkinter as tk

# Importation of "homemade" python module.
import amino_acid_class.sequence_manipulator as clattrib


class GraphicalRepresentation:
    RADIUS = 15
    DIST_SHAPE_DRAW_AREA = 10 + RADIUS * 1

    def __init__(self, seq_manip, model_list):
        self.seq_manip = seq_manip
        self.model_list = model_list

        x_range = np.max(self.seq_manip[0]) - np.min(self.seq_manip[0])
        y_range = np.max(self.seq_manip[1]) - np.min(self.seq_manip[1])

        self.display_seq = tk.Tk()

        # Main frame, you can't be bigger than that.
        frame = tk.Frame(self.display_seq, width=600, height=400)
        frame.pack(expand=True, fill=tk.BOTH)

        # Zone where the draw are going to be
        self.draw_area = tk.Canvas(
            frame,
            bg="white",
            # How much can we scroll, with x1, y1, x2, y2.
            scrollregion=(
                0,
                0,
                x_range * self.RADIUS * 2 + self.DIST_SHAPE_DRAW_AREA * 2,
                y_range * self.RADIUS * 2 + self.DIST_SHAPE_DRAW_AREA * 2
            ),
            width=600,
            height=400
        )

        # Define de horizontal scrolling bar.
        h_bar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        h_bar.pack(side=tk.BOTTOM, fill=tk.X)
        h_bar.config(command=self.draw_area.xview)

        # Define de vertical scrolling bar.
        v_bar = tk.Scrollbar(frame, orient=tk.VERTICAL)
        v_bar.pack(side=tk.RIGHT, fill=tk.Y)
        v_bar.config(command=self.draw_area.yview)

        # Put the scroll bar.
        self.draw_area.config(xscrollcommand=h_bar.set,
                              yscrollcommand=v_bar.set)
        self.draw_area.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.draw_area.pack()

    def draw(self):
        upper_left = self.seq_manip * self.RADIUS * 2 - self.RADIUS
        downer_right = self.seq_manip * self.RADIUS * 2 + self.RADIUS

        min_x = np.min(upper_left[0])
        min_y = np.min(upper_left[1])

        if min_x <= 0:
            min_x = -min_x + self.RADIUS

            upper_left[0] = upper_left[0] + min_x
            downer_right[0] = downer_right[0] + min_x
        if min_y <= 0:
            min_y = -min_y + self.RADIUS

            upper_left[1] = upper_left[1] + min_y
            downer_right[1] = downer_right[1] + min_y

        for i in range(len(upper_left[0])):
            self.__draw_amino_acid(
                upper_left[0, i],
                upper_left[1, i],
                downer_right[0, i],
                downer_right[1, i],
                self.model_list[i]
            )

            if i > 0:
                self.__draw_bond(
                    upper_left[0, i - 1],
                    upper_left[1, i - 1],
                    upper_left[0, i],
                    upper_left[1, i],
                )

    def __draw_amino_acid(self, x_1, y_1, x_2, y_2, model):
        if model == "H":
            color = "#2e2e3e"
        elif model == "P":
            color = "#aaaaca"
        else:
            sys.exit(f"ERROR: Model '{model}' given is wrong. Choice available"
                     " are 'H' or 'P'.")

        self.draw_area.create_oval(
            # Up left point.
            x_1,
            y_1,
            # Down right point.
            x_2,
            y_2,
            # Colors.
            outline="white",
            fill=color
        )

    def __draw_bond(self, x_1, y_1, x_2, y_2):
        self.draw_area.create_line(
            # Up left point.
            x_1 + self.RADIUS,
            y_1 + self.RADIUS,
            # Down right point.
            x_2 + self.RADIUS,
            y_2 + self.RADIUS,
            # Colors.
            fill="white",
            width=3
        )

    def display_window(self):
        self.display_seq.title("SEQUENCE DISPLAYER")
        self.display_seq.mainloop()
