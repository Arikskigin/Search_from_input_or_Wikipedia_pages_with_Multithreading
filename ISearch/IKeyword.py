import abc
from typing import List


class IKeyword:

    @abc.abstractmethod
    def get_keyword(self) -> List[str]:
        raise NotImplementedError("IKeyword: get_keyword")

    @abc.abstractmethod
    def set_keyword(self, *word: str):
        raise NotImplementedError("IKeyword: set_keyword")
