import multiprocessing
import datetime


def worker():
    """worker function"""
    print 'Worker'
    return


if __name__ == '__main__':
    start_time = datetime.datetime.now()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()