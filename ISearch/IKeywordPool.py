import abc
from typing import List
from ISearch.IKeyword import IKeyword


class IKeywordPool:

    @abc.abstractmethod
    def set_keywordpool_from_data(self, data: object):
        raise NotImplementedError("IKeywordPool: set_keywordpool_from_data")

    @abc.abstractmethod
    def set_keywordpool_from_string(self, data: List[str]):
        raise NotImplementedError("IKeywordPool: set_keywordpool_from_string")

    @abc.abstractmethod
    def get_keywords(self) -> List[IKeyword]:
        raise NotImplementedError("IKeywordPool: get_keywords")
