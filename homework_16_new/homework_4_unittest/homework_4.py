def print_escape_table(escape_element, name):
    if 11 < len(name) < 20:
        tab_number = 5
    elif len(name) < 10 or len(name) == 11:
        tab_number = 8
    elif len(name) > 20:
        tab_number = 1
    else:
        tab_number = 0
    return f'\t{escape_element}\t|\{name}' + '\t'* tab_number + '|'



if __name__ == "__main__":
    print('Escape sequences table:')
    print('-' * 45)
    print_escape_table(r'\a', 'Bell (alert)'),
    print_escape_table(r'\b', 'Backspaces'),
    print_escape_table(r'\n', 'New line'),
    print_escape_table(r'\t', 'Horizontal tab'),
    print_escape_table(r'\\', 'Backslash \\'),
    print_escape_table(r'\"', 'Double quotation mark \"'),
    print_escape_table(r'\'', 'Single quotation mark \'')
    print('-' * 45)
