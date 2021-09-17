import os

import _thread as thread,time
import threading

# def filho(tid):
#     print("Ola de thread ",tid)
#
# def pai():
#     i=0
#     while True:
#         i +=1
#         thread.start_new_thread(filho,(i,))
#         if input() =='q':break

#pai()



#
# class Minhathread(threading.Thread):
#     def __init__(self, meuId, cont, mutex):
#         self.meuId = meuId
#         self.cont = cont
#         self.mutex = mutex
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(self.cont):
#             with self.mutex:
#                 print('[%s] => %s' % (self.meuId, i))
#
# stdoutmutex = threading.Lock()
# threads = []
#
# for i in range(10):
#     thread = Minhathread(i, 100, stdoutmutex)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# print('Saindo da Thread principal.')

# def contador(meuId,cont):
#     for i in range(cont):
#         time.sleep(1)
#         print('[%s] => %s'%(meuId))
#
# for i in range(5):
#     thread.start_new_thread(contador,(i,10))
#
# time.sleep(6)

# stdoutmutex=thread.allocate_lock()
# # exitmutexes=[False]*10
# #
# # def contador(meuId,cont):
# #     for i in range(cont):
# #         stdoutmutex.acquire()
# #         print('[%s] =: %s'%(meuId,i))
# #         stdoutmutex.release()
# #     exitmutexes[meuId]=True
# # for i in range(10):
# #     thread.start_new_thread(contador, (i, 100))
# #
# # while False in exitmutexes: pass
# #
# # print('Saindo da thread principal.')
#######################################################
# def g():
#     print("ola")
#
# i=0
#
# while True:
#     i +=1
#     thread.start_new_thread(g,())
#     if input() =='q':break

# ####

# mutex=thread.allocate_lock()
# exits=[False]*10
#
# def cont(meu,con):
#     for i in range(con):
#         mutex.acquire()
#         print('[%s] =: %s'%(meu,i))
#         mutex.release()
#     exits[meu]=True
#
# for i in range(10):
#     thread.start_new_thread(cont,(i,10))
# while False in exits:
#     pass
#
# print('Saindo da thread principal.')

def filho(pipeout):
    zzz=0
    while True:
        time.sleep(zzz)
        msg=('Spam %03d'%zzz).encode()
        os.write(pipeout,msg)
        zzz=(zzz+1)%5
def pai(pipein):
    while True:
        linha=os.read(pipein,32)
        print('Pai %d recebeu [%s] as %s' % (os.getpid(), linha, time.time()))

pipein,pipeout=os.pipe()
threading.Thread(target=filho,args=(pipeout,)).start()
pai(pipein)