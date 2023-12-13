import re
file_name = 'test.txt'
#file_name = 'input.txt'
with open(file_name, 'r') as file_txt:
    content_list = file_txt.readlines()
for i in range(len(content_list)):
    number_list = re.findall('\d+', content_list[i])
    number_indexes = re.finditer('\d+', content_list[i])
    symbol_list = re.finditer('[^.\w\n]', content_list[i])
    for i in symbol_list:
        print(i.start())
    for i in number_indexes:
        print(i.start(), i.end())
    print(number_list)
print(content_list)