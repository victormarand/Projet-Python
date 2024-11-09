import numpy as np

def save_grid(grid, filename="grid_state.txt"):
    """Sauvegarde l'état de la grille dans un fichier."""
    np.savetxt(filename, grid, fmt='%d')

def load_grid(filename="grid_state.txt"):
    """Charge l'état de la grille depuis un fichier."""
    return np.loadtxt(filename, dtype=int)
