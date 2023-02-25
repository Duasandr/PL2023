from . import State, On


class Adder:
    def __init__(self):
        self.__state = On(self)
        self.__sum = 0

    def change_state(self, state: State):
        self.__state = state

    def process_text(self, text: str) -> str:
        return self.__state.process_text(text)

    def add(self, value: int) -> None:
        self.__sum += value

    def get_result(self) -> int:
        return self.__sum
