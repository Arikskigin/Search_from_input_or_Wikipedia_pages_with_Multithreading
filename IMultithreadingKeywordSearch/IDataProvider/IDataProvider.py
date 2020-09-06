import abc
from typing import Dict


class IDataProvider:

    @abc.abstractmethod
    def get_response(self) -> Dict:
        raise NotImplementedError("IDataProvider: get_response")
