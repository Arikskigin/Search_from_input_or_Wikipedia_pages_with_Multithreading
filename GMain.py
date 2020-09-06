import sys
import json
from Search.KeywordPool import KeywordPool
from Search.KeywordSearch import KeywordSearch
from Search.SearchAlgs.KMPSearchAlg import KMPSearchAlg
from MultithreadingKeywordSearch.WikiWorkerPool import WikiWorkerPool

CONFIGURATION_FILE = "config.json"


def get_gm_config():
    """
    :return: return config file
    """
    with open(CONFIGURATION_FILE) as gm_json_config:
        return json.load(gm_json_config)


def load_keyword_search(gm_config: dict):
    """
    :param gm_config: get params from config
    sets our keywords from the file with keywordPool makes list[list] from it, return instance of KeyWordSearch with the
    search algorithm we set to the class
    """
    keywords_file = open(gm_config.get("keywords_file"), "r", encoding="utf-8")
    kyw_pool = KeywordPool()
    kyw_pool.set_keywordpool_from_data(keywords_file)
    src_alg = KMPSearchAlg(kyw_pool)
    return KeywordSearch(src_alg)


def gm_part1(kw_search):
    input_string = input("Enter text: ")
    res = kw_search.search(input_string)
    print("Input: " + input_string)
    print("Output: " + res)


def gm_part2(gm_config, kw_search):
    """
    sets the worker pool with keyWordSearch with initiated alg and parameters from config then runs the thread non stop
    """
    wiki_worker_pool = WikiWorkerPool(kw_search, gm_config.get("requests_per_second"), gm_config.get("number_of_workers"))
    wiki_worker_pool.run()


if __name__ == '__main__':
    try:
        gm_config = get_gm_config()
        kw_search = load_keyword_search(gm_config)
        print("Config: " + str(gm_config))
        print("Menu:")
        print("1. Keyword searching by your text")
        print("2. Keyword searching by wikipedia random pages & multithreading workers")
        choose = input("Please enter assignment part: ")
        if choose == "1":
            gm_part1(kw_search)
            sys.exit(0)
        if choose == "2":
            gm_part2(gm_config, kw_search)
            sys.exit(0)
        raise NotImplementedError("Part does not exist")
    except Exception as err:
        print("Unexpected error occurred: " + str(err))
        sys.exit(1)
