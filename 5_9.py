import time # Импортируем time, нужный для нашей функции

def time_this(num_runs=10): # Функция измерения времени выполнения кода, num_runs - количество прогонов
    def decorator(func_to_run):
        def func(*args, **kwargs):
            kl = 0
            for _ in range(num_runs):
                t0 = time.time()
                func_to_run(*args, **kwargs) # вызываем функцию
                t1 = time.time()
                kl += (t1 - t0)
            kl /= num_runs
            fn = func_to_run.__name__
            print("Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, num_runs, kl))
        return func
    return decorator
@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass
f()



