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


# if __name__ == "__main__":
#     #Последовательное суммирование
#     raz_1 = 0
#     mas_1 = []
#     time_1 = []
#     for i in range(5):
#         raz_1 += 20000
#         array_1 = np.random.randint(0, 200, size=raz_1)
#         mas_1.append(raz_1)
#         start_time = time.time()
#         Posled(array_1)
#         time_1.append(float(time.time() - start_time))
#     # print(mas_1)
#     # print(time_1)
#     #Пирамидальное суммирование
#     raz_2 = 0
#     mas_2 = []
#     time_2 = []
#     for i in range(5):
#         raz_2 += 20000
#         array_2 = np.random.randint(0, 200, size=raz_2)
#         mas_2.append(raz_2)
#         start_time = time.time()
#         Piramid(array_2)
#         time_2.append(float(time.time() - start_time))
#     #Сегментное суммирование
#     raz_3= 0
#     mas_3 = []
#     time_3 = []
#     for i in range(5):
#         raz_3 += 20000
#         array_3 = np.random.randint(0, 200, size=raz_3)
#         mas_3.append(raz_3)
#         start_time = time.time()
#         Segment(array_3)
#         time_3.append(float(time.time() - start_time))
#     #Шаговое суммирование
#     raz_3= 0
#     mas_3 = []
#     time_3 = []
#     for i in range(5):
#         raz_3 += 20000
#         array_3 = np.random.randint(0, 200, size=raz_3)
#         mas_3.append(raz_3)
#         start_time = time.time()
#         Step(array_3)
#         time_3.append(float(time.time() - start_time))
#
#     fig, ax = plt.subplots()
#     ax.plot(mas_1, time_1, label='Послед')
#     ax.plot(mas_2, time_2, label='Пирамид')
#     ax.plot(mas_3, time_3, label='Сегментный')
#     ax.plot(mas_4, time_4, label='Шаговый')
#     ax.legend()
#     fig.set_figheight(5)
#     fig.set_figwidth(8)
#     ax.set_title('Сравнение работ алгоритмов')
#     plt.show()

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
    print(s)


# if __name__ == '__main__':
#     array = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # print(Piramid(array))
    #print(sum(array))
    #print(Segment(array))
    #print(Step(array))
    #print(multiprocessing.cpu_count())

    # pool = Pool(processes=4)  # cpu 4 core 사용
    # for k in range(2, 6):  # input data: 10^2, 10^3, 10^4, 10^5
    #     pool.map(testFunc, [[bubbleSort, k, 0], [insertionSort, k, 0], [selectionSort, k, 0],  # cpu에게 일을 던져줌
    #                         [shellSort, k, 0], [mergeSort, k, 0], [quickSort, k, 0],
    #                         [heapSort, k, 0], [radixSort, k, 8], [radixSort, k, 16], [radixSort, k, 32]])
    #     # pool.map(testFunc,[[bubbleSort,k,0]]) # test 1 sorting method
    # pool.close()  # 병렬 처리가 끝났을 때, 프로세스 종료
    # pool.join()
    # numbers = [5, 10, 20, 10, 5, 10, 20, 10, 5, 10, 20, 10, 5, 10, 20, 10]
    # pool = Pool(processes=1)
    # print(pool.map(Step, numbers))



    #start = time()

    # procs = list()
    # for i in range(1, 3):
    #     proc = mp.Process(target=Step, args=(array,))
    #     procs.append(proc)
    #     proc.start()
    #
    # for proc in procs:
    #     proc.join()

def doubler(array):
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


if __name__ == '__main__':
    numbers = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    pool = Pool(processes=6)
    print(pool.map(doubler, numbers))