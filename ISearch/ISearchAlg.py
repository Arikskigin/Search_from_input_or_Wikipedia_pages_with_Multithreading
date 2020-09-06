import abc
from typing import List
from ISearch.IKeywordPool import IKeywordPool


class ISearchAlg:

    @abc.abstractmethod
    def set_keywordpool(self, keywords: IKeywordPool):
        raise NotImplementedError("ISearchAlg: set_keywordpool")

    @abc.abstractmethod
    def get_keywordpool(self) -> IKeywordPool:
        raise NotImplementedError("ISearchAlg: get_keywordpool")

    @abc.abstractmethod
    def search(self, text: str) -> List[List[str]]:
        raise NotImplementedError("ISearchAlg: search")
