def str_to_dict(source_str: str):
    result = {'ingredient_name': source_str.split(' | ')[0],
              'quantity': int(source_str.split(' | ')[1]),
              'measure': source_str.split(' | ')[2].strip()}
    return result


def read_from_file(file_name: str):
    book = {}
    recipes_names = []
    with open(file_name, 'r', encoding='UTF-8') as f:
        i = 1
        curr_name = ''
        for line in f:
            if line != '\n':
                if i == 1:
                    book[line.strip()] = []
                    curr_name = line.strip()
                    i = 2
                elif '\n' not in line:
                    recipes_names.append(str_to_dict(line))
                    book[curr_name] = recipes_names
                else:
                    if i == 2:
                        i = 0
                        continue
                    else:
                        recipes_names.append(str_to_dict(line))
            else:
                book[curr_name] = recipes_names
                recipes_names = []
                i = 1
    return book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


cook_book = read_from_file('recipes.txt')
dish = ['Фахитос', 'Омлет']
count_of_person = 3
task2 = get_shop_list_by_dishes(dish, count_of_person)
print(task2)
