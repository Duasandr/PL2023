from abc import ABC, abstractmethod


class State(ABC):
    _reOnPattern = "^(?i:on)"
    _reOffPattern = "^(?i:off)"
    _rePrintPattern = "^(=)"
    _reDigitPatter = "^[0-9]"

    def __init__(self, adder) -> None:
        self._adder = adder

    @classmethod
    @abstractmethod
    def process_text(cls, text: str) -> str:
        pass
