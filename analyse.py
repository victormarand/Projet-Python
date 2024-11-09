import matplotlib.pyplot as plt

def plot_population_over_time(population_history):
    """Trace l'évolution de la population de cellules vivantes au fil du temps."""
    plt.plot(population_history)
    plt.xlabel("Temps")
    plt.ylabel("Population Vivante")
    plt.title("Évolution des Cellules Vivantes")
    plt.show()
