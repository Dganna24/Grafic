# duomenys.py

def generuoti_duomenis():
    """Функция для генерации данных x и y."""
    x = list(range(10))  # Генерируем x от 0 до 9
    y = [xi ** 2 for xi in x]  # Генерируем y как квадраты элементов x
    return x, y
