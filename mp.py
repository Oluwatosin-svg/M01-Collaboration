import multiprocessing
import time
import datetime
import os

start = time.time()
Firstprocess = ()
Secondprocess = ()
Thirdprocess = ()

print(datetime.datetime.now())
if __name__=="__main__":
    
    
    
    p1 = multiprocessing.Process(target=Firstprocess)
    p2 = multiprocessing.Process(target=Secondprocess)
    p3 = multiprocessing.Process(target=Thirdprocess)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

end = time.time()
    
print("Waited for " +str(end-start)+" seconds")

