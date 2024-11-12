# ploteris.py
import matplotlib.pyplot as plt

def atvaizduoti_grafika(x, y):
    """Функция для отображения графика на основе координат x и y."""
    plt.plot(x, y, marker='o', linestyle='-', color='b', label="Duomenų grafikas")
    plt.xlabel("X ašis")
    plt.ylabel("Y ašis")
    plt.title("Grafikas pagal duotus duomenis")
    plt.legend()
    plt.grid(True)
    plt.show()
