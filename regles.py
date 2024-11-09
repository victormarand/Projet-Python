import tkinter as tk

def afficher_regles():
    regles = """
    Le Jeu de la Vie est un automate cellulaire inventé par John Conway en 1970.
    Il se joue sur une grille de cellules, où chaque cellule peut être vivante (1) ou morte (0).
    Les règles sont les suivantes :
    
    1. Une cellule vivante avec moins de deux voisins vivants meurt (sous-population).
    2. Une cellule vivante avec deux ou trois voisins vivants survit.
    3. Une cellule vivante avec plus de trois voisins vivants meurt (sur-population).
    4. Une cellule morte avec exactement trois voisins vivants devient vivante (naissance).
    """
    
    root = tk.Tk()
    root.title("Règles du Jeu de la Vie")
    
    text = tk.Text(root, wrap=tk.WORD)
    text.insert(tk.END, regles)
    text.config(state=tk.DISABLED)
    text.pack(padx=20, pady=20)
    
    button = tk.Button(root, text="Fermer", command=root.destroy)
    button.pack(pady=10)
    
    root.mainloop()
