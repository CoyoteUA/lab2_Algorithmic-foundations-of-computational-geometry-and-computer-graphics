import matplotlib.pyplot as plt
import numpy as np

# Назва файлу
file_name = "DS5.txt"

# Функція для зчитування датасету з файлу
def read_dataset(file_name):
    try:
        with open(file_name, "r") as file:
            data = [line.strip().split() for line in file]
            coordinates = [(float(x), float(y)) for x, y in data]
            return coordinates
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        return []
    except ValueError:
        print("Помилка у форматі даних. Перевірте файл.")
        return []

# Зчитування координат
coordinates = read_dataset(file_name)

if coordinates:
    # Встановлення розмірів вікна
    canvas_width = 960
    canvas_height = 540

    # Підготовка до побудови графіку
    x_values, y_values = zip(*coordinates)

    plt.figure(figsize=(canvas_width / 100, canvas_height / 100))
    plt.scatter(x_values, y_values, c="blue", label="Точки")

    # Налаштування осей
    plt.xlim(0, max(x_values) * 1.1)  # Додаємо трохи простору справа
    plt.ylim(0, max(y_values) * 1.1)  # Додаємо трохи простору вгорі
    plt.gca().set_aspect('equal', adjustable='box')  # Рівні масштаби

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Графічне відображення точок")
    plt.legend()

    # Збереження результату у графічний файл
    output_file = "output.png"
    plt.savefig(output_file, dpi=100)
    plt.close()

    print(f"Результат збережено у файл {output_file}.")
else:
    print("Не вдалося зчитати дані.")
