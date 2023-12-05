import re
#file_name = 'test.txt'
file_name = 'input.txt'
with open(file_name, 'r') as file_txt:
    content_list = file_txt.readlines()
output = 0
for i in range(len(content_list)):
    dig_list = re.findall('\d+\s\w', content_list[i])
    colours_dict = {}
    power = 0
    for j in range(len(dig_list)):       
        cubes = dig_list[j]
        if re.findall('[a-z]', cubes)[0] not in colours_dict.keys() or (int(re.findall('\d+', cubes)[0]) > int(colours_dict[re.findall('[a-z]', cubes)[0]])):
            colours_dict.update({'{}'.format(re.findall('[a-z]', cubes)[0]): '{}'.format(re.findall('\d+', cubes)[0])})
    else:
        power = int(colours_dict['r']) * int(colours_dict['b']) * int(colours_dict['g'])
        output += power
print(output)