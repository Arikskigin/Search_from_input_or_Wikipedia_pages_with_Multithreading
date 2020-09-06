import urllib.request
import ssl
from typing import Dict
from IMultithreadingKeywordSearch.IDataProvider.IDataProvider import IDataProvider

WIKIPEDIA_PREFIX_URL_PAGE = "https://en.wikipedia.org/wiki/"


class Wikipedia(IDataProvider):
    """
    in this class we return the request from the random wiki page with its url in a dict format
    """
    def __init__(self, page: str = "Special:Random"):
        self.wiki_req_url = WIKIPEDIA_PREFIX_URL_PAGE + page

    def set_wiki_page(self, page: str = "Special:Random"):
        self.wiki_req_url = WIKIPEDIA_PREFIX_URL_PAGE + page

    def get_wiki_page(self) -> str:
        return self.wiki_req_url

    def get_response(self) -> Dict:
        """
        :return: dict[page,response from wiki page after we read it]
        """
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        conn = urllib.request.urlopen(self.wiki_req_url, context=ctx)
        res = conn.read().decode('utf-8')
        return {'page': conn.url, 'res': res}

