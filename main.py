import tkinter as tk
from tkinter import messagebox
from moteur_de_jeu import GameOfLife
from interface import GameOfLifeGUI

class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de la Vie")
        self.root.geometry("800x600")
        self.root.config(bg="#2e3b4e")
        
        self.game = GameOfLife(size=50)
        
        # Page d'accueil
        self.create_home_screen()

    def create_home_screen(self):
        """Crée l'écran d'accueil."""
        # Titre du jeu
        title_label = tk.Label(self.root, text="Jeu de la Vie", font=("Helvetica", 32), fg="white", bg="#2e3b4e")
        title_label.pack(pady=50)

        # Boutons
        start_button = tk.Button(self.root, text="Démarrer le Jeu", font=("Helvetica", 14), fg="white", bg="#58a6ff", command=self.start_game)
        start_button.pack(pady=20)

        rules_button = tk.Button(self.root, text="Règles du Jeu", font=("Helvetica", 14), fg="white", bg="#58a6ff", command=self.show_rules)
        rules_button.pack(pady=20)

    def start_game(self):
        """Démarre le jeu en affichant l'interface de jeu."""
        self.clear_screen()
        gui = GameOfLifeGUI(self.game, self.root)

    def show_rules(self):
        """Affiche les règles du jeu dans une boîte de dialogue."""
        rules = (
            "Règles du Jeu de la Vie :\n"
            "- Une cellule vivante survit si elle a 2 ou 3 voisins vivants.\n"
            "- Une cellule vivante meurt de solitude ou de surpopulation.\n"
            "- Une cellule morte peut devenir vivante si elle a exactement 3 voisins vivants.\n"
            "Les structures qui apparaissent incluent les oscillateurs, planeurs, et plus encore."
        )
        messagebox.showinfo("Règles du Jeu", rules)

    def clear_screen(self):
        """Efface tous les widgets de l'écran actuel pour passer au jeu."""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = GameOfLifeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()