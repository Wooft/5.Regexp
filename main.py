from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
import collections


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
        temp_list.extend(elements[3:7])
    return result


def get_numbers(): ##Исправление номеров телефона
    data  = get_names()
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

def del_duplicate(data: list):
    dict_names = {}
    duplicates = []
    list_of_duplicates = []
    for i in range(1, len(data)):
        if data[i][0:2] not in dict_names.values():
            dict_names[i] = data[i][0:2]
        else:
            pass
    for items in dict_names.values():
        for elements in data:
            if items[0] in elements and items[1] in elements:
                duplicates.append(data.index(elements))
        if len(duplicates) > 1:
            list_of_duplicates.append(duplicates)
        duplicates=[]
    return list_of_duplicates

def del_duplicates():
    list_duplicates = del_duplicate(get_numbers())
    all_duplicates = []
    data = get_numbers()
    new_data = []
    new_data.append(data[0])
    new_lists = []
    for elements in list_duplicates:
        for items in elements:
            for lists in data:
                if data.index(lists) == items:
                    for i in range(7):
                        if lists[i] not in new_lists and len(lists[i]) > 0:
                            new_lists.append('')
                            if i < len(new_lists):
                                new_lists.pop(i)
                            new_lists.insert(i, lists[i])
        new_data.append(new_lists[0:7])
        new_lists = []
    for p in list_duplicates:
        all_duplicates.extend(p)
    for list_data in data[1:len(data)]:
        if data.index(list_data) not in all_duplicates:
            new_data.append(list_data)
    return new_data
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV


if __name__ == "__main__":
   with open("phonebook.csv", "w", encoding='UTF-8') as f:
       datawriter = csv.writer(f, delimiter=',')
       # Вместо contacts_list подставьте свой список
       datawriter.writerows(del_duplicates())
