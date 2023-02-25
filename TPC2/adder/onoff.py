from . import State
import re


class On(State):
    def process_text(self, text: str) -> str:
        if re.match(State._reOffPattern, text):
            self._adder.change_state(Off(self._adder))
            return text[3:]

        if re.match(State._rePrintPattern, text):
            print(self._adder.get_result())
        elif re.match(State._reDigitPatter, text):
            self._adder.add(int(text[0]))

        return text[1:]


class Off(State):
    def process_text(self, text: str) -> str:
        if re.match(State._reOnPattern, text):
            self._adder.change_state(On(self._adder))
            return text[2:]

        if re.match(State._rePrintPattern, text):
            print(self._adder.get_result())

        return text[1:]
