import queue
import random
import time

# Створення черги заявок
request_queue = queue.Queue()

# Унікальний номер заявки
request_number = 0

# Функція для генерації нових заявок
def generate_request(urgency):
    global request_number
    request_number += 1
    # Створення заявки як кортеж (номер заявки, тип терміновості)
    request = (request_number, urgency)
    # Додавання заявки до черги
    request_queue.put(request)
    print(f"Заявка #{request_number} ({urgency}) додана до черги.")
    time.sleep(0.2)

# Функція для обробки заявок
def process_request():
    if random.random()>0.5:
        if not request_queue.empty():
            # Видалення заявки з черги для обробки
            request = request_queue.get()
            print(f"Заявка #{request[0]} ({request[1]}) оброблена.")
            time.sleep(0.2)
        else:
            print("Черга пуста.")

# Головний цикл програми
def main():
    try:
        while True:  # Виконується у вічному циклі
            generate_request(random.choice(["звичайна", "термінова", "критична"]))  # Створення нових заявок
            time.sleep(1)  # Імітація затримки
            process_request()  # Обробка заявок
    except KeyboardInterrupt:
        print("\nПрограму перервано користувачем. Вихід...")


if __name__ == "__main__":
    main()