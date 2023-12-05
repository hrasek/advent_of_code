import re
#file_name = 'test.txt'
file_name = 'input.txt'
with open(file_name, 'r') as file_txt:
    content_list = file_txt.readlines()
output = 0
for i in range(len(content_list)):
    dig_list = re.findall('\d+\s\w', content_list[i])
    for j in range(len(dig_list)):
        cubes = dig_list[j]
        condition_b = ((int(re.findall('\d+', cubes)[0]) > 14) and (re.findall('[a-z]', cubes)[0] == 'b'))
        condition_g = ((int(re.findall('\d+', cubes)[0]) > 13) and (re.findall('[a-z]', cubes)[0] == 'g'))
        condition_r =  ((int(re.findall('\d+', cubes)[0]) > 12) and (re.findall('[a-z]', cubes)[0] == 'r'))
        if condition_b or condition_g or condition_r:              
            break
    else:
        output += i+1
print(output)