from pprint import pprint

def reading_cookbook_from_file():
    with open('recipes.txt') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            number_ingredients = int(file_obj.readline())
            measure_ingredient = []
            list_ingredients = []
            dictionary_ingredient = {}

            for item in range(number_ingredients):
                measure_ingredient = file_obj.readline().split('|')
                dictionary_ingredient['ingredient_name'] = measure_ingredient[0].strip()
                dictionary_ingredient['quantity'] = int(measure_ingredient[1])
                dictionary_ingredient['measure'] = measure_ingredient[2].strip()
                list_ingredients.append(dictionary_ingredient)
                dictionary_ingredient = {}

            cook_book[dish] = list_ingredients
            file_obj.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = reading_cookbook_from_file()
    list_by_dishes = {}
    weight_distribution = {}
    ingridient_key = ''
    for dish in dishes:

        for ingridient_dish in cook_book[dish]:
            ingridient_key = ingridient_dish['ingredient_name']
            if ingridient_key in list_by_dishes.keys():
                list_by_dishes[ingridient_key]['quantity'] += ingridient_dish['quantity'] * person_count
            else:
                weight_distribution['measure'] = ingridient_dish['measure']
                weight_distribution['quantity'] = ingridient_dish['quantity'] * person_count
                list_by_dishes[ingridient_key] = weight_distribution
            weight_distribution = {}
    return list_by_dishes


cook_book = reading_cookbook_from_file()
pprint(cook_book)

dishes = ['Запеченный картофель', 'Оливье', 'Омлет']
person_count = 2
list_by_dishes = get_shop_list_by_dishes(dishes, person_count)
print(f'\nДля приготовления выбранных блюд: {", ".join(dishes)} \nнеобходимы следующие ингридиенты из расчета на '
      f'{person_count} персоны:')
pprint(list_by_dishes)

dishes = ['Салат на скорую руку', 'Фахитос', 'Омлет']
person_count = 3
list_by_dishes = get_shop_list_by_dishes(dishes, person_count)
print(f'\nДля приготовления выбранных блюд: {", ".join(dishes)} \nнеобходимы следующие ингридиенты из расчета на '
      f'{person_count} персоны:')
pprint(list_by_dishes)

dishes = ['Салат на скорую руку', 'Фахитос', 'Омлет', 'Запеченный картофель', 'Оливье']
person_count = 4
list_by_dishes = get_shop_list_by_dishes(dishes, person_count)
print(f'\nДля приготовления выбранных блюд: {", ".join(dishes)} \nнеобходимы следующие ингридиенты из расчета на '
      f'{person_count} персоны:')
pprint(list_by_dishes)
