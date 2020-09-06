import abc


class IRateLimitingAcquire:

    @abc.abstractmethod
    def acquire(self) -> bool:
        raise NotImplementedError("IRateLimitingAcquire: get_response")


class IRateLimitingThread:

    @abc.abstractmethod
    def watchdog(self) -> bool:
        raise NotImplementedError("IRateLimitingThread: watchdog")

    def get_rate_sem_acquire(self) -> IRateLimitingAcquire:
        raise NotImplementedError("IRateLimitingThread: get_rate_sem_acquire")
