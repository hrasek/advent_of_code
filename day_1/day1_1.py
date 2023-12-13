import re
file_name = 'aoc_day1_input.txt'
file_name = 'test.txt'
res_int = 0

# TODO: Automatic test of this function.
# TODO: Black all codes.
# TODO: Map of the progress, dictionary, knowledge base. Story of the project for job interview.

with open(file_name, 'r') as file_txt:
    for row in file_txt:
        dig_list = re.findall('\d', row)
        if dig_list:
            res_int += int(dig_list[0] +  dig_list[-1])
print(res_int)