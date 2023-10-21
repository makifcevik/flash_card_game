
# IGNORE
# Made to format the definition line with quotations marks
# To prevent commas being interpreted as a csv comma

with open("./data/words.txt") as data:
    list_of_lines = data.readlines()
    formatted_list = []
    for line in list_of_lines:
        word, definition = line.split(',', 1)
        formatted_string = f'{word},"{definition.strip()}"\n'
        formatted_list.append(formatted_string)
    print(formatted_list)
with open("./data/formatted_words.txt", mode="a") as data:
    for line in formatted_list:
        data.write(line)


