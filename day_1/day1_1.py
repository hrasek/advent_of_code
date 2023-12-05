import re
file_name = 'aoc_day1_input.txt'
with open(file_name, 'r') as file_txt:
    content_list = file_txt.readlines()
res_int = 0
for i in range(len(content_list)):
    dig_list = re.findall('\d', content_list[i])
    res_int += int(dig_list[0] +  dig_list[-1]) 
print(res_int)