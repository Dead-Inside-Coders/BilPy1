import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing as mp
from multiprocessing import Pool


# Последовательное суммирование
def Posled(array):
    sum = 0
    for i in array:
        sum += i


# Пирамидальное суммирование
def Piramid(array):
    y = array
    m = len(array)
    while m != 1:
        i = 0
        j = m - 1
        while i < j:
            y[i] = y[i] + y[j]
            i = i + 1
            j = j - 1
        m = int((m + 1) / 2)
    return y[0]


# Сегментное суммирование
def Segment(array):
    threadCount = 1
    n = len(array)
    y = np.arange(threadCount)
    m = int(n / threadCount + 1)
    start = 0
    finish = 0
    k = 0
    while k < threadCount:
        start = k * m
        if (k + 1) * m < n:
            finish = (k + 1) * m
        else:
            finish = n
        i = start
        while i < finish:
            y[k] += array[i]
            i = i + 1
        k = k + 1
    s = y[0]
    i = 1
    while i < threadCount:
        s = s + y[i]
        i = i + 1
    return s


# Шаговое суммирование
def Step(array):
    threadCount = 1
    n = len(array)
    y = np.arange(threadCount)
    k = 0
    while k < threadCount:
        i = k
        while i < n:
            y[k] += array[i]
            i += threadCount
        k = k + 1
    s = y[0]
    i = 1
    while i < threadCount:
        s += y[i]
        i = i + 1
    return s


if __name__ == "__main__":
    # Последовательное суммирование
    raz_1 = 0
    mas_1 = []
    time_1 = []
    for i in range(5):
        raz_1 += 20000
        array_1 = np.random.randint(0, 200, size=raz_1)
        mas_1.append(raz_1)
        start_time = time.time()
        Posled(array_1)
        time_1.append(float(time.time() - start_time))
    # Пирамидальное суммирование
    raz_2 = 0
    mas_2 = []
    time_2 = []
    for i in range(5):
        raz_2 += 20000
        array_2 = np.random.randint(0, 200, size=raz_2)
        mas_2.append(raz_2)
        start_time = time.time()
        Piramid(array_2)
        time_2.append(float(time.time() - start_time))
    # Сегментное суммирование
    raz_3 = 0
    mas_3 = []
    time_3 = []
    for i in range(5):
        raz_3 += 20000
        array_3 = np.random.randint(0, 200, size=raz_3)
        mas_3.append(raz_3)
        start_time = time.time()
        Segment(array_3)
        time_3.append(float(time.time() - start_time))
    # Шаговое суммирование
    raz_4 = 0
    mas_4 = []
    time_4 = []
    for i in range(5):
        raz_4 += 20000
        array_4 = np.random.randint(0, 200, size=raz_4)
        mas_4.append(raz_4)
        start_time = time.time()
        Step(array_4)
        time_4.append(float(time.time() - start_time))
    # Графики
    fig, ax = plt.subplots()
    ax.plot(mas_1, time_1, label='Послед')
    ax.plot(mas_2, time_2, label='Пирамид')
    ax.plot(mas_3, time_3, label='Сегментный')
    ax.plot(mas_4, time_4, label='Шаговый')
    ax.legend()
    fig.set_figheight(5)
    fig.set_figwidth(8)
    ax.set_title('Сравнение работ алгоритмов')
    plt.show()
