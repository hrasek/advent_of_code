import regex as re

# TODO: Requirements.txt
# TODO: Rewrite the tasks to functions.

file_name = 'aoc_day1_input.txt'
#file_name = 'test.txt'
with open(file_name, 'r') as file_txt:
    content_list = file_txt.readlines()
res_int = 0
translator = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'} 
for i in range(len(content_list)):
    dig_list = re.findall('\d|one|two|three|four|five|six|seven|eight|nine', content_list[i], overlapped=True)
    for j in range(len(dig_list)):
        if dig_list[j] in list(translator.keys()):
            dig_list[j] =  translator[dig_list[j]]
    res_int += int(dig_list[0] +  dig_list[-1]) 

print(res_int)