from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def OpenFile():
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def get_names():
    pattern = r'([А-ЯЁ]\w+)'
    result = []
    data = OpenFile()
    result.append(data[0])
    for elements in data:
        temp_list = []
        for items in elements[0:2]:
            word_list = re.findall(pattern, items)
            if len(word_list) > 0:
                for names in word_list:
                    temp_list.append(names)
        if len(temp_list) != 0:
            result.append(temp_list)
        if len(temp_list) != 3:
            for i in range(3 - len(temp_list)):
                temp_list.append('')
        temp_list.extend(elements[3:len(elements)])
    return result


def get_numbers():
    pattern = r'(\+7|8)?(\s*)?(\()?(\d\d\d)(\))?\s*(\d\d\d)[-\s]*(\d\d)[-\s]*(\d\d)\s*(\()?(\доб.)?\s*(\d*)(\))?'
    suns = r'+7(\4)\6-\7-\8 \10 \11'


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

if __name__ == "__main__":
   pprint(get_names())
