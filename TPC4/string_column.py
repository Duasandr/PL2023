from column import CSVColumn


class CSVStringColumn(CSVColumn):
    def __init__(self, name, column_index):
        super().__init__(name, column_index)

    def get_value(self, csv_row: [str]) -> str:
        """
        Returns the value as a simple string
        :param csv_row:
        :return:
        """
        return csv_row[self._column_index]
