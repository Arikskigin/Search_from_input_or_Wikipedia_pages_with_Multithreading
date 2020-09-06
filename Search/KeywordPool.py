import re
from typing import Sequence, List, TextIO
from ISearch.IKeyword import IKeyword
from ISearch.IKeywordPool import IKeywordPool
from Search.Keyword import Keyword


class KeywordPool(IKeywordPool):
    # keywords : List[IKeyword]
    """
    this class makes the keywords into a list[list] then we can substract a single keyword from keyword class when we
    iterate on the list
    """
    def __init__(self):
        self.keywords = list()

    def set_keywordpool_from_data(self, data: TextIO):
        rd = data.readlines()
        self.set_keywordpool_from_string(rd)
        data.close()

    def set_keywordpool_from_string(self, data: List[str]):
        """
        :param data: list[str] of our keywords
        after regex work on keywords to make then alphanumerical and lowercase makes them a list[list]
        """
        for line in data:
            kws = re.sub(r'\W+', ' ', line).casefold()
            if len(kws):
                self.keywords.append(Keyword(list(kws.split())))

    def get_keywords(self) -> List[IKeyword]:
        return self.keywords

