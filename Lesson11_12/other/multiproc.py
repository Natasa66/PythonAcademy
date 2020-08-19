import _multiprocessing
import threading
import time

def funkcia1(param):
    for _ in range(10):
        print("Funkcia1")
        print("Param: {}".format(param))
        time.sleep(1)
    return True

def funkcia2():
    for _ in range(10):
        print("Funkcia2")
        time.sleep(2)
    return False

# ak by som ich pustila po sebe, vykonaval by funkcia1 potom funkcia2, po kazdej pocka 1 resp. 2 sekundy

#Ak to dam do threadu, tak budu bezat obe naraz

if __name__ == "__main__":
    t1 = threading.Thread(target=funkcia1, args=("Ahoj",))    # viem tomu poslat aj nejaky parameter
    t2 = threading.Thread(target=funkcia2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    #--------------------------------------------------------------------
    # multiprocessing:
    # p1 = multiprocessing.Process(target=funkcia1, args=("Ahoj",))
    # p2 = multiprocessing.Process(target=funkcia2)
    # p1.start()
    # p2.start()
    #