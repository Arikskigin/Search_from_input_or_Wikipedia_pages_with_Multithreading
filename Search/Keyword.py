from typing import List
from ISearch.IKeyword import IKeyword


class Keyword(IKeyword):
    # keyword: List[string]
    """
    This class is for saving list of single keywords for example software engineering will be saved as
    ['software','engineering']
    """
    def __init__(self, word: List[str]):
        self.keyword = word

    def get_keyword(self) -> List[str]:
        return self.keyword

    def set_keyword(self, word: List[str]):
        self.keyword = word
