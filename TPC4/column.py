class CSVColumn:
    def __init__(self, name: str, column_index: int) -> None:
        """
        Parameter constructor
        :param name: Name of the column
        :param column_index:
        """
        self._name = name
        self._column_index = column_index

    @classmethod
    def get_value(cls, csv_row: [str]):
        """
        Returns the value of a given field in a csv row.
        Each field subclass implements a different conversion of the string value.
        :param csv_row: list of string values
        :return:
        """
        pass

    def get_name(self) -> str:
        """
        Returns the name of the column
        :return:
        """
        return self._name
