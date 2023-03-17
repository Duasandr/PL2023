import re
import sys
import json
from string_column import CSVStringColumn
from list_column import CSVListColumn


def make_columns(columns, headers, list_re):
    column_index = 0
    for header in headers:

        if header != "":
            re_res = list_re.match(header)

            if re_res:
                column = CSVListColumn(re_res.group('name'),
                                       column_index,
                                       re_res.group('min'),
                                       re_res.group('max'),
                                       re_res.group('func'))
            else:
                column = CSVStringColumn(header, column_index)

            columns.append(column)
            column_index += 1


def make_json(columns, rows):
    """
    Reads all rows and applies a column variable to extract values to a json list of dictionaries
    :param columns:
    :param rows:
    :return:
    """
    json_data = []
    for row in rows[1:]:
        # removes new line
        values = re.split(r',', re.sub(r'\n', "", row))

        dic = {}
        for column in columns:
            # parses a column
            dic[column.get_name()] = column.get_value(values)

        json_data.append(dic)
    return json_data


def main():
    list_re = re.compile(r'(?P<name>\w+){(?P<min>\d+)(,(?P<max>\d+))?}(::(?P<func>\w+))?')
    # negative look behind. fails when a digit is present before a ','
    csv_delim = re.compile(r'(?<!\d),')

    rows = sys.stdin.readlines()

    # splits and removes new line
    headers = csv_delim.split(re.sub(r'\s', "", rows[0]))

    columns = []

    make_columns(columns, headers, list_re)

    json_data = make_json(columns, rows)

    file = open('data.json', 'w')
    json.dump(json_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
