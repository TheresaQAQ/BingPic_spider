import multiprocessing


def thread_start(func, args):
    pool = multiprocessing.Pool(processes=8)
    pool.map(func, args)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出


if __name__ == '__main__':
    pass
