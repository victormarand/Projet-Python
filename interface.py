import tkinter as tk
from tkinter import colorchooser, messagebox
from moteur_de_jeu import GameOfLife 

class GameOfLifeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de la Vie")
        self.root.geometry("1000x700")
        self.root.config(bg="#2e3b4e")
        self.game = GameOfLife(size=50)
        self.cell_size = 10
        self.offset_x = 0
        self.offset_y = 0
        self.cell_color_alive = "#00FF00" 
        self.cell_color_dead = "#FFFFFF"  
        self.create_home_screen()

    def create_home_screen(self):
        """Crée l'écran d'accueil avec les options de démarrage et règles."""
        self.clear_screen()
        title_label = tk.Label(self.root, text="Jeu de la Vie", font=("Helvetica", 32, "bold"), fg="#FFFFFF", bg="#2e3b4e")
        title_label.pack(pady=50)
        start_button = self.create_button(self.root, "Démarrer le Jeu", self.start_game)
        start_button.pack(pady=20)
        rules_button = self.create_button(self.root, "Règles du Jeu", self.show_rules)
        rules_button.pack(pady=20)

    def start_game(self):
        """Affiche l'interface de jeu avec la grille et les options."""
        self.clear_screen()
        self.is_running = False 
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="#1e2b34", highlightthickness=0)
        self.canvas.grid(row=0, column=1, padx=20, pady=20)
        self.canvas.bind("<Button-1>", self.toggle_cell_with_mouse)
        self.canvas.bind("<MouseWheel>", self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.panel = tk.Frame(self.root, bg="#2e3b4e")
        self.panel.grid(row=0, column=0, padx=20, pady=20, sticky="ns")
        self.create_buttons()
        self.save_load_panel = tk.Frame(self.root, bg="#2e3b4e")
        self.save_load_panel.grid(row=0, column=2, padx=10, pady=10, sticky="ne")
        self.create_save_load_buttons()
        back_button = self.create_button(self.root, "Retour au menu", self.create_home_screen, width=15, font_size=10)
        back_button.grid(row=1, column=1, pady=20)
        self.randomize_grid()
        self.update_grid_display()

    def create_buttons(self):
        """Crée les boutons sur le panneau latéral pour contrôler le jeu."""
        self.start_stop_button = self.create_button(self.panel, "Play", self.play_stop_game)
        self.start_stop_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        next_step_button = self.create_button(self.panel, "Étape suivante", self.run_single_step)
        next_step_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        random_button = self.create_button(self.panel, "Aléatoire", self.randomize_grid)
        random_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        reset_button = self.create_button(self.panel, "Réinitialiser", self.reset_grid)
        reset_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        color_button = self.create_button(self.panel, "Choix couleurs", self.change_cell_color)
        color_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

    def create_save_load_buttons(self):
        """Crée les boutons de sauvegarde et chargement dans le panneau de droite."""
        save_button = self.create_button(self.save_load_panel, "Sauvegarder", self.save_grid, width=15, font_size=10)
        save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ne")

        load_button = self.create_button(self.save_load_panel, "Charger", self.load_grid, width=15, font_size=10)
        load_button.grid(row=1, column=0, padx=5, pady=5, sticky="ne")

    def create_button(self, container, text, command, width=20, font_size=14):
        """Crée un bouton stylisé avec effets de survol."""
        button = tk.Button(
            container, text=text, font=("Helvetica", font_size), fg="white", bg="#58a6ff", width=width, command=command,
            activebackground="#0073e6", activeforeground="white", relief="raised", bd=2
        )
        return button

    def toggle_cell_with_mouse(self, event):
        """Permet à l'utilisateur de cliquer sur une cellule pour inverser son état.""" 
        x = (event.x - self.offset_x) // self.cell_size
        y = (event.y - self.offset_y) // self.cell_size
        if 0 <= x < self.game.size and 0 <= y < self.game.size:
            self.game.toggle_cell(y, x)
            self.update_grid_display()

    def play_stop_game(self):
        """Démarre ou arrête la boucle de mise à jour du jeu."""
        if not self.is_running:
            self.is_running = True
            self.start_stop_button.config(text="Stop")  
            print("Jeu démarré")  
            self.run_game_step() 
        else:
            self.is_running = False
            self.start_stop_button.config(text="Play")  
            print("Jeu arrêté")  

    def run_game_step(self):
        """Met à jour la grille à chaque étape."""
        if self.is_running:
            self.game.update()
            self.update_grid_display()  
            self.root.after(100, self.run_game_step)  
        else:
            print("Le jeu est arrêté")  

    def run_single_step(self):
        """Avance d'une étape dans le jeu sans démarrer la boucle continue."""
        self.game.update()
        self.update_grid_display()

    def randomize_grid(self):
        """Initialise la grille de manière aléatoire."""
        self.game.randomize()
        self.update_grid_display()

    def reset_grid(self):
        """Réinitialise la grille."""
        self.game.reset() 
        self.is_running = False  
        self.start_stop_button.config(text="Play")  
        self.update_grid_display()  
        print("Jeu réinitialisé")  

    def save_grid(self):
        """Sauvegarde l'état actuel de la grille dans un fichier."""
        self.game.save_grid("grid_state.txt")
        messagebox.showinfo("Sauvegarde", "Grille sauvegardée avec succès.")

    def load_grid(self):
        """Charge une grille depuis un fichier."""
        self.game.load_grid("grid_state.txt")
        self.update_grid_display()
        messagebox.showinfo("Chargement", "Grille chargée avec succès.")

    def change_cell_color(self):
        """Permet de changer les couleurs des cellules."""
        color = colorchooser.askcolor()[1]
        if color:
            self.cell_color_alive = color
            self.update_grid_display()

    def update_grid_display(self):
        """Met à jour l'affichage de la grille."""
        self.canvas.delete("all")
        
        for i in range(self.game.size):
            for j in range(self.game.size):
                color = self.cell_color_alive if self.game.grid[i][j] else self.cell_color_dead
                self.canvas.create_rectangle(
                    j * self.cell_size + self.offset_x,
                    i * self.cell_size + self.offset_y,
                    (j + 1) * self.cell_size + self.offset_x,
                    (i + 1) * self.cell_size + self.offset_y,
                    fill=color, outline="black"
                )

    def zoom(self, event):
        """Permet de zoomer ou dézoomer sur la grille."""
        if event.delta > 0:
            self.cell_size = min(self.cell_size + 2, 20)  
        else:
            self.cell_size = max(self.cell_size - 2, 5)   
        self.update_grid_display()

    def start_drag(self, event):
        """Démarre le déplacement de la grille."""
        self.drag_data = {"x": event.x, "y": event.y}

    def drag(self, event):
        """Déplace la grille lors du clic-glisser."""
        self.offset_x += event.x - self.drag_data["x"]
        self.offset_y += event.y - self.drag_data["y"]
        self.update_grid_display()
        self.drag_data = {"x": event.x, "y": event.y}

    def show_rules(self):
        """Affiche les règles du jeu."""
        rules_text = """
        Les règles sont les suivantes:
        - Une cellule vivante avec moins de 2 voisines vivantes meurt (sous-population).
        - Une cellule vivante avec 2 ou 3 voisines vivantes survit.
        - Une cellule vivante avec plus de 3 voisines vivantes meurt (surpopulation).
        - Une cellule morte avec exactement 3 voisines vivantes devient vivante (reproduction).
        """
        messagebox.showinfo("Règles du jeu", rules_text)

    def clear_screen(self):
        """Efface le contenu de l'écran actuel."""
        for widget in self.root.winfo_children():
            widget.destroy()

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = GameOfLifeApp(root)
    root.mainloop()
