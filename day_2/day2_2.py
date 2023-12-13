import re

# file_name = 'test.txt'
file_name = "input.txt"
with open(file_name, "r") as file_txt:
    content_list = file_txt.readlines()
output = 0
for i in range(len(content_list)):
    dig_list = re.findall(r"\d+\s\w", content_list[i])
    colours_dict = {}
    power = 0
    for cubes in dig_list:
        if re.findall(r"[a-z]", cubes)[0] not in colours_dict.keys() or (
            int(re.findall(r"\d+", cubes)[0])
            > int(colours_dict[re.findall(r"[a-z]", cubes)[0]])
        ):
            colours_dict.update(
                {re.findall(r"[a-z]", cubes)[0]: re.findall(r"\d+", cubes)[0]}
            )
    power = int(colours_dict["r"]) * int(colours_dict["b"]) * int(colours_dict["g"])
    output += power
print(output)
