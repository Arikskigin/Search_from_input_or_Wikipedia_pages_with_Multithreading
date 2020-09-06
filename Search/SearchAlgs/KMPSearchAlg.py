import re
from typing import Sequence
from ISearch.ISearchAlg import ISearchAlg
from ISearch.IKeywordPool import IKeywordPool


class KMPSearchAlg(ISearchAlg):
    # keyword_pool : IKeywordPool

    def __init__(self, keyword_pool: IKeywordPool):
        self.keyword_pool = keyword_pool

    def set_keywordpool(self, keyword_pool: IKeywordPool):
        self.keyword_pool = keyword_pool

    def get_keywordpool(self) -> IKeywordPool:
        return self.keyword_pool

    def search(self, text: str) -> Sequence[Sequence[str]]:
        """
        :param text: gets string of text from wiki or input string
        :return:list of matches
        this works the text like it does with the keywords, then i iterate from each  single list of
        keywords(class keyword) i use a modified version of the KMS Search alg to check if a a word is in the text,
        the modifications to the KMS search is to include the edge cases in our version of the search alg but mostlly
        it does what it was intended in the first place
        """
        keywords = self.keyword_pool.get_keywords()
        res = list()
        casefold_text = re.sub(r'\W+', ' ', text).casefold()
        for words in keywords:
            lwords = words.get_keyword()
            if self.KMPSearch(lwords, casefold_text):
                res.append(lwords)
        return res

    def KMPSearch(self, keywords: list, text: str):
        """
        :param keywords:list of single keywords
        :param text: full string
        :return: Bool value if single keyword exist in text
        """
        i_word = 0
        pat = keywords[i_word]
        M, N, = len(pat), len(text),
        lps, j = [0] * M, 0  # j is index for pat
        self.computeLPSArray(pat, M, lps)
        i = 0  # index for txt[]
        while i < N:
            if text[i] == ' ' and j != 0:
                j = 0
            elif i_word != 0 and text[i] != ' ' and pat[j] != text[i]:
                i_word = 0
                pat = keywords[i_word]
                M = len(pat)
                lps, j = [0] * M, 0  # j is index for pat
                self.computeLPSArray(pat, M, lps)
                continue
            elif pat[j] == text[i]:
                i += 1
                j += 1
            if j == M:
                if i_word + 1 == len(keywords):
                    if i == N or text[i] == ' ':
                        return True
                    else:
                        if i_word == 0:
                            i += 1
                            j = 0
                            continue
                        else:
                            return False
                i_word += 1
                pat = keywords[i_word]
                M = len(pat)
                lps, j = [0] * M, 0  # j is index for pat
                self.computeLPSArray(pat, M, lps)
            elif i < N and pat[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    @staticmethod
    def computeLPSArray(pat, m, lps):
        """
        :param pat: word
        :param m: length of pat
        :param lps: changes constantly
        :return: changes to lps
        this is the "Table" creating func for the KMS search alg
        """
        len = 0  # length of the previous longest prefix suffix
        lps[0] = 0  # lps[0] is always 0
        i = 1
        # the loop calculates lps[i] for i = 1 to M-1
        while i < m:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                    lps[i] = 0
                    i += 1

