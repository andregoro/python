import _thread as thread


def io(tid):
    print('Ola da thread', tid)


def ola():
    i = 0
    while i<2:
        i += 1
        thread.start_new_thread(io, (i,))
        input()


#ola()

#####################################
import _thread as thread, time


def contador(cont):
    for i in range(cont):
        time.sleep(1)
        mutex.acquire()
        print('[%s] ' % (i))
        mutex.release()


mutex = thread.allocate_lock()
for i in range(5):
    thread.start_new_thread(contador, (i,))

time.sleep(6)
print('Saindo da thread principal.')
