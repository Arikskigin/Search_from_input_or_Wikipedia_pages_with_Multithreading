from IMultithreadingKeywordSearch.IRateLimit.IRateLimiting import IRateLimitingAcquire, IRateLimitingThread
import threading
import time

con_wi: threading.Condition = None
lock_wi_x_sec: threading.Lock = None
wi_x_sec: int = None


class RateLimitingAcquire(IRateLimitingAcquire):
    """
    We use global locks to prevent from over requesting and cause a burden on the wikipedia server,the acquire function
    is uses the global sems, each threads first enters then:
    (if unlocked changes state to locked and returns if locked then blocks entrance)
    waits until counter equals zero, with another lock counter decreases then finally realese both locks
    and return Bool if reached end means its True unless some thing happend
    """

    def acquire(self) -> bool:
        global con_wi
        global lock_wi_x_sec
        global wi_x_sec
        hr = True
        try:
            con_wi.acquire()
            while wi_x_sec == 0:
                con_wi.wait()

            try:
                lock_wi_x_sec.acquire()
                wi_x_sec -= 1
            except:
                hr = False
            finally:
                lock_wi_x_sec.release()
        except:
            hr = False
        finally:
            con_wi.release()
        return hr


class RateLimitingThread(threading.Thread, IRateLimitingThread):
    """
    this class is sort of a watchdog class,that keeps every thing in order also when it runs it does the watchdog func
    with notify other threads when they can reenter the "Race" also uses global locks so all get the same instance
     of the lock this is the only thread that sleeps,like in the instruction it sleeps for 1 sec,which we initialized
     from wikiworkerpool class
    """
    def __init__(self, req_per_x_sec: int, x_rate_sec: int):
        threading.Thread.__init__(self)
        self.req_per_x_sec = req_per_x_sec
        self.x_rate_sec = x_rate_sec
        global con_wi
        global lock_wi_x_sec
        global wi_x_sec
        con_wi = threading.Condition(threading.Lock())
        lock_wi_x_sec = threading.Lock()
        wi_x_sec = self.req_per_x_sec

    def run(self):
        """
        only thread that uses sleep
        :return: nothing
        """
        global wi_x_sec
        wi_x_sec = self.req_per_x_sec
        while True:
            time.sleep(self.x_rate_sec)
            while self.watchdog() is False:
                pass

    def watchdog(self) -> bool:
        """
        when needed notifyall other threads to "Wake up" and carry on, after we passed the global locks
        :return: Bool
        """
        global con_wi
        global lock_wi_x_sec
        global wi_x_sec
        hr = True
        try:
            lock_wi_x_sec.acquire()
            try:
                con_wi.acquire()
                con_wi.notifyAll()
                wi_x_sec = self.req_per_x_sec
            except:
                hr = False
            finally:
                con_wi.release()
        except:
            hr = False
        finally:
            lock_wi_x_sec.release()
        return hr

    def get_rate_sem_acquire(self) -> IRateLimitingAcquire:
        return RateLimitingAcquire()
