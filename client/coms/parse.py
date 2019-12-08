import sys
import csv


def parse_csv_to_dict(string):
    return csv.DictReader(csv.StringIO(string))


def parse_csv_to_list(string):
    return list(csv.reader(csv.StringIO(string)))


def parse_url():
    return 'http://' + sys.argv[1] + '/backend/python/'


def str_to_params(string):
    if '?' not in string:
        return string, dict()

    string = replace_elements(string)

    table_name, param_str = string.split('?')
    params = dict()
    for param in param_str.split('&'):
        param_name, param_value = param.split('=')
        if is_number(param_value):
            params[param_name] = param_value
        elif param_value == 'now':
            params[param_name] = 'NOW()'
        else:
            params[param_name] = f'"{param_value}"'

    return table_name, params


def replace_elements(string):
    return string.replace('[', '(').replace(']', ')')


def is_number(string):
    return string.replace('.', '', 1).isdigit()