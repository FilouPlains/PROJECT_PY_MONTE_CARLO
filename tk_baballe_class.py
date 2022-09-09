#! /usr/bin/env python3

# auteurs: Romain Retureau, Patrick Fuchs, Sept 2018

import tkinter as tk

# Classe principale qui hérite de la classe TkFrame
class AppliPrincipale(tk.Tk):
    def __init__(self):
        # Appel du constructeur de la classe mère (l'instance se retrouve dans le self)
        tk.Tk.__init__(self)
        # Définition des coordonnées (= attributs de la classe)
        self.x1, self.y1 = 10, 10 # coord ini
        self.dx, self.dy = 15, 0  # pas du deplacement
        self.flag = 0
        # création des widgets esclaves (qui seront inclus dans la fenêtre mère)
        self.canv = tk.Canvas(self, bg='dark gray', height=400, width=400)
        self.oval = self.canv.create_oval(self.x1, self.y1, self.x1+30, 
                                          self.y1+30, width=2, fill="red")
        btn1 = tk.Button(self, text="Quitter", command=self.quit)
        btn2 = tk.Button(self, text="Demarrer", command=self.start_it)
        btn3 = tk.Button(self, text="Arreter", command=self.stop_it)
        # Affichage des widgets
        self.canv.pack(side=tk.LEFT)
        btn1.pack(side=tk.BOTTOM)
        btn2.pack()
        btn3.pack()

    def move(self):
        """
        Deplacement de la baballe 
        """
        self.x1 += self.dx        
        self.y1 += self.dy
        if self.x1 > 360:
            self.x1, self.dx, self.dy = 360, 0, 15
        if self.y1 > 360:
            self.y1, self.dx, self.dy = 360, -15, 0
        if self.x1 < 10:
            self.x1, self.dx, self.dy = 10, 0, -15
        if self.y1 < 10:
            self.y1, self.dx, self.dy = 10, 15, 0
        # update coordinates
        self.canv.coords(self.oval, self.x1, self.y1, self.x1+30, self.y1+30)
        if self.flag > 0:
            self.after(50, self.move) # boucle toutes les 50ms 
       
    def start_it(self):
        """
        Demarrage de l'animation
        """
        self.flag += 1 # preferable a flag = 1
        if self.flag == 1:
            self.move()
            
    def stop_it(self):
        """
        Arret de l'animation
        """
        self.flag = 0        
        

if __name__ == "__main__":
    myapp = AppliPrincipale()
    myapp.title("Baballe !")
    myapp.mainloop()


