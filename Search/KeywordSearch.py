from ISearch.IKeywordSearch import IKeywordSearch
from ISearch.ISearchAlg import ISearchAlg


class KeywordSearch(IKeywordSearch):
    """
    this class gets initiated with search alg and uses the alg to search the keywords with text that comes from string
    (input string or response from wiki page)
    """
    def __init__(self, search_alg: ISearchAlg):
        self.search_alg = search_alg

    def set_searchalg(self, search_alg: ISearchAlg):
        self.search_alg = search_alg

    def get_searchalg(self) -> ISearchAlg:
        return self.search_alg

    def search(self, text: str) -> str:
        """
        :param text: get text
        :return: Output
        does the search alg  then joins all the result into 1 list and returns it(This is our output for both parts)
        """
        res = self.search_alg.search(text)
        res_one_list = list()
        for rs in res:
            res_one_list.append(" ".join(rs))

        return str(res_one_list)
