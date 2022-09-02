from abc import abstractmethod


class BaseBillAnalysis(object):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def analysis(self, content):
        raise NotImplementedError("need to be implemented")
