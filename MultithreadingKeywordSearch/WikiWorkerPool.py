from MultithreadingKeywordSearch.RateLimit.RateLimiting import RateLimitingThread
from MultithreadingKeywordSearch.DataSearchWorker import DataSearchWorker
from MultithreadingKeywordSearch.DataProvider.Wikipedia import Wikipedia
from ISearch.IKeywordSearch import IKeywordSearch


class WikiWorkerPool:

    def __init__(self, keyword_search: IKeywordSearch, requests_per_second: int, number_of_workers: int):
        """
        :param keyword_search: keyword search with the alg
        :param requests_per_second: from config
        :param number_of_workers: from config
        worker thread:
        initialize  of the parameters and starting the worker threads from i+1 to number_of_workers,we give it Wikiclass
        so then can make request to the random pages also we send RateLimitingAcquire class for balancing request
        ratelimit thread:
        initialize the thread  with the parameters for the limiting of requests,1 stands for 1 second
        """
        self.requests_per_second = requests_per_second
        self.number_of_workers = number_of_workers
        self.watchdog_rate_limit = RateLimitingThread(self.requests_per_second, 1)
        self.keyword_search = keyword_search
        self.data_provider_workers = list()
        for i in range(0, self.number_of_workers):
            self.data_provider_workers.append(DataSearchWorker(i + 1, self.keyword_search, Wikipedia(),
                                                self.watchdog_rate_limit.get_rate_sem_acquire()))

    def run(self):
        """
        :return: none
        start the rate limit class, and the workers class from the list we initiated in the constructor,we can use the
        # line to make the main not continue when threads are activated.(after this point)
        """
        self.watchdog_rate_limit.start()
        for data_provider_worker in self.data_provider_workers:
            data_provider_worker.start()
        #self.watchdog_rate_limit.join() # if we prefeer that main will not continue