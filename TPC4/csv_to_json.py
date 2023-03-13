import re
import sys
import json


def make_csv_row_re(column_names: list[str]) -> re.Pattern:
    pattern = ''

    for group_name in column_names[:len(column_names) - 2]:
        if group_name != "":
            pattern += f'(?P<{group_name}>' + r'\w+)[,|;]+'
    pattern += f'(?P<{column_names[len(column_names) - 2]}>' + r'\w+)(?=\n)*'

    return re.compile(pattern)


def main():
    csv_lines = sys.stdin.readlines()

    csv_header = csv_lines[0]

    csv_delim = re.compile(r'[,|;]')
    list_re = re.compile(r'\w+{\d+(,\d+)?}')

    csv_header = re.sub('\n', '', csv_header)
    column_names = csv_delim.split(csv_header)
    print(csv_header)

    data = []

    for csv_line in csv_lines[1:]:
        csv_line = re.sub('\n', '', csv_header)
        column_values = csv_delim.split(csv_line)

        if len(column_values) == len(column_names):
            dic = {}
            for i in range(len(column_names)):
                dic[column_names[i]] = column_values[i]
            data.append(dic)

    file = open("data.json", "w")
    json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
