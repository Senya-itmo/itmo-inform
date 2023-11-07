import time, main, task1, task2, task3


start_time = time.time()  # время начала выполнения

for _ in range(100):
    main.main()

end_time = time.time() # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения основного задания x100: {execution_time} секунд")

start_time = time.time()  # время начала выполнения

for _ in range(100):
    task1.task1()

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения доп1 x100: {execution_time} секунд")

start_time = time.time()  # время начала выполнения

for _ in range(100):
    task2.task2()

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения доп2 x100: {execution_time} секунд")

start_time = time.time()  # время начала выполнения

for _ in range(100):
    task3.task3()

end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения доп3 x100: {execution_time} секунд")