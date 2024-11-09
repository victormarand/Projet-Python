import numpy as np

class GameOfLife:
    def __init__(self, size=50):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

    def set_custom_rules(self, survive_neighbors, birth_neighbors):
        """Applique les règles personnalisées."""
        self.survive_neighbors = survive_neighbors
        self.birth_neighbors = birth_neighbors
    def update(self):
        """Met à jour l'état de la grille selon les règles du Jeu de la Vie."""
        new_grid = np.zeros_like(self.grid)
        for i in range(self.size):
            for j in range(self.size):
                alive_neighbors = self.count_alive_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        new_grid[i][j] = 1
                elif alive_neighbors == 3:
                    new_grid[i][j] = 1
        self.grid = new_grid

    def count_alive_neighbors(self, x, y):
        """Compte les voisins vivants autour de la cellule (x, y)."""
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        alive_count = 0
        for dx, dy in neighbors:
            nx, ny = (x + dx) % self.size, (y + dy) % self.size  # Mode "wrap-around"
            alive_count += self.grid[nx, ny]
        return alive_count

    def randomize(self):
        """Initialise la grille de manière aléatoire."""
        self.grid = np.random.randint(2, size=(self.size, self.size))

    def reset(self):
        """Réinitialise la grille à l'état mort."""
        self.grid = np.zeros((self.size, self.size), dtype=int)

    def toggle_cell(self, x, y):
        """Inverser l'état d'une cellule (vivante <-> morte)."""
        self.grid[x, y] = 1 - self.grid[x, y]

    def save_grid(self, filename):
        """Sauvegarde l'état actuel de la grille dans un fichier texte."""
        with open(filename, 'w') as file:
            for row in self.grid:
                file.write("".join(map(str, row)) + "\n")

    def load_grid(self, filename):
        """Charge l'état de la grille à partir d'un fichier texte."""
        with open(filename, 'r') as file:
            self.grid = np.array(
                [[int(char) for char in line.strip()] for line in file.readlines()],
                dtype=int
            )

    def toggle_cell_with_mouse(self, event):
        """Permet à l'utilisateur de cliquer sur une cellule pour inverser son état."""
        cell_size = 10  # La taille de chaque cellule sur le canevas
        x, y = event.x // cell_size, event.y // cell_size  # Calcul de la position de la cellule cliquée
        if 0 <= x < self.game.size and 0 <= y < self.game.size:
            self.game.toggle_cell(y, x)  # Inverser l'état de la cellule cliquée
            self.update_grid_display()  # Met à jour l'affichage après modification
