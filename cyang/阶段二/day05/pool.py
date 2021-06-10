"""进程池"""

from multiprocessing import pool
from time import sleep
import os
#进程池事件
def fun(msg):
    sleep(2)
    print(os.getpid(),":",msg)
#创建进程池对象
pool=pool()
#添加进程事件
for i in range(10):
    msg = "Tedu%d"%i
    pool.apply_async(func=fun,args=(msg,))
 #关闭进程池
pool.close()
#回收进程池
pool.join()