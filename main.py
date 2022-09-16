from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def OpenFile():
  with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list

def Clear_empty_elements():
  result = []
  for elements in OpenFile():
    not_empty = []
    for items in elements:
      if len(items) > 0:
        not_empty.append(items)
    result.append(not_empty)
  return result

def get_names():
  pattern = r'([А-ЯЁ]\w+)'
  result = []
  data = Clear_empty_elements()
  for elements in data:
    temp_list = []
    for items in elements:
      word_list = re.findall(pattern, items)
      if len(word_list) > 0:
        for names in word_list:
          temp_list.append(names)
      else:
        temp_list.append(items)
    result.append(temp_list)
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