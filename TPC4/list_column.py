from column import CSVColumn


class CSVListColumn(CSVColumn):
    def __init__(self, name, column_index: int, min_size: str, max_size: str, aggregation_function: str):
        super().__init__(name, column_index)
        self._min_size = int(min_size)

        if max_size:
            self._max_size = int(max_size)
        else:
            self._max_size = self._min_size

        self._aggregation_function = aggregation_function

    def get_value(self, csv_row: [str]):
        """
        Returns the value of the column. Returns a list if no aggregation function is set
        :param csv_row:
        :return:
        """
        start = self._column_index
        end = start + self._max_size

        values = []
        for x in csv_row[start:end]:
            if x != "":
                values.append(int(x))

        if self._aggregation_function:

            if self._aggregation_function == "sum":
                return sum(values)

            if self._aggregation_function == "mean":
                return sum(values) / len(values)
        else:
            return values
