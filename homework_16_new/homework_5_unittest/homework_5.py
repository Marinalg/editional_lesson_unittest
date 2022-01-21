def homework(first_line: str = "john mart james Morgan Adam Maria huang"):
    data_list = ['john marta james Morgan Adam Maria huang']
    line_width = 21
    first_line: str = "Names".center(line_width, '*')
    line_format = '{:>21\n' * len(data_list)
    all_lines_nf = f'{first_line}\n{line_format}'
    return all_lines_nf.format(*data_list)




