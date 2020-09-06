import abc
from ISearch.ISearchAlg import ISearchAlg


class IKeywordSearch:

    @abc.abstractmethod
    def set_searchalg(self, search_alg: ISearchAlg):
        raise NotImplementedError("IKeywordSearch: set_searchalg")

    @abc.abstractmethod
    def get_searchalg(self) -> ISearchAlg:
        raise NotImplementedError("IKeywordSearch: get_searchalg")

    @abc.abstractmethod
    def search(self, text: str) -> str:
        raise NotImplementedError("IKeywordSearch: search")


