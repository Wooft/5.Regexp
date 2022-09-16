from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def OpenFile():
    with open("phonebook_raw.csv", encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def get_names(): ##Помещение ФИО в соответствующие поля
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


def get_numbers(): ##Исправление номеров телефона
    data  = get_names()
    result = []
    pattern = r'(\+7|8)?(\s*)?(\()?(\d\d\d)(\))?[-\s*]?(\d\d\d)[-\s]*(\d\d)[-\s]*(\d\d)\s*(\()?(\доб.)?\s*(\d*)(\))?'
    suns = r'+7(\4)\6-\7-\8 \10 \11'
    for  lists in data:
        for elements in lists:
            number = re.findall(pattern, elements)
            if len(number) > 0:
                num_res = re.sub(pattern, suns, elements)
                lists.pop(-2)
                lists.insert(-1, num_res)
            else:
                pass
    return data

def del_duplicate():
    data = get_numbers()
    for lists in data:
        print(lists)
        if lists[0] and lists[1]:

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV


if __name__ == "__main__":
   del_duplicate()
   # with open("phonebook.csv", "w", encoding='UTF-8') as f:
   #     datawriter = csv.writer(f, delimiter=',')
   #     # Вместо contacts_list подставьте свой список
   #     datawriter.writerows(get_numbers())
