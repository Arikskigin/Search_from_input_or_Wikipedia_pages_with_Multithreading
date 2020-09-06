import threading
from IMultithreadingKeywordSearch.IDataProvider.IDataProvider import IDataProvider
from IMultithreadingKeywordSearch.IRateLimit.IRateLimiting import IRateLimitingAcquire
from ISearch.IKeywordSearch import IKeywordSearch


class DataSearchWorker(threading.Thread):
    """
    threading class, we initiate a thread we give it the search alg using the interface,we give it the wiki using its
    interface and the parameters from config num_of_workers and requests_per_second also the rate limiter class
    with its interface
    """
    def __init__(self, worker_id: int, keyword_search: IKeywordSearch, data_req: IDataProvider,
                 rate_limit: IRateLimitingAcquire):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.keyword_search = keyword_search
        self.rate_limit = rate_limit
        self.data_req = data_req

    def run(self):
        """
        runs until manual stop,we use rate_limit class to balance the limit per requests to the wiki pages,
        we do that by using locks whice return Bool if we can request or not
        we get the response from wiki page(the string),and use the search alg to find the mathes
        and print to screen
        :return:nothing
        """
        while True:
            while self.rate_limit.acquire() is False:
                pass

            try:
                data_res = self.data_req.get_response()
                if data_res['res'] == '':
                    print(F"Worker {self.worker_id}: empty response from data provider\n-----------------")
                    continue
            except Exception as ex:
                print(F"Worker {self.worker_id}: " + str(ex) + "\n-----------------")
                continue

            kw_res = self.keyword_search.search(data_res['res'])
            print(f"Worker: {self.worker_id}\nRandom URL: {data_res['page']}\nMatches: {kw_res}\n-----------------")

