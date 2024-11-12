# main.py

from duomenys import generuoti_duomenis
from ploteris import atvaizduoti_grafika

# Генерация данных
x, y = generuoti_duomenis()

# Построение графика
atvaizduoti_grafika(x, y)
